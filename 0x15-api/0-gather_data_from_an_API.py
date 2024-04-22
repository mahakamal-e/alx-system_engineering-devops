#!/usr/bin/python3
""" returns information about
emplyee todo list
using emplyee id
using REST API
"""

import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    emplyee_todo = requests.get(f"{url}/users/{sys.argv[1]}/todos")
    emplyee_name = requests.get(f"{url}/users/{sys.argv[1]}")

    emplyee_todo = emplyee_todo.json()
    emplyee_name = emplyee_name.json()['name']

    completed_tasks = 0

    for task in emplyee_todo:
        if task['completed']:
            completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(emplyee_name, completed_tasks, len(emplyee_todo)))

    for line in emplyee_todo:
        if line['completed']:
            print(f"\t {line['title']}")
