import mysql.connector
from datetime import datetime

gym_db = mysql.connector.connect(
    host="localhost", user="viktor", password="20032003", database="gym"
)

cursor = gym_db.cursor()


def check_visit_status(user_id):
    """
    Returns True if visit was started. Otherwise, False.
    """
    query_is_closed = (
        "SELECT end_time FROM attendance WHERE user_id = %s ORDER BY id DESC LIMIT 1;"
    )
    cursor.execute(query_is_closed, (user_id,))
    swipe_out = cursor.fetchone()
    is_closed = swipe_out is None or swipe_out[0] is not None
    return not is_closed


def add_visit_start_dtime(user_id, dtime):
    """
    Arguments:
        dtime (str|datetime): Date and time in format "%Y-%m-%d %H:%M:%S".
    Returns True at success.
    """
    dtime = str(dtime)
    query_open = (
        "INSERT INTO attendance (user_id, start_time, end_time) VALUES (%s, %s, NULL);"
    )
    cursor.execute(query_open, (user_id, dtime))
    gym_db.commit()


def add_visit_end_dtime(user_id, dtime):
    """
    Arguments:
        dtime (str|datetime): Date and time in format "%Y-%m-%d %H:%M:%S".
    Returns True at success.
    """
    dtime = str(dtime)
    query_close = "UPDATE attendance SET end_time = %s WHERE user_id = %s ORDER BY id DESC LIMIT 1;"
    cursor.execute(query_close, (dtime, user_id))
    gym_db.commit()


def get_last_visits_end_time():
    """
    Returns:
        last_visits (dict[user_id: dtime]): Last visit time for every user.
        Last visit time is None if user is currently in the gym.
    """
    query = """SELECT t1.user_id, t1.end_time
FROM attendance AS t1
LEFT JOIN attendance AS t2
ON t1.user_id = t2.user_id
AND t1.start_time < t2.start_time
WHERE t2.user_id IS NULL;"""
    cursor.execute(query)
    records = cursor.fetchall()
    records = dict(records)
    return records


if __name__ == "__main__":
    user_id = "2123456789"
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not check_visit_status(user_id):
        add_visit_start_dtime(user_id, date_str)
        add_visit_end_dtime(user_id, date_str)
    print(get_last_visits_end_time())
