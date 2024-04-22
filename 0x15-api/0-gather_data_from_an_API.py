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
    emplyee_todo = requests.get(f"{url}/users/{employee_id}/todos").json()
    emplyee_name = requests.get(f"{url}/todos?userId=/{employee_id}").json()


    completed_tasks = 0

    for task in emplyee_todo:
        if task['completed']:
            completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name_.get('name'), completed_tasks,
                  len(emplyee_todo)))

    for line in emplyee_todo:
        if line['completed']:
            print(f"\t {line['title']}")
