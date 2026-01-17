import requests

# Here I will be learning how to use an API and how to intergrate it to my programmes

''' 
    An API is like a waiter 🍽️
    - Your program = customer
    - API = waiter
    - Server (Google Calendar) = kitchen

    Me:
        - “Give me my events”

    API:
        - “Here they are (in JSON format)”


    We use request:
        request module allows us to send http requests        

'''




# 📝 ACTIVITY 1 (DO THIS)

# Write a Python dictionary representing:
    # event title, date, start time, end time

my_dict = {
    "title": "calender",
    "date": "18-01-2026",
    "start_time": "00:06",
    "end_time": "00:30"
}



# Activity 2
# get() → asks the API for data
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# print(response.status_code)
# .json() → converts JSON → Python list/dict
# print(response.json())

'''
📝 ACTIVITY 2
Fetch posts from the API
Print only:
    title, body, (Loop through first 5 items)
'''

if response.status_code == 200:
    data = response.json()[0]
    print(data)

for key in data:
    if key == 'title':
        print(f"title: {data[key]}")
    elif key == "body":
        print(f"body: {data[key]}")