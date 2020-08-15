import sqlite3
from sqlite3 import Error

DATABASE = './database.sqlite3'


def create_connection():
    """
    Create connection with a database file,
    here DATABASE is the path to the database file
    :return: sqlite.connect() or None
    """
    global DATABASE
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Error:
        return None


def create_people():  # creates the people table
    """
    Parent Table, with each row as an unique person,
    person details are stored here,
    details like:
    Name, age, gender, height, how_we_met, other details
    :return:
    """
    query = '''
    CREATE TABLE IF NOT EXISTS person(person_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL, age INTEGER, height REAL, gender TEXT, HowWeMet TEXT, Other_Details TEXT)'''

    connection = create_connection()  # create an active connection
    cursor = connection.cursor()  # create a cursor for executing queries
    cursor.execute(query)
    connection.commit()  # finalize changes

    connection.close()  # close active connection
    print("Table Created!")


def create_Named_Events():
    """
    We can store named events for each person here, like birthday, marriage anniversary,
    event time, event name, event message, and person associated is the foreign key to the person table,
    this basically related each event with any person (one-many relationship)
    Event status store,whethere event is complete or not
    :return:
    """
    query = """
    CREATE TABLE IF NOT EXISTS NamedEvents(
        EventID INTEGER PRIMARY KEY AUTOINCREMENT,
        EventDateTime_obj TEXT,
        EventName TEXT,
        EventStatus TEXT,
        PersonAssociated INTEGER,
        EventMessage TEXT,
        EventDetails TEXT,
        FOREIGN KEY(PersonAssociated) REFERENCES person(person_ID))
        """
    connection = create_connection()
    cursor_obj = connection.cursor()
    cursor_obj.execute(query)
    connection.commit()

    connection.close()
    print("Events Table Created")


def create_Reminders():
    """
    this are short time span reminders like, for next 1 month or after 2 days,
    stores, person to whom the reminder is associated to,
    stores the date and time of the reminder
    and some message regarding the reminder
    :return:
    """
    connection = create_connection()
    cursor = connection.cursor()
    query = """
        CREATE TABLE IF NOT EXISTS Reminder(
            ReminderID INTEGER PRIMARY KEY AUTOINCREMENT,
            ReminderDateTime_obj TEXT,
            ReminderMessage TEXT,
            ReminderStatus TEXT,
            PersonAssociated INTEGER,
            Reminder_Details TEXT,
            FOREIGN KEY(PersonAssociated) REFERENCES person(person_ID))
    """
    cursor.execute(query)
    connection.commit()

    connection.close()
    print("Reminder Table Created")


create_people()
create_Named_Events()
create_Reminders()
