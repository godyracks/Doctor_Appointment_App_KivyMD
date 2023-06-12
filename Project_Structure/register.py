from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.material_resources import dp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import hashlib

import mysql.connector

Builder.load_file('register.kv')

class RegisterScreen(Screen):
    name_input = ObjectProperty()
    email_input = ObjectProperty()
    password_input = ObjectProperty()

    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)

    def submit_form(self, instance):
        # get the user's input
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text

        # hash the password
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # check if all fields are filled in
        if not name or not email or not password:
            self.display_message('Please fill in all fields')
            return

        # connect to the database and insert the new user
        conn = mysql.connector.connect(user='root',
                                       password='godygaro66',
                                       host='localhost',
                                       database='doctorapp',
                                       port=3307)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
        result = cursor.fetchone()
        if result:
            self.display_message('An account with that email already exists')
        else:
            cursor.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
                           (name, email, password_hash))
            conn.commit()
            self.display_message('Account created successfully')

        cursor.close()
        conn.close()

    def display_message(self, message):
        # clear the input fields
        self.name_input.text = ''
        self.email_input.text = ''
        self.password_input.text = ''
        # create and display the MDDialog
        dialog = MDDialog(title='Registration Status',
                          text=message,
                          size_hint=(0.7, 1),
                          buttons=[MDFlatButton(text='OK', on_release=self.close_dialog)])
        dialog.open()

    def close_dialog(self, inst):
        inst.parent.parent.parent.parent.dismiss()

    def go_to_login(self, instance):
        # go back to the login screen
        self.manager.current = 'login'
