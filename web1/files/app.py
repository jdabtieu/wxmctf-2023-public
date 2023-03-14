from flask import *
import os

app = Flask(__name__)

flag = os.getenv('FLAG', 'ctf{flag}')

@app.route("/")
def room1():
    return render_template("room_msg.html", msg="Welcome to the Maze. You are currently in room 1. Click on a door to navigate to another room. The flag is at room 0. Good luck!", n=1)

@app.route("/room/<int:room_id>")
def room(room_id):
    if room_id == 1:
        return room1()
    elif room_id == 0:
        return render_template("room_msg.html", msg=flag, n=0)
    elif room_id > 9000:
        return render_template("room_msg.html", msg="It's greater than 9000!", n=1)
    else:
        return render_template("room_msg.html", n=room_id)

@app.errorhandler(404)
def notfound(e):
    return redirect("/")
