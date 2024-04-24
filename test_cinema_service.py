import requests


def test_get_all_artists(url: str):
    res = requests.get(url).json()
    assert (res == [
        {
            "movies_id": 1,
            "name": "KinoMax",
            "description": "47",
            "visitors": "1 billion",
            "address": "123 Main Street"
        },
        {
            "movies_id": 2,
            "name": "Cineplex",
            "description": "47",
            "visitors": "1 billion",
            "address": "456 Elm Street"
        },
        {
            "movies_id": 3,
            "name": "SilverScreen",
            "description": "47",
            "visitors": "1 billion",
            "address": "789 Oak Avenue"
        },
        {
            "movies_id": 4,
            "name": "StarCinema",
            "description": "47",
            "visitors": "1 billion",
            "address": "1010 Maple Drive"
        },
        {
            "movies_id": 5,
            "name": "GoldenTheater",
            "description": "47",
            "visitors": "1 billion",
            "address": "1212 Pine Lane"
        }
    ])


def test_get_artist_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {'artists_id': 1,
                    'name': 'Kany West',
                    'age': '47',
                    'auditions': '1 billion',
                    'genre': 'rap, R&B, electronic, gospel'})


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/artists/'
    test_get_artist_by_id(URL + '1')
    test_get_all_artists(URL)
