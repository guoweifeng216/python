#!/usr/bin/env python
# coding=utf-8
"""
author:     weifeng.guo 
data:       2019/8/22 16:16
filename:   database
"""
import sys, shelve

def store_person(db):
    """
    input data store to db
    :param db:
    :return:
    """
    person_id = input("Enter unique ID number: ")
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input("Enter age: ")
    person['phone'] = input("Enter phone number: ")
    db[person_id] = person


def lookup_person(db):
    """
    enter person id ,then look person information in db
    :param db:
    :return:
    """
    person_id = input("Enter person ID number: ")
    field = input("what would you like to know?(name.age,phone,all)")
    field = field.strip().lower()
    if field == 'all':
        for key, value in db[person_id].items():
            print(key.capitalize() + ':', value)
    else:
        print(field.capitalize() + ':', db[person_id][field])


def print_help():
    print("The available commands are: ")
    print("store: Stores information about a person")
    print("lookup: Looks up a person from ID number")
    print("quit: Save changes and exit")
    print("?: Print this message")


def enter_command():
    cmd = input("Enter command (? for help):")
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('test.txt')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()


if __name__ == '__main__':
    main()
