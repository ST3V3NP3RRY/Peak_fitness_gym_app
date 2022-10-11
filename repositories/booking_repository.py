import sqlite3
from db.run_sql import run_sql

from models.booking import Booking
from models.member import Member
from models.activity import Activity
from models.session import Session
import repositories.activity_repository as activity_repository
import repositories.session_repository as session_repository
import repositories.member_repository as member_repository

# SAVE
def save(booking):
    sql = """
        INSERT INTO bookings ( member_id, session_id )
        VALUES ( %s, %s ) RETURNING id
    """
    values = [booking.member.id, booking.session.id]
    result = run_sql(sql, values)
    booking.id = result[0]["id"]
    return booking


# Select all bookings
def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row["member_id"])
        session = session_repository.select(row["session_id"])
        booking = Booking(member, session)
        bookings.append(booking)
    return bookings


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)
