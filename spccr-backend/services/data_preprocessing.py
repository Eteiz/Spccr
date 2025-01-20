# services/data_preprocessing.py
# Handles preprocessing the fetched app data for input into the neural network
# Sets up dictionaries for supported languages, categories and genres based on filtered app data

from datetime import datetime
from pathlib import Path
import re
from dataclasses import dataclass

from utils.hardcoded_data_dicts.graphics import *
from utils.hardcoded_data_dicts.mac_os import *
from utils.hardcoded_data_dicts.memory import *
from utils.hardcoded_data_dicts.processor import *
from utils.hardcoded_data_dicts.unique_supported_lang_phrases import *
from utils.hardcoded_data_dicts.ubuntu_os import *
from utils.hardcoded_data_dicts.windows_os import *
from utils.common import load_pickle, print_log, save_pickle, normalize, CHECKPOINTS_FOLDER_PATH, APP_DATA_FILENAME, \
    PROCESSED_APP_DATA_FILENAME

@dataclass
class GameObject:
    id: int
    name: str
    required_age: float
    supported_languages: list
    categories: list
    genres: list
    price: float
    release_date: float
    windows_os: list
    mac_os: list
    linux_os: list
    processor: list
    graphics: list
    ram: list

    def to_dict(self):
        return vars(self)

# Utils functions
def extract_field(requirements, field_name):
    match = re.search(rf'<strong>{field_name}\s*\*?:</strong>\s*([^<]+)', requirements)
    return match.group(1).strip() if match else None
def generate_game_objects(app_data, unique_languages, unique_categories, unique_genres, min_price, max_price, min_release_date, max_release_date, max_required_age):
    game_objects = []
    for details in app_data.values():
        data = details.get('data', {})
        platforms = data.get('platforms', {})

        game = GameObject(
            id=data.get('steam_appid'),
            name=data.get('name', ''),
            required_age=parse_required_age(data.get('required_age', 0),0, max_required_age),
            supported_languages= parse_supported_language(data.get('supported_languages', ''), unique_languages),
            categories= parse_categories(data.get('categories', []), unique_categories),
            genres= parse_genres(data.get('genres', []), unique_genres),
            price=parse_price(data.get('is_free', False), data.get('price_overview', {}).get('final', 0), min_price, max_price),
            release_date=parse_release_date(data.get('release_date', {}).get('coming_soon', False), data.get('release_date', {}).get('date', ''), min_release_date, max_release_date),
            windows_os=parse_windows_os(data.get('pc_requirements', {})),
            mac_os=parse_mac_os(data.get('mac_requirements', {})),
            linux_os=parse_linux_os(data.get('linux_requirements', {})),
            processor=parse_processor(platforms, data.get('pc_requirements', {}), data.get('mac_requirements', {}), data.get('linux_requirements', {})),
            graphics=parse_graphics(platforms, data.get('pc_requirements', {}), data.get('mac_requirements', {}), data.get('linux_requirements', {})),
            ram=parse_memory(platforms, data.get('pc_requirements', {}), data.get('mac_requirements', {}), data.get('linux_requirements', {}))
        )
        game_objects.append(game.to_dict())
    return game_objects
def check_app_data(platforms, pc_requirements, mac_requirements, linux_requirements):
    if not (platforms.get('windows', False) or platforms.get('mac', False) or platforms.get('linux', False)):
        return False

    def extract_requirements(requirement_text):
        if not requirement_text:
            return None, None, None, None

        return (
            extract_field(requirement_text, 'OS'),
            extract_field(requirement_text, 'Processor'),
            extract_field(requirement_text, 'Memory'),
            extract_field(requirement_text, 'Graphics')
        )

    processor, memory, graphics = None, None, None

    if platforms.get('mac', False):
        system, mac_processor, mac_memory, mac_graphics = extract_requirements(mac_requirements.get('minimum', ''))
        if system is None or system not in MAC_ALL:
            return False
        processor, memory, graphics = mac_processor, mac_memory, mac_graphics

    if platforms.get('linux', False):
        system, linux_processor, linux_memory, linux_graphics = extract_requirements(linux_requirements.get('minimum', ''))
        if system is None or system not in UBUNTU_ALL:
            return False
        processor, memory, graphics = linux_processor or processor, linux_memory or memory, linux_graphics or graphics

    if platforms.get('windows', False):
        system, windows_processor, windows_memory, windows_graphics = extract_requirements(pc_requirements.get('minimum', ''))
        if system is None or system not in WINDOWS_ALL:
            return False
        processor, memory, graphics = windows_processor or processor, windows_memory or memory, windows_graphics or graphics

    if ((processor is None or processor not in PROCESSOR_ALL)
            or (memory is None or memory not in MEM_ALL)
            or (graphics is None or graphics not in GRAPHICS_ALL)):
        return False
    return True
def process_requirements(platforms, platform_key, requirements_key, details):
    requirements = details['data'].get(requirements_key, {})
    if platforms.get(platform_key, False):
        if isinstance(requirements, dict):
            requirements.pop('recommended', None)
        elif isinstance(requirements, list) and not requirements:
            platforms[platform_key] = False
            details['data'].pop(requirements_key, None)
            return None
    else:
        details['data'].pop(requirements_key, None)
        return None
    return requirements

# Data dictionaries
def set_supported_languages_dict(app_data):
    unique_supported_languages = set()
    for details in app_data.values():
        supported_languages = details.get('data', {}).get('supported_languages', None)
        if supported_languages:
            languages = [lang.strip() for lang in supported_languages.split(',')]
            for language in languages:
                if any(language.startswith(phrase) for phrase in SUPPORTED_LANGUAGES):
                    for phrase in SUPPORTED_LANGUAGES:
                        if language.startswith(phrase):
                            unique_supported_languages.add(phrase)
                            break
                else:
                    for delimiter in ["<", "&", "[", ";", " "]:
                        if delimiter in language:
                            language = language.split(delimiter)[0]
                            break
                    language = language.split()[0]
                    unique_supported_languages.add(language)
    return sorted(unique_supported_languages)
def set_unique_dict(app_data, key):
    unique_items = {}
    for details in app_data.values():
        items = details.get('data', {}).get(key, [])
        for item in items:
            item_id = item.get('id')
            description = item.get('description')
            if item_id and description:
                unique_items[item_id] = description
    return unique_items
def get_max_price(app_data):
    max_price = 0
    for details in app_data.values():
        price_overview = details.get('data', {}).get('price_overview', {})
        final_price = price_overview.get('final')

        if final_price is not None and final_price > max_price:
            max_price = final_price
    return max_price
def get_min_max_release_date(app_data):
    min_timestamp = float('inf')
    max_timestamp = float('-inf')

    for details in app_data.values():
        release_info = details.get('data', {}).get('release_date', {})

        if not release_info.get('coming_soon', False) and release_info.get('date'):
            release_date_str = release_info['date']
            try:
                if "," in release_date_str:
                    release_date_timestamp = datetime.strptime(release_date_str, "%d %b, %Y").timestamp()
                else:
                    release_date_timestamp = datetime.strptime(release_date_str, "%b %Y").timestamp()

                min_timestamp = min(min_timestamp, release_date_timestamp)
                max_timestamp = max(max_timestamp, release_date_timestamp)

            except ValueError:
                print(f"Unrecognized date format: {release_date_str}")
    return min_timestamp, max_timestamp
def get_max_required_age(app_data):
    max_required_age = float('-inf')

    for details in app_data.values():
        final_required_age = details.get('data', {}).get('required_age', 0)
        match final_required_age:
            case '１８' | '18+' | '18':
                final_required_age = 18
            case '7+':
                final_required_age = 7
            case '99999':
                final_required_age = 0
            case str(age_str) if age_str.isdigit():
                final_required_age = int(age_str)
            case _:
                final_required_age = 0
        if final_required_age is not None and final_required_age > max_required_age:
            max_required_age = final_required_age
    return max_required_age

# Data parsing
def parse_required_age(required_age, min_required_age, max_required_age):
    match required_age:
        case '１８' | '18+' | '18':
            required_age = 18
        case '7+':
            required_age = 7
        case '99999':
            required_age = 0
        case str(age_str) if age_str.isdigit():
            required_age = int(age_str)
        case _:
            required_age = 0
    return normalize(required_age, min_required_age, max_required_age)
def parse_price(is_free, price, min_price, max_price):
    if is_free:
        return normalize(0, min_price, max_price)
    return normalize(price / 100, min_price, max_price)
def parse_release_date(coming_soon, release_date, min_release_date, max_release_date):
    if coming_soon:
        return normalize(max_release_date, min_release_date, max_release_date)
    try:
        if "," in release_date:
            release_date_timestamp = datetime.strptime(release_date, "%d %b, %Y").timestamp()
        else:
            release_date_timestamp = datetime.strptime(release_date, "%b %Y").timestamp()
    except ValueError:
        release_date_timestamp = max_release_date
    return normalize(release_date_timestamp, min_release_date, max_release_date)
def parse_categories(categories_data, categories_dict):
    categories = [0] * len(categories_dict)
    categories_keys = list(categories_dict.keys())
    for category in categories_data:
        cat_id = category.get('id')
        if cat_id in categories_keys:
            index = categories_keys.index(cat_id)
            categories[index] = 1
    return categories
def parse_genres(genres_data, genres_dict):
    genres = [0] * len(genres_dict)
    genres_keys = list(genres_dict.keys())
    for genre in genres_data:
        gen_id = genre.get('id')
        if gen_id in genres_keys:
            index = genres_keys.index(gen_id)
            genres[index] = 1
    return genres
def parse_supported_language(supported_languages_data, supported_languages_dict):
    languages = [0] * len(supported_languages_dict)
    for lang in supported_languages_data.split(','):
        lang = lang.strip()

        if lang == '#lang_slovakian':
            index = supported_languages_dict.index('Slovak')
            languages[index] = 1
            continue

        for phrase in SUPPORTED_LANGUAGES:
            if lang.startswith(phrase):
                lang = phrase
                break
        else:
            for delimiter in ["<", "&", "[", ";", " "]:
                if delimiter in lang:
                    lang = lang.split(delimiter)[0]
                    break
        if lang in supported_languages_dict:
            index = supported_languages_dict.index(lang)
            languages[index] = 1
    return languages

def parse_windows_os(requirements):
    windows_os_vector = [0] * len(WINDOWS_OS_DICT)

    os_name = extract_field(requirements.get('minimum', ''), 'OS')
    if not os_name or os_name not in WINDOWS_OS_MAPPING:
        return windows_os_vector

    index_info = WINDOWS_OS_MAPPING[os_name]
    if len(index_info) == 2:
        start, stop = index_info
        windows_os_vector[start:] = [1] * len(windows_os_vector[start:])
    elif len(index_info) == 3:
        start, stop, step = index_info
        windows_os_vector[start:stop:step] = [1] * len(windows_os_vector[start:stop:step])

    windows_os_vector[len(WINDOWS_OS_DICT) - 1] = 1
    return windows_os_vector
def parse_mac_os(requirements):
    mac_os_vector = [0] * len(MAC_OS_DICT)

    os_name = extract_field(requirements.get('minimum', ''), 'OS')
    if not os_name or os_name not in MAC_OS_MAPPING:
        return mac_os_vector

    index_info = MAC_OS_MAPPING[os_name]
    start, stop = index_info
    mac_os_vector[start:stop] = [1] * len(mac_os_vector[start:stop])

    mac_os_vector[len(MAC_OS_DICT) - 1] = 1
    return mac_os_vector
def parse_linux_os(requirements):
    linux_os_vector = [0] * len(UBUNTU_OS_DICT)

    os_name = extract_field(requirements.get('minimum', ''), 'OS')
    if not os_name or os_name not in UBUNTU_OS_MAPPING:
        return linux_os_vector

    index_info = UBUNTU_OS_MAPPING[os_name]
    start, stop, step = index_info if len(index_info) == 3 else (*index_info, None)
    linux_os_vector[start:stop:step] = [1] * len(linux_os_vector[start:stop:step])

    linux_os_vector[len(UBUNTU_OS_DICT) - 1] = 1
    return linux_os_vector

def parse_memory(platforms, pc_requirements, mac_requirements, linux_requirements):
    memory_vector = [0] * len(MEMORY_DICT)
    memory = None
    if platforms.get('linux', False):
        memory = extract_field(linux_requirements.get('minimum', ''), 'Memory')
    if platforms.get('mac', False):
        memory = extract_field(mac_requirements.get('minimum', ''), 'Memory')
    if platforms.get('windows', False):
        memory = extract_field(pc_requirements.get('minimum', ''), 'Memory')

    if memory and memory in MEMORY_MAPPING:
        start, stop = MEMORY_MAPPING[memory]
        memory_vector[start:stop] = [1] * len(memory_vector[start:stop])

    memory_vector[len(MEMORY_DICT) - 1] = 1
    return memory_vector
def parse_processor(platforms, pc_requirements, mac_requirements, linux_requirements):
    processor_vector = [0] * len(PROCESSOR_DICT)
    processor = None
    if platforms.get('linux', False):
        processor = extract_field(linux_requirements.get('minimum', ''), 'Processor')
    if platforms.get('mac', False):
        processor = extract_field(mac_requirements.get('minimum', ''), 'Processor')
    if platforms.get('windows', False):
        processor = extract_field(pc_requirements.get('minimum', ''), 'Processor')

    if processor and processor in PROCESSOR_MAPPING:
        start, stop = PROCESSOR_MAPPING[processor]
        processor_vector[start:stop] = [1] * (len(processor_vector[start:stop]) if stop else len(processor_vector[start:]))

    processor_vector[len(PROCESSOR_DICT) - 1] = 1
    return processor_vector
def parse_graphics(platforms, pc_requirements, mac_requirements, linux_requirements):
    graphics_vector = [0] * len(GRAPHICS_DICT)

    graphics = None
    if platforms.get('linux', False):
        graphics = extract_field(linux_requirements.get('minimum', ''), 'Graphics')
    if platforms.get('mac', False):
        graphics = extract_field(mac_requirements.get('minimum', ''), 'Graphics')
    if platforms.get('windows', False):
        graphics = extract_field(pc_requirements.get('minimum', ''), 'Graphics')

    if graphics in GRAPHICS_MAPPING:
        start, stop = GRAPHICS_MAPPING[graphics]
        if stop is None:
            graphics_vector[start:] = [1] * (len(graphics_vector) - start)
        else:
            graphics_vector[start:stop] = [1] * (stop - start)

    graphics_vector[len(GRAPHICS_DICT) - 1] = 1
    return graphics_vector

def main():
    app_data_path = (Path(CHECKPOINTS_FOLDER_PATH) / APP_DATA_FILENAME).resolve()
    app_data = load_pickle(app_data_path)

    # Cutting unnecessary data
    app_data_filtered = {}
    for appid, details in app_data.items():

        platforms = details['data'].get('platforms', {})
        pc_requirements = mac_requirements = linux_requirements = None

        details.pop('success', None)
        if 'data' in details:
            details['data'].pop('type', None)
            details['data'].pop('developers', None)
            details['data'].pop('publishers', None)

            price_overview = details['data'].get('price_overview', None)
            if price_overview:
                price_overview.pop('currency', None)
                price_overview.pop('initial', None)
                price_overview.pop('discount_percent', None)
                price_overview.pop('initial_formatted', None)
                price_overview.pop('final_formatted', None)

            # Windows specification
            pc_requirements = process_requirements(platforms, 'windows', 'pc_requirements', details)
            # Mac specification
            mac_requirements = process_requirements(platforms, 'mac', 'mac_requirements', details)
            # Linux specification
            linux_requirements = process_requirements(platforms, 'linux', 'linux_requirements', details)

        if not check_app_data(platforms, pc_requirements, mac_requirements, linux_requirements):
            continue
        app_data_filtered[appid] = details

    unique_supported_languages = [lang for lang in set_supported_languages_dict(app_data_filtered) if lang != '#lang_slovakian']
    unique_categories = set_unique_dict(app_data_filtered, "categories")
    unique_genres = set_unique_dict(app_data_filtered, "genres")

    min_price, max_price = 0, get_max_price(app_data_filtered) / 100
    min_release_date, max_release_date = get_min_max_release_date(app_data_filtered)
    max_required_age = get_max_required_age(app_data_filtered)

    game_objects = generate_game_objects(app_data_filtered,
                                         unique_supported_languages,
                                         unique_categories,
                                         unique_genres,
                                         min_price,
                                         max_price,
                                         min_release_date,
                                         max_release_date,
                                         max_required_age)
    print_log('Total number of apps processed:', len(game_objects))

    # Saving processed data
    output_path = Path(CHECKPOINTS_FOLDER_PATH) / PROCESSED_APP_DATA_FILENAME
    save_pickle(game_objects, Path(CHECKPOINTS_FOLDER_PATH) / PROCESSED_APP_DATA_FILENAME)

    print_log('Game objects saved to:', output_path)
    print_log('Returning dictionaries of languages, categories, names')
    return (unique_supported_languages,
            unique_categories,
            unique_genres,
            max_required_age,
            max_price,
            max_release_date, min_release_date
            )

if __name__ == '__main__':
    main()