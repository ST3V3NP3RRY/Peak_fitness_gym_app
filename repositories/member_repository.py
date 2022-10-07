from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member

# Save single member into database table members
def save(member):
    sql = "INSERT INTO members ( name ) VALUES ( %s ) RETURNING id"
    values = [member.name]
    results = run_sql(sql, values)
    member.id = results[0]["id"]
    return member


# Select_all
def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row["name"], row["id"])
        members.append(member)
    return member


# Select(id)
def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result["name"], result["id"])
    return member


# Delete all
def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


# Activity(member)
def activity(member):
    members = []

    sql = """
    SELECT members.* FROM members 
    INNER JOIN sessions 
    ON activities.member_id = members.id
    WHERE activity_id = %s
    """
    values = [member.id]
    results = run_sql(sql, values)
    for row in results:
        member = Member(row["name"], row["id"])
        members.append(member)
    return member
