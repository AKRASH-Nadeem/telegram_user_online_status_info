# Telegram bot for saving online status of users

## Install requirements

### python3 => 3.9

```
pip install -r requirements.txt
```

**login** and get your _**pyrogram**_ session and store it in the **config.py** file

### **config.py**

```
session_string = "pyrogram_session"
```

### **users.txt**

```
username1
username2
username3
```

## Start the bot

```
python3 main.py
```

## Usage instruction

1. go to your save messages and see if you got any started message
2. send a command **/getusers**,you will get a message that says "done getting users"
3. send a command **/ready** the bot will be ready to go
