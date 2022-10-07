from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member


def save(activity):
    sql = """
    INSERT INTO activities ( name, title )
    VALUES ( %s %s ) RETURNING id
    """
    values = [activity.name, activity.title]
    results = run_sql( sql, values )
    activity.id = results[0]['id']
    
