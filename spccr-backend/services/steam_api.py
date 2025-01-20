# services/steam_api.py
# Handles fetching the game data using Steam API endpoints
# Utilizes checkpoint logic in case of unexpected program termination

import requests
import traceback
from collections import deque
import os
import time

from utils.common import *

def get_all_app_id():
    response = requests.get(f"{GET_APP_LIST_URL}")

    if response.status_code != 200:
        print_log("ERROR: STATUS code: " + str(response.status_code))
        print_log("Failed to load app data from Steam")
        return

    try:
        apps_data = response.json()['applist']['apps']
    except Exception:
        traceback.print_exc(limit=5)
        return {}

    apps_ids = []

    for app in apps_data:
        appid = app['appid']
        name = app['name']

        if not name:
            continue
        apps_ids.append(appid)

    return apps_ids


def save_checkpoints(checkpoint_folder, app_data, excluded_app_data, error_app_data):
    if not checkpoint_folder.exists():
        checkpoint_folder.mkdir(parents=True)

    # Create pickle paths
    app_data_path = checkpoint_folder.joinpath(
        APP_DATA_FILENAME_PREFIX + f'-ckpt-fin.p'
    ).resolve()

    excluded_app_data_path = checkpoint_folder.joinpath(
        EXCLUDED_APP_DATA_FILENAME_PREFIX + f'-ckpt-fin.p'
    ).resolve()

    error_app_data_path = checkpoint_folder.joinpath(
        ERROR_APP_DATA_FILENAME_PREFIX + f'-ckpt-fin.p'
    ).resolve()

    # Save data
    save_pickle(app_data, app_data_path)
    print_log(f'Successfully create app_data checkpoint: {app_data_path}')

    save_pickle(excluded_app_data_path, app_data_path)
    print_log(f"Successfully create excluded_app_data checkpoint: {excluded_app_data_path}")

    save_pickle(error_app_data_path, app_data_path)
    print_log(f"Successfully create error_app_data checkpoint: {error_app_data_path}")

    print()

def check_latest_checkpoints(checkpoint_folder):
    all_pickles = []

    # Get all pickles from checkpoint folder
    for root, dirs, files in os.walk(checkpoint_folder):
        all_pickles = list(map(lambda f: Path(root, f), files))
        all_pickles = [p for p in all_pickles if p.suffix == '.p']
        break

    # Load data from pickle files.
    # There may be more than one file with the same filename and ckpt suffix, therefore the list is sorted to get the latest checkpoint

    # app_data
    app_data_ckpt_files = [f for f in all_pickles if APP_DATA_FILENAME_PREFIX in f.name and "ckpt" in f.name]
    app_data_ckpt_files.sort()
    latest_app_data_ckpt_path = app_data_ckpt_files[-1] if app_data_ckpt_files else None

    # excluded_app_data
    excluded_app_data_ckpt_files = [f for f in all_pickles if EXCLUDED_APP_DATA_FILENAME_PREFIX in f.name and "ckpt" in f.name]
    excluded_app_data_ckpt_files.sort()
    latest_excluded_app_data_ckpt_path = excluded_app_data_ckpt_files[-1] if excluded_app_data_ckpt_files else None

    # error_app_data
    error_app_data_ckpt_files = [f for f in all_pickles if ERROR_APP_DATA_FILENAME_PREFIX in f.name and "ckpt" in f.name]
    error_app_data_ckpt_files.sort()
    latest_error_app_data_ckpt_path = error_app_data_ckpt_files[-1] if error_app_data_ckpt_files else None

    return latest_app_data_ckpt_path, latest_excluded_app_data_ckpt_path, latest_error_app_data_ckpt_path


def delete_redundant_app_details(app_details, appid):
    fields_to_remove = [
        'detailed_description',
        'about_the_game',
        'short_description',
        'header_image',
        'capsule_image',
        'capsule_imagev5',
        'website',
        'legal_notice',
        'drm_notice',
        'ext_user_account_notice'
    ]

    app_id_str = str(appid)
    for field in fields_to_remove:
        if field in app_details['data']:
            del app_details['data'][field]

    return app_details


def main():
    print_log("Fetching Steam App Data", os.getpid())
    all_app_ids = get_all_app_id()
    print_log('Total number of apps on Steam:', len(all_app_ids))

    app_data = {}
    excluded_app_data = []
    error_app_data = []

    checkpoint_folder = Path(CHECKPOINTS_FOLDER_PATH).resolve()
    print_log('Checkpoint folder:', checkpoint_folder)

    if not checkpoint_folder.exists():
        print_log(f'Fail to find checkpoint folder: {checkpoint_folder}')
        print_log(f'Creating checkpoint folder.')

        # Crate checkpoints folder if one does not exist
        checkpoint_folder.mkdir(parents=True)

    # Load the latest checkpoints
    latest_app_data_ckpt_path, latest_excluded_app_data_ckpt_path, latest_error_app_data_ckpt_path = check_latest_checkpoints(checkpoint_folder)

    # Get data from checkpoints
    if latest_app_data_ckpt_path:
        app_data = load_pickle(latest_app_data_ckpt_path)
        print_log('Successfully load app_data checkpoint:', latest_app_data_ckpt_path)
        print_log(f'Number of apps in app_data: {len(app_data)}')

    if latest_excluded_app_data_ckpt_path:
        excluded_app_data = load_pickle(latest_excluded_app_data_ckpt_path)
        print_log("Successfully load excluded_app_data checkpoint:", latest_excluded_app_data_ckpt_path)
        print_log(f'Number of apps in excluded_app_data: {len(excluded_app_data)}')

    if latest_error_app_data_ckpt_path:
        error_app_data = load_pickle(latest_error_app_data_ckpt_path)
        print_log("Successfully load error_app_data checkpoint:", latest_error_app_data_ckpt_path)
        print_log(f'Number of apps in error_app_data: {len(error_app_data)}')

    # Remove already fetched, excluded and error app data
    all_app_ids = set(all_app_ids) \
                  - set(map(int, set(app_data.keys()))) \
                  - set(map(int, excluded_app_data)) \
                  - set(map(int, error_app_data))

    # Create queue for fetching app data
    apps_remaining_deque = deque(set(all_app_ids))
    print_log('Number of remaining apps:', len(apps_remaining_deque))

    i = 0
    while len(apps_remaining_deque) > 0:
        appid = apps_remaining_deque.popleft()

        try:
            app_details_response = requests.get(f"{APP_DETAILS_URL}?appids={appid}&filters=basic,controller_support,developers,publishers,price_overview,platforms,categories,genres,release_date&l=english")

            if app_details_response.status_code == 200:
                app_details = app_details_response.json()
                app_details = app_details[str(appid)]

            elif app_details_response.status_code == 429:
                print_log(f'Too many requests. Put App ID {appid} back to deque. Sleep for 10 sec')
                apps_remaining_deque.appendleft(appid)
                time.sleep(10)
                continue

            elif app_details_response.status_code == 403:
                print_log(f'Forbidden access. Put App ID {appid} back to deque. Sleep for 5 min.')
                apps_remaining_deque.appendleft(appid)
                time.sleep(5 * 60)
                continue

            else:
                print_log("ERROR: STATUS code:", app_details_response.status_code)
                print_log(f"Error in App Id: {appid}. Put the app to error apps list.")
                error_app_data.append(appid)
                continue

        except:
            print_log(f"Error in decoding app details request. App id: {appid}")
            traceback.print_exc(limit=5)
            app_details = {'success': False}
            print()

        # If success is not true then the game does not exist and is added to excluded apps list
        if not app_details.get('success'):
            excluded_app_data.append(appid)
            print_log(f'No successful response. Add App ID: {appid} to excluded apps list')
            continue

        if app_details.get('data', {}).get('type') != 'game':
            print_log(f'App\'s type is not game. Add App ID: {appid} to excluded apps list')
            excluded_app_data.append(appid)
            continue

        # Delete redundant part of the data
        delete_redundant_app_details(app_details, appid)
        app_details_data = app_details
        app_details_data['appid'] = appid

        app_data[appid] = app_details_data
        print_log(f"Successfully get content of App ID: {appid}")

        i += 1
        # After 2500 app data which is roughly 1h of time, save a checkpoint
        if i >= 2500:
            save_checkpoints(checkpoint_folder, app_data, excluded_app_data, error_app_data)
            i = 0

    # After enqueuing is over, save final checkpoints
    save_checkpoints(checkpoint_folder, app_data, excluded_app_data, error_app_data)

    print_log(f"Total number of valid apps: {len(app_data)}")
    print_log(f"Total number of skipped apps: {len(excluded_app_data)}")
    print_log(f"Total number of error apps: {len(error_app_data)}")
    print_log('Steam App data successfully fetched. Terminating program.')

if __name__ == '__main__':
    main()



