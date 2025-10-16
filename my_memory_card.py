#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QRadioButton, QButtonGroup
from random import *


app = QApplication([])
class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
    
window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(250,250)
button = QPushButton("Ответить")
group = QGroupBox("Варианты ответов")
group_2 = QGroupBox("Результат теста")
answer = QLabel("Правильно/Неправильно")
true = QLabel("Правильный ответ")
question = QLabel("Вопрос")
answer_1 = QRadioButton("Вариант 1")
answer_2 = QRadioButton("Вариант 2")
answer_3 = QRadioButton("Вариант 3")
answer_4 = QRadioButton("Вариант 4")
button_group = QButtonGroup()

button_group.addButton(answer_1)
button_group.addButton(answer_2)
button_group.addButton(answer_3)
button_group.addButton(answer_4)

def show_results():
    group.hide()
    group_2.show()
    button.setText("Следующий вопрос")

def show_question():
    group_2.hide()
    group.show()
    button.setText("Ответить")
    button_group.setExclusive(False)
    answer_1.setChecked(False)
    answer_2.setChecked(False)
    answer_3.setChecked(False)
    answer_4.setChecked(False)
    button_group.setExclusive(True)

buttons = [answer_1, answer_2, answer_3, answer_4]

def ask(q:Question):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong_1)
    buttons[2].setText(q.wrong_2)
    buttons[3].setText(q.wrong_3)
    question.setText(q.question)
    true.setText(q.right_answer)
    show_question()

def show_correct(res):
    answer.setText(res)
    show_results()

def check_answer():
    if buttons[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print("Статистика")
        print("-Всего вопросов:", window.total)
        print("-Правильных ответов:", window.score)
        print("Рейтинг:", window.score/window.total * 100,"%")
    else:
        show_correct('Неверно')


def next_question():
    window.total += 1
    print("Статистика")
    print("-Всего вопросов:", window.total)
    print("-Правильных ответов:", window.score)
    
    cur_question = randint(0, len(question_2) - 1)
 
    ask(question_2[cur_question])

def click_ok():
    if button.text() == "Ответить":
        check_answer()
    else:
        next_question()

layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()

layout_4 = QVBoxLayout()
layout_5 = QHBoxLayout()
layout_6 = QHBoxLayout()
layout_7 = QHBoxLayout()

layout_2.addWidget(answer_1)
layout_2.addWidget(answer_2)
layout_3.addWidget(answer_3)
layout_3.addWidget(answer_4)
layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)

layout_4.addWidget(answer, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_4.addWidget(true, alignment = Qt.AlignCenter)


group.setLayout(layout_1)
group_2.setLayout(layout_4)

layout_5.addWidget(question, alignment = Qt.AlignCenter)
layout_6.addWidget(group)
layout_6.addWidget(group_2)
layout_7.addStretch(1)
layout_7.addWidget(button, stretch = 2)
layout_7.addStretch(1)

main_layout = QVBoxLayout()
main_layout.addLayout(layout_5)
main_layout.addLayout(layout_6)
main_layout.addLayout(layout_7)
main_layout.setSpacing(15)

group_2.hide()
question_2 = []


question_2.append(Question("Государственный язык Бразилии", "Португальский", "Испанский", "Итальянский", "Бразильский"))
question_2.append(Question("Как пишется на английском питон","Python","Puton","Piton","Pyton"))
question_2.append(Question("Какого цвета нет на флаги России?","Фиолетовый", "Красный","Синий", "Белый"))

button.clicked.connect(click_ok)
window.setLayout(main_layout)
window.score = 0 
window.total = 0
next_question()
window.show()
app.exec_()