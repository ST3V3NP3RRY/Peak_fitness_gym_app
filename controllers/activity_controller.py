from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository

activity_blueprint = Blueprint("activity", __name__)


@activity_blueprint.route("/activities/index")
def activity():
    activities = activity_repository.select_all()
    return render_template("activities/index.html", activities=activities)
