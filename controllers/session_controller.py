from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
from models.activity import Activity
from models.member import Member
import repositories.session_repository as session_repository
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository

session_blueprint = Blueprint("sessions", __name__)


@session_blueprint.route("/sessions/index")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions=sessions)


# Make a new session
@session_blueprint.route("/sessions/new", methods=["GET"])
def new_session():
    members = member_repository.select_all()
    activities = activity_repository.select_all()
    return render_template("sessions/new.html", members=members, activities=activities)


# Create a New session
@session_blueprint.route("/sessions/index", methods=["POST"])
def create_session():
    member_id = request.form["member_id"]
    activity_id = request.form["activity_id"]
    date_of_class = request.form["date_of_class"]
    time_of_class = request.form["time_of_class"]
    duration = request.form["duration"]
    session = Session(member_id, activity_id, date_of_class, time_of_class, duration)
    session_repository.save(session)
    return redirect("/sessions/index")
