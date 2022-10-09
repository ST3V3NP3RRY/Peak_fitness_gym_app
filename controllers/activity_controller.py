from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository

activity_blueprint = Blueprint("activity", __name__)


@activity_blueprint.route("/activities/index")
def activity():
    activities = activity_repository.select_all()
    return render_template("activities/index.html", activities=activities)


@activity_blueprint.route("/activities/new", methods=["GET"])
def new_activity():
    return render_template("/activities/new.html")


# make a new exercise activity
@activity_blueprint.route("/activities/index", methods=["POST"])
def create_activity():
    activity_name = request.form["activity_name"]
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    activity = Activity(activity_name, start_time, duration)
    activity_repository.save(activity)
    return redirect("/activities/index")
