from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member

# Save
def save(activity):
    sql = """
    INSERT INTO activities ( name, start_time, duration )
    VALUES ( %s, %s, %s ) RETURNING id
    """
    values = [activity.name, activity.start_time, activity.duration]
    results = run_sql(sql, values)
    activity.id = results[0]["id"]
    return activity


# Select_all
def select_all():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for row in results:
        activity = Activity(row["name"], row["start_time"], row["duration"], row["id"])
        activities.append(activity)
    return activities


# Select(id)
def select(id):
    activity = None
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        activity = Activity(
            result["name"], result["start_time"], result["duration"], result["id"]
        )
    return activity


# def members(location):
def members(activity):
    members = []

    sql = """
    SELECT members.* FROM members 
    INNER JOIN sessions 
    ON sessions.member_id = members.id 
    WHERE activity_id = %s
    """
    values = [activity.id]
    results = run_sql(sql, values)

    for row in results:

        member = Member(row["name"], row["age"], row["address"], row["id"])
        members.append(member)

    return members


def update(activity):
    sql = """
    UPDATE activities SET (name, start_time, duration ) = ( %s, %s, %s ) WHERE id = %s
    """
    values = [activity.name, activity.start_time, activity.duration, activity.id]

    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)
