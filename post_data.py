import requests

# Here I will be posting data

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My First API Post",
    "body": "Learning APIs",
    "userId": 1
}
# Status code 200 - means ok , 201 - measns created

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

# 📝 ACTIVITY 3
def create_event(title, body):
    url = "https://jsonplaceholder.typicode.com/posts"  # Fake API endpoint
    data = {
        "title": title,
        "body": body,
        "userId": 1
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:  # 201 = created
        print("Event created successfully!")
        print(response.json())
    else:
        print("Failed to create event", response.status_code)


create_event("Meeting with team", "Discuss project progress")