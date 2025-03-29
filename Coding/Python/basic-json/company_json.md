Company JSON manipulation

```python
import requests

def fetch_and_process_users():
    """
    Challenge: User Data Processing and Sorting
    
    Problem Statement:
    Create a function that retrieves user data from the JSONPlaceholder API,
    processes the data, and provides sorting capabilities.
    
    Endpoint: https://jsonplaceholder.typicode.com/users
    
    Requirements:
    1. Fetch all users from the API
    2. Implement methods to sort users by:
       a) Name (alphabetically)
       b) Company name
       c) Unique ID number
    3. Return a list of dictionaries with the following simplified user info:
       - id
       - name
       - email
       - company name
    
    Example output format:
    [
        {
            'id': 1,
            'name': 'Leanne Graham',
            'email': 'Sincere@april.biz',
            'company_name': 'Romaguera-Crona'
        },
        ...
    ]
    
    Bonus challenges:
    - Handle potential network errors
    - Implement error checking for API response
    - Add optional sorting direction (ascending/descending)
    """
```