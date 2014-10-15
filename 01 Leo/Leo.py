# =*- coding: utf-8 -*-

class Leo:

    def __init__(self, commands):
        self.historyOfStates = []
        self.historyOfActions = []
        self.state = "сытый"
        self.commands = {}
        try:
            self.commands = commands.split()
        except AttributeError:
            print "Неверный формат данных"
            return
        if len(self.commands)==0:
            print "Нет ни одной комманды"
        for t in self.commands:
            print("Команда: " + t)
            if t == "антилопа":
                if self.state == "сытый":
                    self.action("спать")
                    self.stateHungry()
                elif self.state == "голодный":
                    self.action("съесть")
                    self.stateSatisfied()
            elif t == "охотник":
                if self.state == "сытый":
                    self.action("убежать")
                    self.stateHungry()
                elif self.state == "голодный":
                    self.action("убежать")
                    self.stateHungry()
            elif t == "дерево":
                if self.state == "сытый":
                    self.action("смотреть")
                    self.stateHungry()
                elif self.state == "голодный":
                    self.action("спать")
                    self.stateHungry()
            else:
                print "Ошибка: нет такой команды"
                break
        print "Завершено выполнение программы"
        #print self.historyOfStates
        for t in self.historyOfStates:
            print t,
        print ""
        for t in self.historyOfActions:
            print t,
        print ""

    def action(self, action):
        print "Действие: " + action
        self.historyOfActions.append(action)

    def stateHungry(self):
        historyString = ""
        if self.state == "сытый":
            print "Переход в состояние голодный"
            historyString = "сытый->голодный"
        self.state = "голодный"
        if historyString != "":
            self.historyOfStates.append(historyString)
        else:
            self.historyOfStates.append("голодный->голодный")

    def stateSatisfied(self):
        historyString = ""
        if self.state == "голодный":
            print "Переход в состояние сытый"
            historyString = "голодный->сытый"
        self.state = "сытый"
        if historyString != "":
            self.historyOfStates.append(historyString)
        else:
            self.historyOfStates.append("сытый->сытый")

#print "Введите последовательность команд: "
#text = ""
#flag = False
#try:
#    text = input()
#    flag = True
#except SyntaxError:
#    print "Ошибка. Возможные причины:"
#    print "1. Ничего не введено"
#    print "2. Введена строка без кавычек"
#    print "3. Внутри строки используются кавычки"
#if flag == True:
#    temp = Leo(text)