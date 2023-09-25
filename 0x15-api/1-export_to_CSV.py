#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_info = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json()

    if not user_info:
        print("No employee found with ID {}".format(employee_id))
        sys.exit(1)

    employee_name = user_info.get("name")

    todo_list = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id)
    ).json()

    if not todo_list:
        print("No tasks found for employee {}".format(employee_name))
        sys.exit(1)

    csv_filename = "{}.csv".format(employee_id)

    with open(csv_filename, mode="w", newline="") as csv_file:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for task in todo_list:
            writer.writerow(
                {
                    "USER_ID": employee_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": str(task.get("completed")),
                    "TASK_TITLE": task.get("title"),
                }
            )

    print("CSV data exported to {}".format(csv_filename))
