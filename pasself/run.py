#!/usr/bin/env python3
import argparse
import os
import json
import random
from lib import bcrypt as b
from tabulate import tabulate


def duplicate(items): 
    unique = [] 
    for item in items: 
        if item not in unique: 
            unique.append(item) 
    return unique


def fourmat(data):
    print("\n")
    if type(data[0][0]) is not int: 
        print (tabulate(data, headers=["Password"]))
    else:
        print (tabulate(data, headers=[ \
            "No", \
            "Username", \
            "Description", \
            "Website", \
            "Created At", \
            "Last Modified"]))
    print("\n")


def izpass(**keywords):
    try:
        key = "{: <32}".format(os.environ['PWSELF_KEY']).encode("utf-8")
	    #  -- b.decrypt_file('.credential/to_enc.txt.enc', key)
        #  -- b.encrypt_file('to_enc.txt', key)
    except Exception as e:
    	print("[FM02-00] missing_system_environment", e)
        
    with open(".credential/to_enc.txt") as js:
        json_data = json.loads(js.read())
        res_show = []
        res_pass = []
        num = 1
        for arg in sorted(keywords.keys()):
            #print("hihi", arg)
            #print(keywords[arg])
            if keywords[arg]:
                if arg == 'all':
                    for i in json_data:
                    	for j in "username", "description", "website":
                            if keywords[arg] in i[j]:
                                res_show.append([ \
                                    num, \
                                    i['username'], \
                                    i['description'], \
                                    i['website'], \
                                    i['created_at'], \
                                    i['last_modified']])
                                res_pass.append([ \
                                    num, \
                                    i['password']])
                                num += 1
                else:
                    for i in json_data:
                        print(i[arg])
                        if keywords[arg] in i[arg]:
                            res_show.append([ \
                                num, \
                                i['username'], \
                                i['description'], \
                                i['website'], \
                                i['created_at'], \
                                i['last_modified']])
                            res_pass.append([ \
                                num, \
                                i['password']])
                            num += 1
                fourmat(duplicate(res_show))


        try:
            variable = int(input("{} which_user_comma_you_wanna_get_password_question ".format(chr(127800))))
            for i in res_show:
                for k, v in dict(res_pass).items():
                    if i[0] == variable and k == variable:
                        fourmat([["{} {}".format(chr(random.randint(127800, 127900)), v)]])
        except ValueError as e:
            print("[FM02-01] wrong_type_input", e)


            '''
            if keywords[arg]:
                for i in json_data:
                    print(i[arg])
                    if keywords[arg] in i[arg]:
                        res_show.append([ \
                            num, \
                            i['username'], \
                            i['description'], \
                            i['website'], \
                            i['created_at'], \
                            i['last_modified']])
                        res_pass.append([ \
                        	num, \
                        	i['password']])
                        num += 1
                fourmat(res_show)

        try:
            variable = int(input("{} which_user_comma_you_wanna_get_password_question ".format(chr(127800))))
            for i in res_show:
                for k, v in dict(res_pass).items():
                    if i[0] == variable and k == variable:
                        fourmat([["{} {}".format(chr(random.randint(127800, 127900)), v)]])
        except ValueError as e:
            print("[FM02-01] wrong_type_input", e)
            '''

def main():
    parser = argparse.ArgumentParser(description='password for human beings')
    parser.add_argument('-a', '--all', help='filter all fields',required=False)
    parser.add_argument('-d', '--description', help='filter on field[`description`]',required=False)
    parser.add_argument('-u', '--username', help='filter on field[`username`]', required=False)
    parser.add_argument('-w', '--website', help='filter on field[`website`]', required=False)
    args = parser.parse_args()

    izpass(all=args.all, description=args.description, username=args.username, website=args.website)


if __name__ == "__main__":
    main()
