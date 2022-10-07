from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member

# Save
def save(activity):
    sql = """
    INSERT INTO activities ( name, title )
    VALUES ( %s, %s ) RETURNING id
    """
    values = [activity.name, activity.title]
    results = run_sql(sql, values)
    activity.id = results[0]["id"]
    return activity


# Select_all


# Select(id)


# def members(location):


def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)
