#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(f"{base_url}users/{employee_id}").json()
    todos = requests.get(f"{base_url}todos", params={
                         "userId": employee_id}).json()

    completed = [task["title"] for task in todos if task["completed"]]

    # Correct employee name length and format
    employee_name = user.get("name")[:15]  # Truncate to 15 characters
    employee_name = f"{employee_name:<15}"  # Pad with spaces to 15 characters

    return employee_name, completed, len(todos)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, completed_tasks, total_tasks = get_employee_todo_progress(
        employee_id)

    if not employee_name:
        print(f"No employee found with ID {employee_id}")
    else:
        print(
            f"Employee Name: {employee_name}OK is done with tasks({len(completed_tasks)}/{total_tasks}):"
        )
        [print("\t" + c) for c in completed_tasks]
