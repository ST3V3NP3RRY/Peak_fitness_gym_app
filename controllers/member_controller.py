from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

member_blueprint = Blueprint("members", __name__)


@member_blueprint.route("/members/index")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)


@member_blueprint.route("/members/new", methods=["GET"])
def new_member():
    return render_template("/members/new.html")


@member_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    return render_template("members/show.html", member=member)


@member_blueprint.route("/members/index", methods=["POST"])
def create_member():
    member_name = request.form["member_name"]
    age = request.form["age"]
    address = request.form["address"]
    new_member = Member(member_name, age, address)
    member_repository.save(new_member)
    return redirect("/members/index")
