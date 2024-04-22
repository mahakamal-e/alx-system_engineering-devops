#!/usr/bin/python3
""" using this REST API, for a given employee ID """
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee_name = requests.get(f"{url}users/{employee_id}").json()
    employee_todo = requests.get(f"{url}todos?userId={employee_id}").json()

    completed_tasks = 0

    for task in employee_todo:
        if task['completed']:
            completed_tasks += 1

    print(f"Employee {employee_name['name']} is done with tasks "
          f"({completed_tasks}/{len(employee_todo)}):")
    for task in employee_todo:
        if task['completed']:
            print(f"\t{task['title']}")
