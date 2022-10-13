from flask import Flask, render_template, request, redirect
from flask import Blueprint
from datetime import datetime
from models.session import Session
from models.activity import Activity
from models.member import Member
from models.booking import Booking
import repositories.session_repository as session_repository
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

booking_blueprint = Blueprint("bookings", __name__)


@booking_blueprint.route("/bookings/index")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)


@booking_blueprint.route("/bookings/new")
def new_booking():
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("bookings/new.html", members=members, sessions=sessions)


@booking_blueprint.route("/bookings/index", methods=["POST"])
def create_new_booking():

    member = member_repository.select(request.form["member_id"])
    session = session_repository.select(request.form["session_id"])

    booking = Booking(member, session)
    booking_repository.save(booking)

    return redirect("/bookings/index")
