'''
A python script that uses the REST API for a given employee ID
returns information about his/her TODO list progress.
'''
# import reqyured modules
import sys
import requests

id = sys.argv[1]

# API endpoint
todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
details_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

# request the API for both the todo and the details
todo = requests.get(todo_url)
employee_details = requests.get(details_url)

if todo.status_code == 200 and employee_details.status_code == 200:
    # parse the JSON response
    todo_data = todo.json()
    details_data = employee_details.json()

    # extract relevant information
    employee_name = details_data['name']

    # number of task completed
    total_tasks = len(todo_data)
    completed_task = sum(1 for task in todo_data if task['completed'])

    # output the result
    print('Employee {} is done with task ({}/{}):'.format(employee_name, completed_task, total_tasks))

    # output title of completed tasks

    for task in todo_data:
        if task['completed']:
            print('\t{}'.format(task['title']))
else:
    print('couldnt retrieve')