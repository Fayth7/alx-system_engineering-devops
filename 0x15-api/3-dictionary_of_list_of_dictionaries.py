#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 3-dictionary_of_list_of_dictionaries.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get the user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    username = user_data["username"]

    # Get the tasks for the user
    tasks_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    tasks_data = tasks_response.json()

    # Create a dictionary to store the tasks
    task_dict = {employee_id: []}

    # Iterate through the tasks and add them to the dictionary
    for task in tasks_data:
        task_dict[employee_id].append({
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        })

    # Output the data to a JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w") as json_file:
        json.dump(task_dict, json_file, indent=4)

    print(f"Data exported to {filename}")
