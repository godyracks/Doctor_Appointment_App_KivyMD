from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField

from database import delete_appointment, create_appointment


class AppointmentScreen(Screen):
    def __init__(self, **kwargs):
        super(AppointmentScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        # Heading and Logo
        header = BoxLayout(size_hint=(1, 0.1))
        logo = Image(source='hospital_logo.png', size_hint=(0.3, 1))
        heading = BoxLayout(size_hint=(0.8, 1))
        heading_label = MDLabel(text='LU Hospital', halign='center', font_style='H4', font_size=48, bold=True)
        subheading_label = MDLabel(text='Book Appointment', halign='center', font_style='Subtitle1', font_size=36)
        heading.add_widget(heading_label)
        heading.add_widget(subheading_label)
        header.add_widget(logo)
        header.add_widget(heading)
        layout.add_widget(header)

        # Entries for user input
        self.name_ent = MDTextField(hint_text="Enter patient's name")
        layout.add_widget(self.name_ent)

        self.age_ent = MDTextField(hint_text="Enter age")
        layout.add_widget(self.age_ent)

        self.gender_ent = MDTextField(hint_text="Enter gender")
        layout.add_widget(self.gender_ent)

        self.location_ent = MDTextField(hint_text="Enter location")
        layout.add_widget(self.location_ent)

        self.time_ent = MDTextField(hint_text="Enter appointment time")
        layout.add_widget(self.time_ent)

        self.phone_ent = MDTextField(hint_text="Enter phone number")
        layout.add_widget(self.phone_ent)

        # Button to add appointment
        self.submit = MDFlatButton(text="Book Appointment", md_bg_color=(0, 0.6, 1, 1), on_press=self.add_appointment)
        layout.add_widget(self.submit)

        # Button to delete appointment
        self.delete = MDFlatButton(text="Cancel Appointment", md_bg_color=(1, 0, 0, 1),
                                   on_press=self.cancel_appointment)
        layout.add_widget(self.delete)

        # return layout
        self.add_widget(layout)

    # Function to add appointment
    def add_appointment(self, instance):
        # Get the user inputs
        self.val1 = self.name_ent.text
        self.val2 = self.age_ent.text
        self.val3 = self.gender_ent.text
        self.val4 = self.location_ent.text
        self.val5 = self.time_ent.text
        self.val6 = self.phone_ent.text

        # Check if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            Snackbar(text="Please fill up all boxes").open()
        else:
            # Add the appointment to the database
            create_appointment(self.val1, self.val2, self.val3, self.val4, self.val5, self.val6)
            self.dialog = MDDialog(title="Success", text="Appointment for " + self.val1 + " has been created",
                                   size_hint=(0.7, 1),
                                   buttons=[MDFlatButton(text='OK', on_release=self.close_dialog)])
            self.dialog.open()

            # functiion to delete appointment

    def cancel_appointment(self, instance):
        # Get the user inputs
        self.val1 = self.name_ent.text
        self.val2 = self.time_ent.text

        # Check if the user input is empty
        if self.val1 == '' or self.val2 == '':
            Snackbar(text="Please fill up all boxes").open()
        else:
            delete_appointment(self.val1, self.val2)
            self.dialog = MDDialog(title="Success", text="Appointment for " + self.val1 + " has been deleted",
                                   size_hint=(0.7, 1),
                                   buttons=[MDFlatButton(text='OK', on_release=self.close_dialog)])
            self.dialog.open()
            # else:
            Snackbar(text="Appointment not found").open()

        # Method to close the dialog

    def close_dialog(self, *args):
        self.dialog.dismiss()


