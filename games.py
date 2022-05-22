import requests
import dotenv
import os


dotenv.load_dotenv()

__AUTH_URL = 'https://id.twitch.tv/oauth2/token'
__TOP_GAMES_URL = 'https://api.twitch.tv/helix/games/top'
__CLIENT_ID = os.getenv('CLIENT_ID')
__CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def __get_access_token():
    auth_params = {
        'client_id': __CLIENT_ID,
        'client_secret': __CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url=__AUTH_URL, params=auth_params)
    response.raise_for_status()

    return response.json()['access_token']


def get_games():
    top_game_headers = {
        'Client-ID': __CLIENT_ID,
        'Authorization': f'Bearer {__get_access_token()}'
    }
    response = requests.get(url=__TOP_GAMES_URL, headers=top_game_headers)
    response.raise_for_status()

    games = {}
    for position, game in enumerate(response.json()['data']):
        games[game['name']] = position + 1

    print(games)
