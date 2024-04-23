#!/usr/bin/python3
"""
Using REST API, for a given employee ID,
returns information about his/her TODO list progress.
and exports it to a json dict.
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    employee_name = requests.get("{}users/{}".format(url, employee_id)).json()
    employee_todos = requests.get(
            "{}todos?userId={}".format(url, employee_id)
    ).json()
    total_tasks = []
    updated_user = {}

    for task in employee_todos:
        total_tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name.get("username"),
        })

    updated_user[employee_id] = total_tasks

    with open("{}.json".format(employee_id), 'w') as file:
        json.dump(updated_user, file)
