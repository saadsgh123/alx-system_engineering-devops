#!/usr/bin/python3
"""retreive data from an API"""
import requests, json, sys


def gather_data_from_Emp_API():
    """main function"""
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = "users?id={}".format(id)
    todo = "todos?userId={}".format(id)
    done_todos = "{}&completed=true".format(todo)
    userData = requests.get(f'{url}{user}').json()
    username = userData[0]['name']
    todosData = requests.get(f'{url}{todo}').json()
    todosDone = requests.get(f'{url}{done_todos}').json()
    done_num = len(todosDone)
    all_todo = len(todosData)
    print(f'Employee {username} is done with tasks({done_num}/{all_todo}):')
    for task in todosDone:
        print("\t " + task.get("title"))

if __name__ == '__main__':
    gather_data_from_Emp_API()
