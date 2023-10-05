"""
A Python script to export data in the JSON format.
"""

import json
import requests
import sys

def main():
    employee_id = sys.argv[1]
    
    # Request employee details and todo list from the API
    response_user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    response_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    
    if response_user.status_code == 200 and response_todos.status_code == 200:
        user_data = json.loads(response_user.text)
        todos_data = json.loads(response_todos.text)
        
        employee_name = user_data.get("name")
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for task in todos_data if task["completed"])
        
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        
        for task in todos_data:
            if task["completed"]:
                print(f"\t {task['title']}")

        # Create a dictionary in the required JSON format
        user_json_data = {
            "USER_ID": [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user_data["username"]
                }
                for task in todos_data
            ]
        }

        # Save the JSON data to a file
        file_name = f'{employee_id}.json'
        with open(file_name, 'w') as json_file:
            json.dump(user_json_data, json_file, indent=4)

    else:
        print("Failed to retrieve data")

if __name__ == "__main__":
    main()
