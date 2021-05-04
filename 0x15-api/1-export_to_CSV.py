#!/usr/bin/python3
""" Using a rest api return information about the id passed as argument """
if __name__ == "__main__":
    import requests
    from sys import argv
    html = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()
    employee_name = html['name']
    html = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    csv = ""
    for dic in html:
        if dic['userId'] == int(argv[1]):
            csv += '"{}","{}","{}","{}"\n'.format(
                dic['userId'], employee_name, dic['completed'], dic['title'])

    with open(argv[1] + ".csv", "w+") as file:
        file.write(csv)
