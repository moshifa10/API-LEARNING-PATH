import requests

# 📝 ACTIVITY 4
# Simulate deleting an event
# Simulate updating an event title


delete_data = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print(delete_data.status_code)
print(delete_data.json())