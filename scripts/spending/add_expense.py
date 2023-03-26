#!/bin/python3

import datetime
import time
import sys
from os.path import join, dirname, abspath
import pandas as pd
from curtsies import Input
import inquirer

class Expense_add():
    def __init__(self):
        self.new_expense = {'date': '', 'item': '', 'place': '', 'amount': 0.0, 'category': '', 'sub_category': ''}
        #self.db_path = join(dirname(abspath(__file__)), 'spending.csv')
        self.db_path = '~/Cloud/other/spending/spending.csv'
        self.db = pd.read_csv(self.db_path)

    def save_db(self):
        print(self.db.tail(10))
        self.db.to_csv(path_or_buf=self.db_path, index=False)
        print('successfully added data')

    def ask_new_expense(self):
        self.__ask_date()
        self.__ask_item()
        self.__ask_amount()

        self.__inquire_user('category')
        self.__inquire_user('sub_category')
        self.__inquire_user('place')

        self.db = self.db.append(self.new_expense, ignore_index=True)

    def __ask_date(self):
        today = datetime.date.today()
        days_delta = 0
        print('date:')
        # output in same line
        date = today
        sys.stdout.write('\r{}'.format(date))
        # use curtsies for Key input
        # decrese date with KEY_UP, incrise date with KEY_DOWN
        # select with return
        with Input(keynames='curses') as input_generator:
            for e in input_generator:
                if e == 'KEY_UP':
                    days_delta += 1
                if e == 'KEY_DOWN':
                    days_delta -= 1
                if e == '\n':
                    break
                date = today - datetime.timedelta(days=days_delta)
                sys.stdout.write('\r{}'.format(date))
        print('')
        self.new_expense['date'] = date

    def __ask_item(self):
        item = input('item:\n')
        while len(item) < 3:
            print('item needs to be given!')
            item = input('item:\n')
        self.new_expense['item'] = item

    def __ask_amount(self):
        amount = 0.0
        while amount <= 0.0:
            try:
                a = input('amount:\n')
                a = float(a)
                amount = a
            except ValueError:
                print('amount has to be given as float')
        self.new_expense['amount'] = amount

    def __inquire_user(self, column):
        choices = self.__get_choices(column)
        message = column.replace('_', ' ')
        questions = [inquirer.List(column, message=message, choices=choices)]
        answers = inquirer.prompt(questions)
        if answers[column] == 'new':
            self.new_expense[column] = input('new {}:\n'.format(column.replace('_', ' ')))
        elif answers[column] == 'blank':
            self.new_expense[column] = ''
        else:
            self.new_expense[column] = answers[column]

    def __get_choices(self, column):
        choices = self.db.query('item == "{}"'.format(self.new_expense['item']))
        choices = choices[column]
        choices = choices.drop_duplicates()
        choices = choices.dropna()
        choices = choices.tolist()
        choices += ['blank', 'new']
        return choices

if __name__=='__main__':
    ex_add = Expense_add()

    finished = False
    while not finished:
        ex_add.ask_new_expense()
        message = 'add another expense ?'
        choices = ['yes', 'no']
        questions = [inquirer.List('f', message=message, choices=choices)]
        answers = inquirer.prompt(questions)
        if answers['f'] == 'no':
            finished = True
    ex_add.save_db()
