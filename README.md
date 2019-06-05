# `euler` - project euler

## what-is-it-?
That depends on your background. There are two tables containing problems. The Recent problems table lists the ten most recently published problems, so if you are new to Project Euler then you may prefer to start with the Archives to get a feel for the different types/difficulties of our problems. The first one-hundred or so problems are generally considered to be easier than the problems which follow. In the archives table you will be able to see how many people have solved each problem; as a general rule of thumb the more people that have solved it, the easier it is. To assist further there is a difficulty rating system which may also help you decide where to start. You are able to sort the problems in the archives table on ID, Solved By, or Difficulty.

## my-currrent-state
![alt text](https://projecteuler.net/profile/tin.tran.png "tin-euler")



# `pasself` - password for my self

## what-is-it-?
hope this tool will help my life easier and save my memory
  - store credentials binary and filter
  
#### version-01:
  - initial tool with structure data format
```sh
[
  {
    "username": "foo_username",
    "password": "foo_password",
    "website": "http://foo.com",
    "description": "this is account to login foo.com",
    "created_at": "YYYY-MM-DD:HH-MM-SS",
    "last_modified": "YYYY-MM-DD:HH-MM-SS"
  },
  {
    "username": "bar_username",
    "password": "bar_password",
    "website": "http://bar.com",
    "description": "this is account to login bar.com",
    "created_at": "YYYY-MM-DD:HH-MM-SS",
    "last_modified": "YYYY-MM-DD:HH-MM-SS"
  }
]
```
  - crypto and filter basic function
```sh
  [1] $0 -u|--username foo
  [2] $0 -d|--description foo 
  [3] $0 -w|--website foo
  [4] $0 -a | --all foo
``` 

#### version-02:
  - add/update/delete credential function
  - not show plaint text password on console, get the password via email
  - refactor, flake8 scripts

## url-reference
  - [python-pycrypto-encrypt-decrypt-text-files-with-aes]
  - [python-base64-data-decode]
  - [python-print-pretty-table-list]

## pip-packages
| name | use-for |
| ------ | ------ |
| argparse | parser for command-line options, arguments and sub-commands |
| os | miscellaneous operating system interfaces |
| json | JSON encoder and decoder |
| tabulate | pretty-print tabular data in Python, a library and a command-line utility |

## license
MIT
**Free Software, Hell Yeah!**

  [python-pycrypto-encrypt-decrypt-text-files-with-aes]:  <https://stackoverflow.com/questions/20852664/python-pycrypto-encrypt-decrypt-text-files-with-aes>
  [python-base64-data-decode]: <https://stackoverflow.com/questions/3470546/python-base64-data-decode>
  [python-print-pretty-table-list]: <https://blog.softhints.com/python-print-pretty-table-list/>
