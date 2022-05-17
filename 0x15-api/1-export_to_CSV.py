#!/usr/bin/python3
''' Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress '''

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 0:
        user_res = requests.get(
                "https://jsonplaceholder.typicode.com/users/{}".
                format(sys.argv[1]), verify=False).json()
        TODO_res = requests.get(
                "https://jsonplaceholder.typicode.com/todos?userId={}".
                format(sys.argv[1]), verify=False).json()
        with open("{}.csv".format(sys.argv[1]), 'w') as csv_file:
            csv_obj_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for com in TODO_res:
                csv_obj_writer.writerow(
                        [int(sys.argv[1]), user_res.get('username'),
                            com.get('completed'), com.get('title')])
