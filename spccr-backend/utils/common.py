# utils/common.py
# Contains commonly used in program methods and variables

from datetime import datetime
import pickle
from pathlib import Path

CHECKPOINTS_FOLDER_PATH = "services/checkpoints"
MODELS_FOLDER_PATH = "models"

APP_DATA_FILENAME_PREFIX = "app_data_dict"
EXCLUDED_APP_DATA_FILENAME_PREFIX = "excluded_app_data"
ERROR_APP_DATA_FILENAME_PREFIX = "error_app_data"

APP_DATA_FILENAME = "app_data_dict-ckpt-fin.p"

PROCESSED_APP_DATA_FILENAME = "processed_game_objects.p"
MODEL_FILENAME = "recommendation_model.pth"

GET_APP_LIST_URL = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
APP_DETAILS_URL = 'https://store.steampowered.com/api/appdetails/'

def print_log(*args):
    print(f"[{str(datetime.now())[:-3]}] ", end="")
    print(*args)

def load_pickle(path_to_load: Path) -> dict:
    obj = pickle.load(open(path_to_load, "rb"))
    return obj

def save_pickle(data, path_to_save: Path):
    with open(path_to_save, "wb") as file:
        pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)

def normalize(value, range_min, range_max):
    return 0 if range_max == range_min else (value - range_min) / (range_max - range_min)