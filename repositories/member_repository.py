from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member

# Save single member into database table members
def save(member):
    sql = "INSERT INTO members ( name ) VALUES ( %s) RETURNING id"
    values = [member.name]
    results = run_sql(sql, values)
    member.id = results[0]["id"]
    return member


# Select_all


# Select(id)


# Delete all


# Acivity(member)
