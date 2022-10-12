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

booking_blueprint = Blueprint("bookings", __name__)


@booking_blueprint.route("/bookings/index")
def sessions():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)
