import requests

def test_get_random_activity():
    response = requests.get("https://www.boredapi.com/api/activity")
    assert response.status_code == 200
    activity = response.json()
    assert 'activity' in activity

def test_activity_type():
    response = requests.get("https://www.boredapi.com/api/activity")
    assert response.status_code == 200
    activity = response.json()
    assert 'type' in activity
    assert isinstance(activity['type'], str)

# Запуск тестов
test_get_random_activity()
test_activity_type()
