#!/usr/bin/env python3
import argparse
import os
import json
from lib import bcrypt as b
from tabulate import tabulate


def fourmat(data):
    print (tabulate(data, headers=[ \
        "Username", \
        "Description", \
        "Website", \
        "Created At", \
        "Last Modified"]))


def izpass(**keywords):
    try:
	    key = "{: <32}".format(os.environ['PWSELF_KEY']).encode("utf-8")
	    #  -- b.decrypt_file('.credential/to_enc.txt.enc', key)
        #  -- b.encrypt_file('to_enc.txt', key)
    except Exception as e:
    	print("[FM02-00] missing system environment", e)

    with open(".credential/to_enc.txt") as js: 
        json_data = json.loads(js.read())
        
        result = []
        for arg in sorted(keywords.keys()):
            if keywords[arg]:  
                for i in json_data:
                    if keywords[arg] in i[arg]:
                       result.append([ \
                           i['username'], \
                           i['description'], \
                           i['website'], \
                           i['created_at'], \
                           i['last_modified']])
                       #print(result)
                fourmat(result)


def main():
    parser = argparse.ArgumentParser(description='password for human beings')
    parser.add_argument('-a', '--all', help='filter all fields',required=False)
    parser.add_argument('-d', '--description', help='filter on field[`description`]',required=False)
    parser.add_argument('-u', '--username', help='filter on field[`username`]', required=False)
    parser.add_argument('-w', '--website', help='filter on field[`website`]', required=False)
    args = parser.parse_args()

    izpass(a=args.all, description=args.description, username=args.username, website=args.website)


if __name__ == "__main__":
    main()