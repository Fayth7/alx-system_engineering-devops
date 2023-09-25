#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
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

    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(completed_tasks), total_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
