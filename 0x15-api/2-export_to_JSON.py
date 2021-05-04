#!/usr/bin/python3
""" Using a rest api return information about the id passed as argument """
if __name__ == "__main__":
    import requests
    from sys import argv
    import json
    html = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()
    employee_name = html['username']
    html = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    with open(argv[1] + ".json", "w+") as file:
        json.dump(html, file)
