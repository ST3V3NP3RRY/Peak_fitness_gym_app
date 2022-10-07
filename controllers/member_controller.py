from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

member_blueprint = Blueprint("members", __name__)


@member_blueprint.route("/members/index")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)
