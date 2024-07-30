#!/usr/bin/python3
'''
A Python script that, using this REST API,
exports all information on tasks for selected
employee in the JSON format.
'''
import json

import sys

import requests

API_URL = 'https://jsonplaceholder.typicode.com'


def gather_data_from_api(user_id):
    user_res = requests.get(f'{API_URL}/users/{user_id}').json()
    todos_res = requests.get(f'{API_URL}/todos').json()
    return user_res, todos_res


def main():
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            user_res, todos_res = gather_data_from_api(employee_id)
            user_name = user_res.get('name')

            todos = [
                todo for todo in todos_res
                if todo.get('userId') == employee_id
            ]
            todos_done = [todo for todo in todos if todo.get('completed')]

            print(
                f"Employee {user_name} is done with tasks "
                f"({len(todos_done)}/{len(todos)}):"
            )
            for todo in todos_done:
                print(f"\t {todo.get('title')}")

            # Format data for JSON
            tasks = [
                {
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": user_name
                } for todo in todos
            ]
            data = {str(employee_id): tasks}

            # Write to JSON
            with open(f'{employee_id}.json', mode='w') as file:
                json.dump(data, file, indent=4)

        except ValueError:
            print("Please provide a valid employee ID.")
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")


if __name__ == "__main__":
    main()
