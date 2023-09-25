#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(base_url + f"users/{employee_id}").json()
    todos = requests.get(base_url + "todos",
                         params={"userId": employee_id}).json()

    completed = [task["title"] for task in todos if task["completed"]]

    return user, completed, len(todos)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_info, completed_tasks, total_tasks = get_employee_todo_progress(
        employee_id)

    if not user_info:
        print(f"No employee found with ID {employee_id}")
    else:
        employee_name = user_info.get("name")
        print(
            f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):"
        )
        [print("\t" + c) for c in completed_tasks]
