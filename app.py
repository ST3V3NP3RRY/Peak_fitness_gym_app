from flask import Flask, render_template
from datetime import datetime
import time
from controllers.member_controller import member_blueprint
from controllers.activity_controller import activity_blueprint
from controllers.session_controller import session_blueprint
from controllers.booking_controller import booking_blueprint

app = Flask(__name__)

app.register_blueprint(member_blueprint)
app.register_blueprint(activity_blueprint)
app.register_blueprint(session_blueprint)
app.register_blueprint(booking_blueprint)

now = datetime.now()
date = now.strftime("%A, %d %B %Y")

current_time = time.strftime("%H:%M")


@app.route("/")
def home():
    return render_template("index.html", date=date, current_time=current_time)


if __name__ == "__main__":
    app.run(debug=True)
