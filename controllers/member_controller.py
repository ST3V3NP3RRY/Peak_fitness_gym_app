from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

member_blueprint = Blueprint("members", __name__)

# Display all members
@member_blueprint.route("/members/index")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)


# Show form to create new member
@member_blueprint.route("/members/new", methods=["GET"])
def new_member():
    return render_template("/members/new.html")


# Show member ------------------------------------------
@member_blueprint.route("/members/<id>", methods=["GET"])
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


# Edit member
@member_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("/members/edit.html", member=member)


# Update member
@member_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    member_name = request.form["member_name"]
    age = request.form["age"]
    address = request.form["address"]
    member = Member(member_name, age, address, id)
    member_repository.update(member)
    return redirect("/members/index")
