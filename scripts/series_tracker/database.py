import csv
from pathlib import Path

from series import Series

class Database():
    def __init__(self):
        self.folder = str(Path.home()) + '/.personalize/myScripts/series_tracker/'
        self.db_file = self.folder + 'series_db.csv'                    # -> name of db file
        self.current_series_file =  self.folder + 'current_series.txt'   # -> name file for current series
        self.db = self.__load_db()                                      # -> database
        self.current_series = self.__load_current()                     # -> current series as Series object

    #get Database
    def get_db(self):
        return self.db

    #get current series
    def get_current_series(self):
        return self.current_series

    def set_current_series(self, series_name):
        self.current_series = self.__find_series(series_name)
        self.__save_current()

    #updates the db for the selected to either increment the series number
    def next_season(self):
        self.current_series.next_season()
        self.__recreate_db()

    #updates the db for the selected to either increment the episode number
    def next_episode(self):
        self.current_series.next_episode()
        self.__recreate_db()

    #returns an array of names of the tracked series
    def get_series_name_arr(self):
        arr = []
        for series in self.db:
            arr.append(series.get_name())
        return arr

    #adds new sereis to database
    def add_series(self, series):
        series_arr = series.split(' ')
        new_series = Series(series_arr[0], series_arr[1], series_arr[2], series_arr[3])
        self.db.append(new_series)
        self.__recreate_db()

    #removes series from database
    def remove_series(self):
        self.db.remove(self.current_series)
        self.__recreate_db()

    #loads database
    def __load_db(self):
        db = []
        with open(self.db_file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                series = Series(row[0], row[1], row[2], row[3])
                db.append(series)
        return db

    #loads current series object specifyed in current_series file
    def __load_current(self):
        with open(self.current_series_file, 'r') as f:
            series_name = f.read()
        return self.__find_series(series_name)

    #returns the series object from the database
    def __find_series(self, series_name):
        found_series = None
        for series in self.db:
            if series_name.strip() == series.get_name().strip():
                found_series = series
        return found_series

    #rewrites the database
    def __recreate_db(self):
        with open(self.db_file, 'w', newline='') as f:
            writer = csv.writer(f)
            for series in self.db:
                writer.writerow(series.get_csv_arr())

    #saves the current series name to the current_series file
    def __save_current(self):
        with open(self.current_series_file, 'w') as f:
            f.write(self.current_series.get_name())

    #representation of the db
    def __str__(self):
        header = 'series name       | season | episode | link'
        str = header + '\n'
        for series in self.db:
            n, s, e, l = series.get_str_arr()
            str += '{}{} |{}{} |{}{} | {}\n'.format(
            n, ' '*(17 - len(n)),
            ' '*(7 - len(s)), s,
            ' '*(7 - len(e)), e,
            l)
        return str
