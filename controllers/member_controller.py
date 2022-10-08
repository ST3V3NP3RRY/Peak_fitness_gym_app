from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

member_blueprint = Blueprint("members", __name__)


@member_blueprint.route("/members/index")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)


@member_blueprint.route("/members/new", methods=["GET"])
def new_member():
    return render_template("/members/new.html")


# Show user
@member_blueprint.route("/members/<id>")
def show(id):
    members = member_repository.select(id)
    activities = member_repository.activities(members)
    return render_template("members/show.html", members=members, activities=activities)


# Create a new Member
@member_blueprint.route("/members/index", methods=["POST"])
def create_member():
    member_name = request.form["member_name"]
    age = request.form["age"]
    address = request.form["address"]
    new_member = Member(member_name, age, address)
    member_repository.save(new_member)
    return redirect("/members/index")
