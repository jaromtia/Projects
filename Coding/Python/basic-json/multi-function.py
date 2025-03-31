import requests

def fetch_users():
    """
    Fetches user data from JSONPlaceholder API.
    Handles network errors and checks the API response.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching users: {e}")
        return []

def process_users(user_data):
    """
    Extracts relevant user information and returns a simplified list.
    """
    return [
        {
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
            'company_name': user['company']['name']
        }
        for user in user_data
    ]

def sort_users(users, key, descending=False):
    """
    Sorts the users based on the specified key (name, company_name, id).
    Allows optional descending order sorting.
    """
    valid_keys = {'id', 'name', 'company_name'}
    if key not in valid_keys:
        raise ValueError(f"Invalid sort key. Choose from {valid_keys}")
    return sorted(users, key=lambda x: x[key], reverse=descending)

def fetch_and_process_users(sort_key='name', descending=False):
    """
    Main function to fetch, process, and sort user data.
    Default sorting is by name in ascending order.
    """
    user_data = fetch_users()
    if not user_data:
        return []
    processed_users = process_users(user_data)
    return sort_users(processed_users, sort_key, descending)

# Example usage
if __name__ == "__main__":
    users_sorted_by_name = fetch_and_process_users(sort_key='name')
    users_sorted_by_company = fetch_and_process_users(sort_key='company_name')
    users_sorted_by_id_desc = fetch_and_process_users(sort_key='id', descending=True)
    
    print("Sorted by Name:", users_sorted_by_name[:3])  # Print first 3 results
    print("Sorted by Company:", users_sorted_by_company[:3])
    print("Sorted by ID (Descending):", users_sorted_by_id_desc[:3])
