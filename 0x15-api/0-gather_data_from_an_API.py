#!/usr/bin/python3
''' Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress '''

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 0:
        completed_tasks = []
        user_res = requests.get(
                "https://jsonplaceholder.typicode.com/users/{}".
                format(sys.argv[1]), verify=False).json()
        TODO_res = requests.get(
                "https://jsonplaceholder.typicode.com/todos?userId={}".
                format(sys.argv[1]), verify=False).json()
        for tasks in TODO_res:
            if tasks.get('completed') is True:
                completed_tasks.append(tasks.get('title'))
        print("Employee {} is done with tasks({}/{}):".
              format(user_res.get(
                  'name'), len(completed_tasks), len(TODO_res)))
        for com in completed_tasks:
            print("\t {}".format(com))
