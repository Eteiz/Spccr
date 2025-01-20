# app.py
# 127.0.0.1:5000
# Defines routes to interact with frontend.
import requests

from services.data_preprocessing import main as data_processing
from models.neural_network import train_and_save_model, predict_best_game
from utils.common import normalize, APP_DETAILS_URL
from utils.hardcoded_data_dicts.graphics import GRAPHICS_DICT
from utils.hardcoded_data_dicts.mac_os import MAC_OS_DICT
from utils.hardcoded_data_dicts.memory import MEMORY_DICT
from utils.hardcoded_data_dicts.processor import PROCESSOR_DICT
from utils.hardcoded_data_dicts.ubuntu_os import UBUNTU_OS_DICT
from utils.hardcoded_data_dicts.windows_os import WINDOWS_OS_DICT
from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

dynamic_dictionaries = {}
neural_input_size = 0
expected_parameters_data_vector_sizes = {}

# Initialize dictionaries and train neural network
def initialize_data():
    global dynamic_dictionaries, neural_input_size, expected_parameters_data_vector_sizes
    (
        unique_supported_languages,
        unique_categories,
        unique_genres,
        max_required_age,
        max_price,
        max_release_date,
        min_release_date
    ) = data_processing()

    dynamic_dictionaries["languages"] = unique_supported_languages
    dynamic_dictionaries["categories"] = unique_categories
    dynamic_dictionaries["genres"] = unique_genres
    dynamic_dictionaries["max_required_age"] = max_required_age
    dynamic_dictionaries["max_price"] = max_price
    dynamic_dictionaries["max_release_date"] = max_release_date
    dynamic_dictionaries["min_release_date"] = min_release_date

    neural_input_size = (
        len(unique_supported_languages)
        + len(unique_categories)
        + len(unique_genres)
        + len(WINDOWS_OS_DICT)
        + len(MAC_OS_DICT)
        + len(UBUNTU_OS_DICT)
        + len(PROCESSOR_DICT)
        + len(GRAPHICS_DICT)
        + len(MEMORY_DICT)
    )
    expected_parameters_data_vector_sizes = {
        "supportedLanguages": len(unique_supported_languages),
        "categories": len(unique_categories),
        "genres": len(unique_genres),
        "windowsOs": len(WINDOWS_OS_DICT),
        "macOs": len(MAC_OS_DICT),
        "linuxOs": len(UBUNTU_OS_DICT),
        "processor": len(PROCESSOR_DICT),
        "graphics": len(GRAPHICS_DICT),
        "ram": len(MEMORY_DICT),
    }
    train_and_save_model(neural_input_size)

@app.route('/dict/filters', methods=['GET'])
def get_filters_dict():
    global dynamic_dictionaries
    try:
        filters = {
            "maxRequiredAge": dynamic_dictionaries.get("max_required_age"),
            "maxPrice": dynamic_dictionaries.get("max_price"),
            "maxReleaseDate": datetime.fromtimestamp(dynamic_dictionaries.get("max_release_date")).strftime(
                '%Y-%m-%d'),
            "minReleaseDate": datetime.fromtimestamp(dynamic_dictionaries.get("min_release_date")).strftime(
                '%Y-%m-%d'),
            "preferenceDataSizes": expected_parameters_data_vector_sizes
        }
        return jsonify(filters), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/dict/languages', methods=['GET'])
def get_languages_dict():
    languages_dict = {str(index): language for index, language in enumerate(dynamic_dictionaries["languages"], start=1)}
    return languages_dict

@app.route('/dict/categories', methods=['GET'])
def get_categories_dict():
    return dynamic_dictionaries["categories"]

@app.route('/dict/genres', methods=['GET'])
def get_genres_dict():
    return dynamic_dictionaries["genres"]

@app.route('/dict/windows', methods=['GET'])
def get_windows_os_dict():
    windows_dict = {str(index): language for index, language in enumerate(WINDOWS_OS_DICT, start=1)}
    return windows_dict

@app.route('/dict/linux', methods=['GET'])
def get_linux_os_dict():
    ubuntu_dict = {str(index): language for index, language in enumerate(UBUNTU_OS_DICT, start=1)}
    return ubuntu_dict

@app.route('/dict/mac', methods=['GET'])
def get_mac_os_dict():
    mac_dict = {str(index): language for index, language in enumerate(MAC_OS_DICT, start=1)}
    return mac_dict

@app.route('/dict/processor', methods=['GET'])
def get_processor_dict():
    processor_dict = {str(index): language for index, language in enumerate(PROCESSOR_DICT, start=1)}
    return processor_dict

@app.route('/dict/memory', methods=['GET'])
def get_memory_dict():
    memory_dict = {str(index): language for index, language in enumerate(MEMORY_DICT, start=1)}
    return memory_dict

@app.route('/dict/graphics', methods=['GET'])
def get_graphics_dict():
    graphics_dict = {str(index): language for index, language in enumerate(GRAPHICS_DICT, start=1)}
    return graphics_dict

@app.route('/game/predict', methods=['PUT'])
def predict_game():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    game_data = request.get_json()
    filters_data_raw = game_data.get('filtersData', {})
    preferences_data_raw = game_data.get('preferencesData', {})

    if not filters_data_raw or not preferences_data_raw:
        return jsonify({"error": "Both 'filtersData' and 'preferencesData' must be provided"}), 400

    expected_filter_keys = {'minRequiredAge', 'maxRequiredAge', 'minPrice', 'maxPrice', 'minReleaseDate', 'maxReleaseDate'}
    if not expected_filter_keys.issubset(filters_data_raw.keys()):
        return jsonify({"error": f"FiltersData must include the keys: {', '.join(expected_filter_keys)}"}), 400

    for preference_data_vector_name, expected_size in expected_parameters_data_vector_sizes.items():
        vector = preferences_data_raw.get(preference_data_vector_name)
        if not vector or len(vector) != expected_size:
            return jsonify({"error": f"'{preference_data_vector_name}' must be a list of size {expected_size}"}), 400

        if not all(isinstance(element, int) for element in vector):
            return jsonify({"error": f"All elements in '{preference_data_vector_name}' must be boolean type"}), 400

    try:
        def parse_date(date_str, default_value):
            try:
                return datetime.strptime(date_str, '%Y-%m-%d').timestamp()
            except (ValueError, TypeError):
                return default_value

        filters_data = {
            'min_required_age': normalize(filters_data_raw.get('minRequiredAge', 0.0), 0.0, dynamic_dictionaries["max_required_age"]),
            'max_required_age': normalize(filters_data_raw.get('maxRequiredAge', 0.0), 0.0, dynamic_dictionaries["max_required_age"]),
            'min_price': normalize(filters_data_raw.get('minPrice', 0.0), 0.0, dynamic_dictionaries["max_price"]),
            'max_price': normalize(filters_data_raw.get('maxPrice', 1.0), 0.0, dynamic_dictionaries["max_price"]),
            'min_release_date': normalize(parse_date(filters_data_raw.get('minReleaseDate'), 0.0), 0.0, dynamic_dictionaries["max_release_date"]),
            'max_release_date': normalize(parse_date(filters_data_raw.get('maxReleaseDate'), 0.0), 0.0, dynamic_dictionaries["max_release_date"]),
        }

        # Map preferencesDataRaw to preferencesData
        preferences_data = {
            'supported_languages': [int(el) for el in preferences_data_raw.get('supportedLanguages', [])],
            'categories': [int(el) for el in preferences_data_raw.get('categories', [])],
            'genres': [int(el) for el in preferences_data_raw.get('genres', [])],
            'windows_os': [int(el) for el in preferences_data_raw.get('windowsOs', [])],
            'mac_os': [int(el) for el in preferences_data_raw.get('macOs', [])],
            'linux_os': [int(el) for el in preferences_data_raw.get('linuxOs', [])],
            'processor': [int(el) for el in preferences_data_raw.get('processor', [])],
            'graphics': [int(el) for el in preferences_data_raw.get('graphics', [])],
            'ram': [int(el) for el in preferences_data_raw.get('ram', [])],
        }

        result = predict_best_game(filters_data, preferences_data, neural_input_size)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/steam/game-details', methods=['GET'])
def get_game_details():
    appids = request.args.get('appids')
    if not appids:
        return jsonify({"error": "No app IDs provided"}), 400

    appids_list = appids.split(',')
    if not all(appid.isdigit() for appid in appids_list):
        return jsonify({"error": "Invalid app IDs provided"}), 400

    try:
        game_details = {}
        for appid in appids_list:
            response = requests.get(f"{APP_DETAILS_URL}?appids={appid}")
            response.raise_for_status()
            game_details[appid] = response.json()

        return jsonify(game_details), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch game details: {str(e)}"}), 500

if __name__ == '__main__':
    initialize_data()
    app.run(debug=False, host="0.0.0.0", port=5000)