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


@session_blueprint.route("/sessions/new", methods=["GET"])
def new_session():
    members = member_repository.select_all()
    activities = activity_repository.select_all()
    return render_template("sessions/new.html", members=members, activities=activities)
