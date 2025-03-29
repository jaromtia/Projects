import requests

def fetch_and_process_users():
    url = "http://127.0.0.1:5000/users"

    response = requests.get(url)
    print(response)