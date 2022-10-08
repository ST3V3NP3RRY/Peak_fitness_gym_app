from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
from models.activity import Activity
from models.member import Member
import repositories.session_repository as session_repository

session_blueprint = Blueprint("sessions", __name__)


@session_blueprint.route("/sessions/index")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions=sessions)
