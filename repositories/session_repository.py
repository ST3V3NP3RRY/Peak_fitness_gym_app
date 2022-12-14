from db.run_sql import run_sql
from models.member import Member
from models.session import Session
from models.activity import Activity
import repositories.activity_repository as activity_repository


def save(session):
    sql = """INSERT INTO sessions ( time, duration, activity_id ) 
    VALUES ( %s, %s, %s ) RETURNING id
    """
    values = [
        session.time,
        session.duration,
        session.activity.id,
    ]
    results = run_sql(sql, values)
    session.id = results[0]["id"]
    return session


# def select_all():
def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)

    for row in results:
        activity = activity_repository.select(row["activity_id"])
        session = Session(row["time"], row["duration"], activity, row["id"])
        sessions.append(session)
    return sessions


# Select(id)
def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        activity = activity_repository.select(
            result["activity_id"]
        )  # Here is the problem I think
        session = Session(result["time"], result["duration"], activity, result["id"])
    return session


def activity(session):
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [session.activity.id]
    results = run_sql(sql, values)[0]
    activity = Activity(results["name"], results["id"])
    return activity


# NEEDS REFACTORED
# Activity Session
def members(session):

    sql = "SELECT * FROM members WHERE id = %s"
    values = [session.member.id]
    result = run_sql(sql, values)[0]
    member = Member(result["name"], result["age"], result["address"], result["id"])
    return member


def session_members(session):
    session_members = []

    sql = """
    SELECT members.* FROM members
    INNER JOIN bookings
    ON bookings.member_id = members.id
    WHERE session_id = %s
    """
    values = [session.id]
    results = run_sql(sql, values)
    for row in results:
        member = Member(row["name"], row["age"], row["address"])
        session_members.append(member)
    return session_members


def update(session):
    sql = """UPDATE sessions 
    SET ( time, duration, activity_id ) = ( %s, %s, %s ) WHERE id = %s
    """
    values = [session.time, session.duration, session.activity.id, session.id]
    run_sql(sql, values)


# # Update member
# def update(member):
#     sql = """UPDATE members
#     SET ( name, age, address ) = ( %s, %s, %s ) WHERE id = %s
#     """
#     values = [member.name, member.age, member.address, member.id]
#     run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)
