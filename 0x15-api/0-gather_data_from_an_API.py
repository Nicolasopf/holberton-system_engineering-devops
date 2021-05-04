#!/usr/bin/python3
""" Using a rest api return information about the id passed as argument """
from sys import argv
import requests

html = requests.get(
    "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()
employee_name = html['name']
html = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

tasks_no_completed = 0
title_of_tasks = []

for dic in html:
    if dic['userId'] == int(argv[1]):
        if dic['completed']:
            title_of_tasks.append(dic['title'])
        else:
            tasks_no_completed += 1

print("Employee {} is done with tasks({}/{}):\n\t {}".format(
    employee_name, len(title_of_tasks),
    tasks_no_completed + len(title_of_tasks), "\n\t ".join(title_of_tasks)))
