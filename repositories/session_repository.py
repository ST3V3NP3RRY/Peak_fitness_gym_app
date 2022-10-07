from db.run_sql import run_sql

from models.session import Session
from models.activity import Activity
from models.member import Member
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository


def save(session):
    sql = """INSERT INTO sessions ( member_id, activity_id, date, time, duration ) 
    VALUES ( %s, %s, %s, %s, %s ) RETURNING id
    """
    values = [
        session.member.id,
        session.activity.id,
        session.date,
        session.time,
        session.duration,
    ]
    results = run_sql(sql, values)
    session.id = results[0]["id"]
    return session


# def select_all():


# def activity(session):


# def member(session):


def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)
