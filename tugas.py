import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QRadioButton, QButtonGroup, QPushButton, QComboBox, QGroupBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout
        self.setWindowTitle('Week 2: Layout - User Registration Form')
        self.setGeometry(100, 100, 450, 400)
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: Arial;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QGroupBox {
                font-size: 16px;
                font-weight: bold;
                border: 2px solid #3f51b5;
                border-radius: 8px;
                margin-top: 10px;
                padding: 10px;
            }
            QPushButton {
                background-color: #3f51b5;
                color: white;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #303f9f;
            }
            QLineEdit, QComboBox {
                border: 1px solid #3f51b5;
                border-radius: 5px;
                padding: 5px;
            }
        """)

        main_layout = QVBoxLayout()

        # Identity Section
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel('Nama : Andika Dhanan Jaya'))
        identity_layout.addWidget(QLabel('NIM : F1D022111'))
        identity_layout.addWidget(QLabel('Kelas : C'))
        
        identity_group = QGroupBox('Identitas')
        identity_group.setLayout(identity_layout)
        main_layout.addWidget(identity_group)

        # Navigation Section
        navigation_layout = QHBoxLayout()
        home_btn = QPushButton('Home')
        about_btn = QPushButton('About')
        contact_btn = QPushButton('Contact')
        navigation_layout.addWidget(home_btn)
        navigation_layout.addWidget(about_btn)
        navigation_layout.addWidget(contact_btn)

        main_layout.addLayout(navigation_layout)

        # User Registration Section
        form_layout = QVBoxLayout()

        self.full_name = QLineEdit()
        form_layout.addWidget(QLabel('Full Name:'))
        form_layout.addWidget(self.full_name)

        self.email = QLineEdit()
        form_layout.addWidget(QLabel('Email:'))
        form_layout.addWidget(self.email)

        gender_group = QButtonGroup(self)
        self.male_radio = QRadioButton('Male')
        self.female_radio = QRadioButton('Female')
        gender_group.addButton(self.male_radio)
        gender_group.addButton(self.female_radio)

        form_layout.addWidget(QLabel('Gender:'))
        form_layout.addWidget(self.male_radio)
        form_layout.addWidget(self.female_radio)

        self.country_combo = QComboBox()
        self.country_combo.addItems(['Select Country', 'USA', 'Canada', 'UK', 'Australia'])
        form_layout.addWidget(QLabel('Country:'))
        form_layout.addWidget(self.country_combo)

        form_group = QGroupBox('User Registration')
        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)

        # Actions Section
        actions_layout = QHBoxLayout()
        submit_btn = QPushButton('Submit')
        cancel_btn = QPushButton('Cancel')
        actions_layout.addWidget(submit_btn)
        actions_layout.addWidget(cancel_btn)
        main_layout.addLayout(actions_layout)

        # Set the main layout
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())