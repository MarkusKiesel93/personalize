import datetime

import pandas as pd

#create dataframe
expense = {'date': [], 'expense': [], 'place': [], 'amount': []}
df = pd.DataFrame(data=expense)

first_date = datetime.date(2019,3,2)

date = first_date

with open('./spending.txt', 'r') as file:
    for line in file:
        if not line.strip():
            date = date + datetime.timedelta(days=1)
        else:
            expense['place'] = ''
            if line.strip() != '-':
                expense['date'] = date
                l = line.split()
                print(l)
                expense['amount'] = l.pop()
                if '(' in line:
                    place = l.pop()
                    place = place.replace('(', '')
                    place = place.replace(')', '')
                    expense['place'] = place
                expense['expense'] = ' '.join(l)
                df = df.append(expense, ignore_index=True)



df.to_csv(path_or_buf='./spending.csv')
