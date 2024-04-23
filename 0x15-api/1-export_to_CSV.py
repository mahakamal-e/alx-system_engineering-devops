#!/usr/bin/python3
"""
Using REST API, for a given employee ID,
returns information about his/her TODO list progress.
and exports it to a CSV file
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    employee_name = requests.get("{}users/{}".format(url, employee_id)).json()
    employee_todos = requests.get(
            "{}todos?userId={}".format(url, employee_id)
    ).json()

    csv_data = []

    for todo in employee_todos:
        csv_data.append({
            "USER_ID": employee_id,
            "USERNAME": employee_name.get("username"),
            "TASK_COMPLETED_STATUS": todo.get("completed"),
            "TASK_TITLE": todo.get("title")
        })
    with open("{}.csv".format(employee_id), 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_data[0].keys(),
                                quoting=csv.QUOTE_ALL)

        writer.writerows(csv_data)
