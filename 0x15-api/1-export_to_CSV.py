#!/usr/bin/python3
"""
Using REST API, for a given employee ID,
returns information about his/her TODO list
and exports it to a CSV file
"""
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    employee_name = requests.get(f"{url}users/{employee_id}").json()
    employee_todo = requests.get(f"{url}todos?userId={employee_id}").json()

    filename = f"{employee_id}.csv"

    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["USER_ID", "USERNAME",
                            "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in employee_todo:
            task_id = task['id']
            task_title = task['title']
            task_completed = task['completed']

            csvwriter.writerow([employee_id, employee_name.get('name'),
                               task_completed, task_title])

    print(f"Exported TODO list for Employee {employee_name.get('name')}" \
          f"to {filename}")

