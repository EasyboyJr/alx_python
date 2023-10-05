import csv
import json
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        return

    employee_id = sys.argv[1]
    
    # Request employee details and todo list from the API
    response_user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    response_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    
    if response_user.status_code == 200 and response_todos.status_code == 200:
        user_data = json.loads(response_user.text)
        todos_data = json.loads(response_todos.text)
        
        employee_name = user_data.get("name")
        username = user_data.get('username')
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for task in todos_data if task["completed"])
        
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        
        for task in todos_data:
            if task["completed"]:
                print(f"\t {task['title']}")
        
        # Export data in CSV
        file_name = '{}.csv'.format(employee_id)
        with open(file_name, mode='w', newline='',) as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

            # header
            csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

            # write each csv row
            for task in todos_data:
                csv_writer.writerow([employee_id, username, task['completed'], task['title']])
    else:
        print("Failed to retrieve data. Please check the employee ID and API availability.")

if __name__ == "__main__":
    main()