#!/usr/bin/python3
'''
A Python script that, using this REST API, for a given employee ID,
export all information on tasks for all
employees in the JSON format.
'''
import requests
import json

API_URL = 'https://jsonplaceholder.typicode.com'


def gather_data_from_api():
    users_res = requests.get(f'{API_URL}/users').json()
    todos_res = requests.get(f'{API_URL}/todos').json()
    return users_res, todos_res


def main():
    users_res, todos_res = gather_data_from_api()

    all_tasks = {}
    for user in users_res:
        user_id = user.get('id')
        user_name = user.get('username')
        user_tasks = [
            {
                "username": user_name,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            } for todo in todos_res if todo.get('userId') == user_id
        ]
        all_tasks[user_id] = user_tasks

    # Write to JSON
    with open('todo_all_employees.json', mode='w') as file:
        json.dump(all_tasks, file, indent=4)


if __name__ == "__main__":
    main()
