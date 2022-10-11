from flask import Flask, render_template, request, redirect
from flask import Blueprint
from datetime import datetime
from models.session import Session
from models.activity import Activity
from models.member import Member
import repositories.session_repository as session_repository
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

session_blueprint = Blueprint("sessions", __name__)


@session_blueprint.route("/sessions/index")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions=sessions)


# GET
# Route to form for making new session
@session_blueprint.route("/sessions/new", methods=["GET"])
def new_session():
    return render_template("sessions/new.html")


# Create a New session
@session_blueprint.route("/sessions/index", methods=["POST"])
def create_session():
    pass
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    # activity = 

    

    # How can I get the activity to make a new session
    new_session = Session(start_time, duration, activity)
    session_repository.save(new_session)
    return redirect("/sessions/index")


# Delete a Session
@session_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions/index")
