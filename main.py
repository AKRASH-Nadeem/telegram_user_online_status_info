"""
This bot is made by AKRASH NADEEM
fiverr : https://www.fiverr.com/users/akrash_nadeem
"""
from config import session_string
from pyrogram import Client, filters,idle
from pyrogram.enums import UserStatus
import sqlite3
import datetime


con = sqlite3.connect("usersinfo.db")

con.row_factory = lambda cursor, row: row[0]

c = con.cursor()

app = Client("my_account", session_string=session_string)

users = []


@app.on_user_status(UserStatus.ONLINE)
async def getit(client, status):
    e = datetime.datetime.now()
    if status.status == UserStatus.ONLINE and status.id in users:
        print(status.status)
        userid = int(status.id)
        us = await client.get_users(userid)
        t = us.username + " " + str(status.status) + " %s" % e + "\n"
        with open("info.txt", "a") as file:
            file.write(t)


@app.on_message(filters.me & filters.private & filters.command(['getusers']))
async def getusers(client, status):
    with open("users.txt", "r") as f:
        data = f.read().splitlines()
        try:
            u = await app.get_users(data)
            for user in u:
                if user.username:
                    try:
                        con.execute("INSERT OR IGNORE INTO users(username,userid) VALUES(?,?)", [
                                    user.username, int(user.id)])
                    except Exception as error:
                        print(error)
                else:
                    try:
                        con.execute(
                            "INSERT OR IGNORE INTO users(userid) VALUES(?)", [int(user.id)])
                    except Exception as error:
                        print(error)
            con.commit()
            await app.send_message("me", "done getting the users")
        except Exception as error:
            print(error)


@app.on_message(filters.me & filters.private & filters.command(['ready']))
async def getdata(client, message):
    global users
    users = c.execute("SELECT userid FROM users").fetchall()
    await client.send_message("me", "now it is ready")


if __name__ == "__main__":
    app.start()
    app.send_message("me", "started")
    print("[*] status bot started...")
    idle()
    app.stop()
