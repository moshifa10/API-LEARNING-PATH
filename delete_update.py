import requests

# 📝 ACTIVITY 4
# Simulate deleting an event
# Simulate updating an event title


def delete_event(event_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{event_id}"
    response = requests.delete(url)
    if response.status_code == 200:  # 200 = success
        print(f"Event {event_id} deleted successfully!")
    else:
        print(f"Failed to delete event {event_id}. Status code:", response.status_code)
delete_event(1)


# Update event
def update_event(event_id, new_title):
    url = f"https://jsonplaceholder.typicode.com/posts/{event_id}"
    data = {
        "title": new_title
    }
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print(f"Event {event_id} updated successfully!")
        print(response.json())
    else:
        print(f"Failed to update event {event_id}. Status code:", response.status_code)

update_event(1, "Updated Meeting with Team")
update_event(2, "Updated Gym Time")