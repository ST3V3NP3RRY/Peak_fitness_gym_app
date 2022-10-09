from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository

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


# Show activity
@activity_blueprint.route("/activities/<id>", methods=["GET"])
def show(id):
    activities = activity_repository.select(id)
    members = activity_repository.members(activities)
    return render_template(
        "/activities/show.html", members=members, activities=activities
    )


# Redirect to edit page to update activity
@activity_blueprint.route("/activities/edit", methods=["GET"])
def edit_activity():
    activities = activity_repository.select_all()
    return render_template("/activities/edit.html", activities=activities)


# Update activity
@activity_blueprint.route("/activities/<id>", methods=["POST"])
def update_activity(id):
    activity_name = request.form["activity_name"]
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    activity = Activity(activity_name, start_time, duration, id)
    activity_repository.update(activity)
    return redirect("/activities/index")
