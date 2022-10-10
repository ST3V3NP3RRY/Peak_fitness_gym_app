from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member

# Save single member into database table members
def save(member):
    sql = (
        "INSERT INTO members ( name, age, address ) VALUES ( %s, %s, %s ) RETURNING id"
    )
    values = [member.name, member.age, member.address]
    results = run_sql(sql, values)
    member.id = results[0]["id"]
    return member


# Select_all
def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row["name"], row["age"], row["address"], row["id"])
        members.append(member)
    return members


# Select(id)
def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result["name"], result["age"], result["address"], result["id"])
    return member


# Delete all
def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


# Update member
def update(member):
    sql = """UPDATE members 
    SET ( name, age, address ) = ( %s, %s, %s ) WHERE id = %s
    """
    values = [member.name, member.age, member.address, member.id]
    run_sql(sql, values)


# Activity(member)
def activities(member):
    activities = []

    sql = """
    SELECT activities.* FROM activities 
    INNER JOIN sessions 
    ON sessions.activity_id = activities.id WHERE member_id = %s
    """
    values = [member.id]
    results = run_sql(sql, values)
    for row in results:
        activity = Activity(row["name"], row["start_time"], row["duration"], row["id"])
        activities.append(activity)
    return activities
