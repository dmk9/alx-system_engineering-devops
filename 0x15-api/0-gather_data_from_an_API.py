#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

# The API's URL
API_URL = 'https://jsonplaceholder.typicode.com'

# Check if the script is being run directly
if __name__ == '__main__':
    # Check if command line arguments were provided
    if len(sys.argv) > 1:
        try:
            # Get the employee ID from command line arguments
            employee_id = int(sys.argv[1])

            # Get the user's information from the API
            user_res = requests.get(f'{API_URL}/users/{employee_id}').json()
            todos_res = requests.get(f'{API_URL}/todos').json()
            user_name = user_res.get('name')

            # Filter todos for the given user
            todos = [
                todo for todo in todos_res
                if todo.get('userId') == employee_id
            ]
            todos_done = [todo for todo in todos if todo.get('completed')]

            # Print the user's tasks
            print(
                f"Employee {user_name} is done with tasks"
                f"({len(todos_done)}/{len(todos)}): ")
            for todo in todos_done:
                print(f"\t {todo.get('title')}")
        except ValueError:
            print("Please provide a valid employee ID.")
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
