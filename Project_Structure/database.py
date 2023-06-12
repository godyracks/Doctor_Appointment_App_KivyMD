import mysql.connector
from kivymd.uix.snackbar import Snackbar
from mysql.connector import connect

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="godygaro66",
    database="doctorapp",
    port=3307
)
c = conn.cursor()

# Creating the appointments table if it doesn't exist
c.execute("""CREATE TABLE IF NOT EXISTS appointments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT,
                gender VARCHAR(10),
                location VARCHAR(255),
                scheduled_time VARCHAR(255),
                phone VARCHAR(255)
            )""")
conn.commit()

def create_appointment(name, age, gender, location, scheduled_time, phone):
    # Add the appointment to the database
    sql = "INSERT INTO appointments (name, age, gender, location, scheduled_time, phone) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, age, gender, location, scheduled_time, phone)
    c.execute(sql, val)
    conn.commit()
    return c.lastrowid

def get_appointments():
    # Retrieve all the appointments from the database
    c.execute("SELECT * FROM appointments")
    return c.fetchall()

def delete_appointment(name, scheduled_time):
    # Delete an appointment from the database
    # Find the appointment in the database
    sql = "SELECT * FROM appointments WHERE name = %s AND scheduled_time = %s"
    val = (name, scheduled_time)
    c.execute(sql, val)
    result = c.fetchone()

    if result:
        # Delete the appointment from the database
        sql = "DELETE FROM appointments WHERE id = %s"
        val = (result[0],)
        c.execute(sql, val)
        conn.commit()
        conn.close()
    else:
        Snackbar(text="Appointment not found").open()

#def insert_user(name, email, password):
    #conn = connect()
    #cursor = conn.cursor()
   # cursor.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (name, email, password))
    #conn.commit()
    #cursor.close()
    #conn.close()

