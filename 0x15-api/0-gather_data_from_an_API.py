#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    user_info = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()

    if not user_info:
        print(f"No employee found with ID {employee_id}")
        return

    employee_name = user_info.get("name")

    todo_list = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    ).json()

    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task.get("completed")]

    print(
        f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):"
    )

    for task in completed_tasks:
        print(f"    {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit
