#!/bin/python3

import pandas as pd
import datetime

class Database_reader():
    def __init__(self):
        self.db_path = '~/Cloud/other/spending/spending.csv'
        self.db = pd.read_csv(self.db_path)
        self.db['date'] = pd.to_datetime(self.db['date'])

    def get_month(self, year, month):
        start_date = datetime.date(year, month, 1)
        end_date = datetime.date(year, month + 1, 1)
        query = 'date>="{}" & date<"{}"'.format(start_date, end_date)
        result = self.db.query(query)
        return result

    def query(self, db, querys):
        result = db
        for query in querys:
            result = result.query(query)
        return result




if __name__=="__main__":
    reader = Database_reader()

    month = reader.get_month(2020, 2)

    query_1 = 'category=="Nahrung"'
    querys = [query_1, ]
    output = reader.query(month, querys)
    print(output)

    print('Summe:')
    print(output['amount'].sum())
