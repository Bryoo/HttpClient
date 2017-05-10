# Word Count Program

This is a simple http web and client program

It contains the get, post and update implementations to a public [JSONPlaceholder API](https://jsonplaceholder.typicode.com/).

It asks the user for input then sends get, post or update requests to api

## Getting Started

Some prerequisites are required to have achieved desired output.

    This code is written in Python3 and may have unexpected functionality when run with Python 2.x

Install pytest:
```
$ pip install pytest

```
Alternatively, Install nose
```
$ pip install nose

```

Additionally, you need to pip install requests
```
$ pip install request

```
### Using the Code

clone the code from git using this limk:
```
git clone https://github.com/Bryoo/HttpClient
```
Ensure you're in the main directory 'HttpClient' and then run the code
```
python3 mainfile.py

## Executing the tests included

if you've got pytest
```
$ py.test test_http_client.py
```
If you've got nosetests
```
$ nosetests test_http_client.py
```
Alternatively, if you do not have either nosetests or pytest installed, use:

```
$ python3 test_http_client.py
```

 The test cases present includes some tests for both edge and general cases:



