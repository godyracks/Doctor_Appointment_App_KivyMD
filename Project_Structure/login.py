import hashlib

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
import mysql.connector
from kivymd.uix.snackbar import Snackbar
from register import RegisterScreen
from mysql.connector import cursor


Builder.load_file('login.kv')


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # establish connection to database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="godygaro66",
            database="doctorapp",
            port=3307
        )

        # create cursor
        cursor = db.cursor()

    def hash_password(self, password):
        # Hash the password using SHA-256 algorithm
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def authenticate_user(self, email_input, password_input):
        # get email and password input from user
        email = email_input.text.strip()
        password = password_input.text.strip()

        # check if email and password are not blank
        if email and password:
            # establish connection to database
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="godygaro66",
                database="doctorapp",
                port=3307
            )

            # create cursor
            cursor = db.cursor()

            # hash the password
            hashed_password = self.hash_password(password)

            # create query to check if user exists in database
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(query, (email, hashed_password))
            result = cursor.fetchone()

            # check if user exists in database
            if result:
                # user exists in database, change screen to appointment screen
                self.manager.current = 'appointment'
            else:
                # user does not exist in database, show error message
                Snackbar(text="Invalid email or password").open()
        else:
            # email or password input fields are blank, show error message
            Snackbar(text="Email and password cannot be blank").open()

    def on_signup_button_press(self):
        # get the screen manager from the root widget
        screen_manager = self.manager

        # set the current screen to the register screen
        screen_manager.current = 'register'

    def change_screen(self, instance):
        self.manager.current = 'appointment'