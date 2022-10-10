from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository

activity_blueprint = Blueprint("activity", __name__)

# Display all activities ------------------------------------
@activity_blueprint.route("/activities/index")
def activity():
    activities = activity_repository.select_all()
    return render_template("activities/index.html", activities=activities)


# Show form to create new activity --------------------------
@activity_blueprint.route("/activities/new", methods=["GET"])
def new_activity():
    return render_template("/activities/new.html")


# Show activity ---------------------------------------------
@activity_blueprint.route("/activities/<id>", methods=["GET"])
def show(id):
    activity = activity_repository.select(id)
    members = activity_repository.members(activity)
    return render_template("activities/show.html", members=members, activity=activity)


# Create a new activity ------------------------------------
@activity_blueprint.route("/activities/index", methods=["POST"])
def create_activity():
    activity_name = request.form["activity_name"]
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    activity = Activity(activity_name, start_time, duration)
    activity_repository.save(activity)
    return redirect("/activities/index")


# Edit activity ---------------------------------------------------
@activity_blueprint.route("/activities/<id>/edit")
def edit_activity(id):
    activity = activity_repository.select(id)
    return render_template("/activities/edit.html", activity=activity)


# Update activity ------------------------------------------------------
@activity_blueprint.route("/activities/<id>", methods=["POST"])
def update_activity(id):
    activity_name = request.form["activity_name"]
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    activity = Activity(activity_name, start_time, duration, id)
    activity_repository.update(activity)
    return redirect("/activities/index")
