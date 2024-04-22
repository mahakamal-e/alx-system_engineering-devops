#!/usr/bin/python3
"""
 Using REST API, for a given employee ID,
 returns information about his/her TODO list
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    employee_name = requests.get(f"{url}users/{employee_id}").json()
    employee_todo = requests.get(f"{url}todos?userId={employee_id}").json()

    completed_tasks = 0

    for task in employee_todo:
        if task['completed']:
            completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name.get('name'), completed_tasks,
                  len(employee_todo)))

    for task in employee_todo:
        if task['completed']:
            print(f"\t {task['title']}")
