# Import requests module
import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users"

try:
    # Send GET request to API
    response = requests.get(url)

    # Convert response into JSON format
    data = response.json()

    print("Users Data:\n")

    # Display user details
    for user in data:
        print("Name:", user['name'])
        print("Email:", user['email'])
        print("City:", user['address']['city'])
        print("-" * 30)


    # Filtering example
    print("\nUsers from South Christy city:\n")

    for user in data:
        if user['address']['city'] == 'South Christy':
            print(user['name'])


except requests.exceptions.RequestException as e:
    print("API Request Error:", e)

except Exception as e:
    print("Something went wrong:", e)
