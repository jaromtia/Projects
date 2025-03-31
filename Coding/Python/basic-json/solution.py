import requests

def fetch_and_process_users():
    url = "http://127.0.0.1:5000/users"

    response = requests.get(url)
    response.raise_for_status()
    user_data = response.json()

    users = [user["name"] for user in user_data]
    # print(users)
    users_and_companies = [{user["company_name"], user["name"]} for user in user_data]
    print(sorted(users_and_companies)) 

    # print(users)

    alphabetical_users = sorted(users)

    print(alphabetical_users)



if __name__ == "__main__":
    fetch_and_process_users()