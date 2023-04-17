#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox
from random import shuffle



def ask(question1, right_answer, wrong1, wrong2, wrong3):
    shuffle(answer)
    question.setText(question1)
    answer[0].setText(right_answer)
    answer[1].setText(wrong1)
    answer[2].setText(wrong2)
    answer[3].setText(wrong3)

def check_answer():
    if answer[0].isChecked():
        radio.hide()
        res1 = QLabel('Правильно')
        button.setText('Следуюший вопрос')
    if answer[1].isChecked() or answer[2].isChecked()or answer[3].isChecked():
        radio.hide()
        res1 = QLabel('Неправильно')
        button.setText('Следуюший вопрос')


app = QApplication([])
main_win = QWidget()
main_win.resize(500, 300)
main_win.setWindowTitle('Memory Card')
question = QLabel('Какой национальности не существует?')
radio = QGroupBox('Варианты ответов')

widget = QRadioButton('Энцы')
widget1 = QRadioButton('Смурфы')
widget2 = QRadioButton('Чулымцы')
widget3 = QRadioButton('Алеуты')

answer = [widget, widget1, widget2, widget3]


layout_main = QVBoxLayout()
layout = QHBoxLayout()
layout1 = QVBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

layout.addWidget(question, alignment = Qt.AlignCenter)
layout2.addWidget(widget, alignment = Qt.AlignCenter)
layout2.addWidget(widget1, alignment = Qt.AlignCenter)
layout3.addWidget(widget2, alignment = Qt.AlignCenter)
layout3.addWidget(widget3, alignment = Qt.AlignCenter)
layout1.addLayout(layout2)
layout1.addLayout(layout3)

radio.setLayout(layout1)
layout4 = QHBoxLayout()
button = QPushButton('Ответить')
layout4.addStretch(1)
layout4.addWidget(button, stretch=3)
layout4.addStretch(1)
layout_main.addLayout(layout)
layout_main.addWidget(radio)
layout_main.addLayout(layout4)

main_win.setLayout(layout_main)
result = QGroupBox('Результат текста')
lb_Result = QLabel('верно/неверно')
lb_Correct = QLabel('ответ')

ask('Какой национальности не существует', 'Энцы', 'Смурфы', 'Чулымцы', 'Алеуты')
button.clicked.connect(check_answer)
main_win.show()
app.exec_()
