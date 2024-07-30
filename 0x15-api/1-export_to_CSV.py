#!/usr/bin/python3
'''
A Python script that, using this REST API, for a given employee ID,
exports all information on tasks for selected 
employee in the CSV format.
'''

import requests
import sys
import csv

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

            # Write to CSV
            with open(f'{employee_id}.csv', mode='w', newline='') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                for todo in todos:
                    writer.writerow(
                        [employee_id, user_name,
                         todo.get('completed'), todo.get('title')])

        except ValueError:
            print("Please provide a valid employee ID.")
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")


if __name__ == "__main__":
    main()
