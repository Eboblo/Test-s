import requests
import json
from jsonschema import validate

# URL API Basketball
base_url = "https://api-basketball.p.rapidapi.com"
headers = {
    'x-rapidapi-host': "api-basketball.p.rapidapi.com",
    'x-rapidapi-key': "73ce7d2eb9msh519e3e532f65687p17ef07jsn33b6342b17a6"
}

# JSON Schema для списка лиг
league_schema = {
    "type": "object",
    "properties": {
        "response": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                },
                "required": ["id", "name"]
            }
        }
    },
    "required": ["response"]
}

def test_get_all_leagues():
    response = requests.get(f"{base_url}/leagues", headers=headers)
    assert response.status_code == 200
    leagues = response.json()
    validate(instance=leagues, schema=league_schema)

# Запуск теста
test_get_all_leagues()
