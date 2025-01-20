# models/neutral_network.py
# Trains neural network and saves a model
# Predicts an app id based on preferences vector and filters results based on filters

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import os

from utils.common import *

EPOCHS = 15
HIDDEN_LAYER_SIZE = 128
OUTPUT_LAYER_SIZE = 64

class GameDataset(Dataset):
    def __init__(self, app_data):
        self.app_data = app_data

    def __len__(self):
        return len(self.app_data)

    def __getitem__(self, idx):
        game = self.app_data[idx]
        input_vector = (
            np.concatenate([
                np.array(game['supported_languages']),
                np.array(game['categories']),
                np.array(game['genres']),
                np.array(game['windows_os']),
                np.array(game['mac_os']),
                np.array(game['linux_os']),
                np.array(game['processor']),
                np.array(game['graphics']),
                np.array(game['ram'])
            ])
        )
        return torch.tensor(input_vector, dtype=torch.float32), game['id']

class RecommendationNN(nn.Module):
    def __init__(self, input_size):
        super(RecommendationNN, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, HIDDEN_LAYER_SIZE),
            nn.ReLU(),
            nn.Linear(HIDDEN_LAYER_SIZE, OUTPUT_LAYER_SIZE),
            nn.ReLU(),
            nn.Linear(OUTPUT_LAYER_SIZE, 1)
        )

    def forward(self, x):
        return self.model(x)

def train_and_save_model(input_size):
    app_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", CHECKPOINTS_FOLDER_PATH,
                                 PROCESSED_APP_DATA_FILENAME)
    app_data = load_pickle(app_data_path)

    dataset = GameDataset(app_data)
    dataloader = DataLoader(dataset, batch_size=16, shuffle=True)
    model = RecommendationNN(input_size)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    print_log(f"Training neural network on {len(dataset)} games")
    for epoch in range(EPOCHS):
        epoch_loss = 0.0
        for inputs, _ in dataloader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, torch.zeros_like(outputs))
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        print_log(f"Epoch {epoch + 1}, Loss: {epoch_loss:.4f}")

    model_path = os.path.join(MODEL_FILENAME)
    torch.save(model.state_dict(), model_path)
    print_log(f"Recommendation model saved to {model_path}")

def predict_best_game(filters_data, preferences_data, input_size):
    app_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", CHECKPOINTS_FOLDER_PATH,
                                 PROCESSED_APP_DATA_FILENAME)
    app_data = load_pickle(app_data_path)

    model = RecommendationNN(input_size)
    model_path = os.path.join(MODEL_FILENAME)
    model.load_state_dict(torch.load(model_path))
    model.eval()

    predictions = []

    def calculate_similarity(user_vec, game_vec):
        return np.sum(np.array(user_vec) & np.array(game_vec))

    def calculate_percentage_similarity(user_vec, game_vec):
        intersection = np.sum(np.array(user_vec) & np.array(game_vec))
        union = np.sum(np.array(user_vec) | np.array(game_vec))
        return (intersection / union) * 100 if union != 0 else 0

    def has_minimum_one_match(user_vec, game_vec):
        return (np.array(user_vec) & np.array(game_vec)).any()

    with torch.no_grad():
        for game in app_data:
            input_vector = torch.tensor(
                np.concatenate([
                    np.array(game['supported_languages']),
                    np.array(game['categories']),
                    np.array(game['genres']),
                    np.array(game['windows_os']),
                    np.array(game['mac_os']),
                    np.array(game['linux_os']),
                    np.array(game['processor']),
                    np.array(game['graphics']),
                    np.array(game['ram'])
                ]), dtype=torch.float32
            )
            prediction = model(input_vector.unsqueeze(0)).item()

            supported_languages_similarity = calculate_similarity(preferences_data['supported_languages'], game['supported_languages'])
            categories_similarity = calculate_similarity(preferences_data['categories'], game['categories'])
            genres_similarity = calculate_similarity(preferences_data['genres'], game['genres'])

            supported_languages_percentage = calculate_percentage_similarity(preferences_data['supported_languages'], game['supported_languages'])
            categories_percentage = calculate_percentage_similarity(preferences_data['categories'], game['categories'])
            genres_percentage = calculate_percentage_similarity(preferences_data['genres'], game['genres'])

            os_overlap = sum([
                has_minimum_one_match(preferences_data['windows_os'], game['windows_os']),
                has_minimum_one_match(preferences_data['mac_os'], game['mac_os']),
                has_minimum_one_match(preferences_data['linux_os'], game['linux_os'])
            ])

            hardware_overlap = sum([
                has_minimum_one_match(preferences_data['processor'], game['processor']),
                has_minimum_one_match(preferences_data['graphics'], game['graphics']),
                has_minimum_one_match(preferences_data['ram'], game['ram'])
            ])

            if os_overlap < 1 or hardware_overlap < 1:
                continue

            total_similarity_score = (
                supported_languages_similarity + prediction + categories_similarity + genres_similarity +
                os_overlap + hardware_overlap
            )

            total_percentage_similarity = (
                supported_languages_percentage + categories_percentage + genres_percentage +
                (os_overlap / 3 * 100) + (hardware_overlap / 3 * 100)
            ) / 5

            predictions.append((total_similarity_score, total_percentage_similarity, game['id'], game))

    filtered_predictions = [
        (score, percentage, game_id, game) for score, percentage, game_id, game in predictions
        if (filters_data['min_required_age'] <= game['required_age'] <= filters_data['max_required_age'] and
            filters_data['min_price'] <= game['price'] <= filters_data['max_price'] and
            filters_data['min_release_date'] <= game['release_date'] <= filters_data['max_release_date'])
    ]
    filtered_predictions.sort(key=lambda x: -x[1])

    if filtered_predictions:
        best_match = filtered_predictions[0][2]
        best_match_percentage = filtered_predictions[0][1]

        additional_matches = [
            (game_id, percentage) for _, percentage, game_id, _ in filtered_predictions[1:4]
        ]

        print_log(f"Best match game ID: {best_match} with similarity: {best_match_percentage:.2f}%")
        print_log(f"Additional matches with closest similarity: {additional_matches}")

        return {
            "best_match": {
                "game_id": best_match,
                "similarity_percentage": best_match_percentage
            },
            "additional_matches": additional_matches
        }
    else:
        print_log("No matching game found for given criteria and filters.")
        return {
            "best_match": None,
            "additional_matches": []
        }