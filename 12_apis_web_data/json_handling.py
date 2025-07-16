import json

sample_json = """
{
    "users": [
        {
            "name": "John",
            "age": 30,
            "email": "john@example.com", 
            "active": true
        },
        {
            "name": "Jane",
            "age": 25,
            "email": "jane@example.com",
            "active": false
        }
    ], 
    "meta": {
        "count": 2,
        "page": 1,
        "limit": 10
    }
}
"""

data = json.loads(sample_json)
print(f"Total users: {data['meta']['count']}")

active_users = [user for user in data['users'] if user['active']]
print(f"Active users: {active_users}")

import pandas as pd
users_df = pd.DataFrame(data['users'])
print(users_df)
