#!/usr/bin/python3

import subprocess
import os

class ID_Manager:

    def __init__(self):
        self.ids = self.__get_all_ids()

    def get_new_id(self):
        new_id = []
        new_ids = self.__get_all_ids()
        for id in new_ids:
            if id not in self.ids:
                new_id.append(id)
        if len(new_id) > 1:
            print('more than one new ID')
        else:
            self.ids.append(new_id[0])
            return new_id[0]

    def __get_all_ids(self):
        ids = []
        sp = subprocess.run(['wmctrl', '-l'], stdout=subprocess.PIPE)
        sp_output = sp.stdout.decode('utf-8')
        sp_output_list = sp_output.split()
        for s in sp_output_list:
            if s[0:2] == '0x':
                ids.append(s)

        return ids

if __name__ == '__main__':
    id_manager = ID_Manager()

    os.system('wmctrl -s 0')
    os.system('wmctrl -r firefox -t 0')
    os.system('wmctrl -r firefox -e 0,0,0,1920,1000')

    os.system('wmctrl -s 1')
    os.system('gnome-terminal -- bash -c "cd $HOME/projects; exec bash" &')
    os.system('sleep 2')
    id = id_manager.get_new_id()
    os.system('wmctrl -i -r {} -t 1'.format(id))
    os.system('wmctrl -i -r {} -e 0,0,0,960,1080'.format(id))

    os.system('atom ~/business/ &')
    os.system('sleep 3')
    id = id_manager.get_new_id()
    os.system('wmctrl -i -r {} -t 1'.format(id))
    os.system('wmctrl -i -r {} -e 0,960,0,960,1080'.format(id))

    os.system('wmctrl -s 2')
    os.system('gnome-terminal -- bash -c "cd $HOME/projects; exec bash" &')
    os.system('sleep 1')
    id = id_manager.get_new_id()
    os.system('wmctrl -i -r {} -t 2'.format(id))
    os.system('wmctrl -i -r {} -e 0,0,0,960,1080'.format(id))

    os.system('gnome-terminal -- bash -c "cd $HOME/projects; exec bash" &')
    os.system('sleep 1')
    id = id_manager.get_new_id()
    os.system('wmctrl -i -r {} -t 2'.format(id))
    os.system('wmctrl -i -r {} -e 0,960,0,960,1080'.format(id))

    os.system('wmctrl -s 3')

    os.system('wmctrl -s 3')
    os.system('wmctrl -r spotify -t 3')
    os.system('wmctrl -r spotify -e 0,0,0,960,1080')

    os.system('wmctrl -r signal -t 3')
    os.system('wmctrl -r signal -e 0,960,0,960,1080')

    os.system('wmctrl -s 0')

    os.system('google-chrome --new-window http://127.0.0.1:8000 &')
    os.system('sleep 2')
    id = id_manager.get_new_id()
    os.system('wmctrl -i -r {} -e 0,1920,0,960,1080'.format(id))

    os.system('google-chrome --new-window http://127.0.0.1:8000/admin &')
    os.system('sleep 2')
    id = id_manager.get_new_id()
    os.system('wmctrl -i -r {} -e 0,2880,0,960,1080'.format(id))

    os.system('wmctrl -s 2')
