import requests

def fetch_and_manipulate_users():
    # URL of the Flask backend
    url = "http://127.0.0.1:5000/users"

    response = requests.get(url)
    response.raise_for_status()
    users = response.json()

    # Extract unique company names
    user_companies = {user["company_name"] for user in users}
    print("Unique company names:")
    print(user_companies)

    # Sort companies alphabetically
    sorted_companies = sorted(user_companies)
    print("\nSorted company names:")
    print(sorted_companies)

    # Create a dictionary mapping companies to user names
    company_to_users = {}
    for user in users:
        company = user["company_name"]
        if company not in company_to_users:
            company_to_users[company] = []
            print(company_to_users)
        company_to_users[company].append(user["name"])

    print("\nCompany to user mapping:")
    for company, names in company_to_users.items():
        print(f"{company}: {', '.join(names)}")

if __name__ == "__main__":
    fetch_and_manipulate_users()