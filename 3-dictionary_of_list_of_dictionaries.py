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

    employee_name = requests.get("{}users".format(url)).json()
    employee_todos = requests.get("{}todos".format(url)).json()
    data_json = {}
    for user in employee_name:
        tasks = []
        for task in employee_todos:
            if task.get('userId') == user.get('id'):
                tasks_dict = {"username": user.get('username'),
                              "task": task.get('title'),
                              "completed": task.get('completed')}
                tasks.append(tasks_dict)

        data_json[user.get('id')] = tasks
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(data_json, f)
