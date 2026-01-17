import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"  # Fake API

# 1. View events
def view_events():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        events = response.json()[:5] 
        for event in events:
            print(f"ID: {event['id']}, Title: {event['title']}")
    else:
        print("Failed to fetch events. Status code:", response.status_code)

# 2. Create event
def create_event(title, body):
    data = {"title": title, "body": body, "userId": 1}
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        event = response.json()
        print(f"Event created! ID: {event['id']}, Title: {event['title']}")
    else:
        print("Failed to create event. Status code:", response.status_code)

# 3. Delete event
def delete_event(event_id):
    url = f"{BASE_URL}/{event_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        print(f"Event {event_id} deleted successfully!")
    else:
        print(f"Failed to delete event {event_id}. Status code:", response.status_code)
