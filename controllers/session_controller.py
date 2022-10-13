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

# Display all sessions
@session_blueprint.route("/sessions/index")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions=sessions)


# GET
# Route to form for making new session
@session_blueprint.route("/sessions/new", methods=["GET"])
def new_session():
    activities = activity_repository.select_all()
    return render_template("sessions/new.html", activities=activities)


# Show session details
@session_blueprint.route("/sessions/<id>", methods=["GET"])
def show_session(id):
    session = session_repository.select(id)
    activity = session_repository.activity(session)
    members = session_repository.session_members(session)
    return render_template(
        "sessions/show.html", session=session, members=members, activity=activity
    )


@session_blueprint.route("/sessions/<id>/edit")
def edit_activity(id):
    activities = activity_repository.select_all()
    session = session_repository.select(id)
    return render_template(
        "/sessions/edit.html", session=session, activities=activities
    )


# Create a New session
@session_blueprint.route("/sessions/index", methods=["POST"])
def create_session():

    start_time = request.form["start_time"]
    duration = request.form["duration"]
    activity = request.form["activity_id"]

    activity_id = activity_repository.select(activity)

    new_session = Session(start_time, duration, activity_id)
    session_repository.save(new_session)
    return redirect("/sessions/index")


# Update session
@session_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    activity = activity_repository.select(request.form["activity_id"])
    time = request.form["time"]
    duration = request.form["duration"]

    session = Session(time, duration, activity, id)

    session_repository.update(session)
    return redirect("/sessions/index")


# Delete a Session
@session_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions/index")
