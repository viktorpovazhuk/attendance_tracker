# CREATE TABLE attendance (id INT AUTO_INCREMENT PRIMARY KEY, user_id VARCHAR(10), swipe_in DATETIME, swipe_out DATETIME);
# INSERT INTO attendance (user_id, swipe_in, swipe_out) VALUES ('0123456789', '1998-01-23 12:45:56', '1998-01-23 14:45:56');
# SELECT * FROM attendance WHERE DATE(swipe_in) = '1998-01-23';

import mysql.connector
from datetime import datetime

gym_db = mysql.connector.connect(
    host="localhost", user="viktor", password="20032003", database="gym"
)

cursor = gym_db.cursor()


def add_swipe_point(user_id):
    """
    Open attendance session if it is closed. Otherwise, close.
    """
    query_is_closed = (
        "SELECT swipe_out FROM attendance WHERE user_id = %s ORDER BY id DESC LIMIT 1;"
    )
    query_open = (
        "INSERT INTO attendance (user_id, swipe_in, swipe_out) VALUES (%s, %s, NULL);"
    )
    query_close = "UPDATE attendance SET swipe_out = %s WHERE user_id = %s ORDER BY id DESC LIMIT 1;"
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(query_is_closed, (user_id,))
    swipe_out = cursor.fetchone()
    is_closed = swipe_out is None or swipe_out[0] is not None
    if is_closed:
        cursor.execute(query_open, (user_id, date_str))
    else:
        cursor.execute(query_close, (date_str, user_id))
    gym_db.commit()


if __name__ == "__main__":
    add_swipe_point("0123456789")
    # add_swipe_point("1123456789")
