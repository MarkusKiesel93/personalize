#!/usr/bin/python3

from argparse import ArgumentParser
import subprocess

from database import Database

class Series_Tracker():
    def __init__(self):
        self.db = Database()

    #startes firefox with the link for the series
    def stream(self):
        link = self.db.get_current_series().get_link()
        subprocess.Popen(['firefox', link])


#what happens when the script is called
if __name__ == '__main__':
    #create Series Tracker object
    st = Series_Tracker()
    series_names = st.db.get_series_name_arr()

    #pares arguments
    parser = ArgumentParser(description='track and stream series')
    parser.add_argument('-s', '--series', choices=series_names)
    parser.add_argument('-sn', '--stream_next', action='store_true')
    parser.add_argument('-sns', '--stream_next_season', action='store_true')
    parser.add_argument('-l', '--list', action='store_true')
    parser.add_argument('-c', '--current_show', action='store_true')
    parser.add_argument('-n', '--new', help='in form: series_name season episode link{{s}}{{e}}')
    parser.add_argument('-rm', '--remove', action='store_true')
    args = parser.parse_args()

    if args.series != None:
        st.db.set_current_series(args.series)

    if args.stream_next == True:
        st.stream()
        st.db.next_episode()

    if args.stream_next_season == True:
        st.stream()
        st.db.next_season()

    if args.list == True:
        print(st.db)

    if args.current_show == True:
        print(st.db.get_current_series().get_name())

    if args.new != None:
        st.db.add_series(args.new)

    if args.remove == True:
        if args.series != None:
            st.db.remove_series()
        else:
            print('no series specifyed')
