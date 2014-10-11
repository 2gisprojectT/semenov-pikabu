# =*- coding: utf-8 -*-

from unittest import TestCase
import Leo
import unittest

#               сытый                                   голодный
#   антилопа    спать, перейти в состояние голодный     съесть, перейти в состояние сытый
#   охотник     убежать, перейти в состояние голодный   убежать
#   дерево      смотреть, перейти в состояние голодный  спать
#начальное состояние: сытый

class TestOfLeo(TestCase):
    def test_init(self):
        #тест инициализации класса с пустой строкой
        temp = Leo.Leo("")
        self.assertEqual([], temp.historyOfActions, "history of actions is not empty")
        self.assertEqual([], temp.historyOfStates, "history of states is not empty")
        self.assertEqual("сытый", temp.state, "start state is wrong")

    def test_hungryTosatisfied(self):
        #тестирование переходов по графу
        temp2 = Leo.Leo("антилопа антилопа охотник охотник дерево антилопа дерево")
        self.assertEqual(["сытый->голодный", "голодный->сытый", "сытый->голодный", "голодный->голодный", "голодный->голодный", "голодный->сытый", "сытый->голодный"], temp2.historyOfStates, "history of states is wrong")
        self.assertEqual(["спать", "съесть", "убежать", "убежать", "спать", "съесть", "смотреть"], temp2.historyOfActions, "history of action is wrong")
        self.assertEqual("голодный", temp2.state, "start state is wrong")

    def test_wrong_data(self):
        #ввод несуществующей команды
        temp = Leo.Leo("несуществующаяКоманда антилопа")
        self.assertEqual("сытый", temp.state, "start state is wrong (\"несущуствующая Команда\")")

    def test_wrong_type(self):
        #ввод не строки
        temp = Leo.Leo(123)
        self.assertEqual([], temp.historyOfActions, "history of actions is not empty")
        self.assertEqual([], temp.historyOfStates, "history of states is not empty")
        self.assertEqual("сытый", temp.state, "start state is wrong")

if __name__ == '__main__':
    unittest.main()