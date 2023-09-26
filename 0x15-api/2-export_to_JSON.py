#!/usr/bin/python3
"""Returns to-do list and exports it in JSON format for a given employee ID."""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(f"{base_url}users/{employee_id}").json()
    todos = requests.get(f"{base_url}todos", params={
                         "userId": employee_id}).json()

    todo_list = []

    for task in todos:
        task_info = {
            "task": task["title"],
            "completed": task["completed"],
            "username": user["username"]
        }
        todo_list.append(task_info)

    return user["id"], todo_list


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_id, todo_list = get_employee_todo_progress(employee_id)

    if not user_id:
        print(f"No employee found with ID {employee_id}")
    else:
        json_data = {str(user_id): todo_list}
        with open(f"{user_id}.json", "w") as json_file:
            json.dump(json_data, json_file)

        print(f"Data exported to {user_id}.json successfully.")
