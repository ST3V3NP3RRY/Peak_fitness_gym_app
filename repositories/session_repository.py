from db.run_sql import run_sql

from models.session import Session
from models.activity import Activity
from models.member import Member
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository


def save(session):
    sql = """INSERT INTO sessions ( member_id, activity_id, date ) 
    VALUES ( %s, %s, %s ) RETURNING id
    """
    values = [session.member.id, session.activity.id, session.date]
    results = run_sql(sql, values)
    session.id = results[0]["id"]
    return session


# def select_all():
def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row["member_id"])
        activity = activity_repository.select(row["activity_id"])
        session = Session(member, activity, row[("date")], row["id"])
        sessions.append(session)
    return sessions


# def activity(session):
def activity(session):
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [session.activity.id]
    results = run_sql(sql, values)[0]
    activity = Activity(
        results["name"], results["start_time"], results["duration"], results["id"]
    )
    return activity


# def member(session):
def member(session):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [session.member.id]
    results = run_sql(sql, values)[0]
    member = Member(results["name"], results["age"], results["address"], results["id"])
    return member


def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)
