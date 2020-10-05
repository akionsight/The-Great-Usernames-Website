my entry for the 1st Timathon challenge
# great-usernames
A cool Username generator + sqlite3 database for storing them + repetition protection

## Features
Username generator
sqlite3 db for storage of usernames
repetition protection

## Usage
1. Clone the repository

2.import the main.py file from the src folder
```python
from src/main import *
```
3. Paste this code 
```python
username = generate_username()
print(insert_username(username))
```
If the terminal prints `True` then you know that the username has been inserted.




