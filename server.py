from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = user.get_all()
    print(users)
    return render_template("create.html")



            
if __name__ == "__main__":
    app.run(debug=True)