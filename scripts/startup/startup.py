# TODO: save the ids somewhere so I can close everything again should also work with wmctrl
# TODO: idmanager überabreiten

import subprocess

from config_handler import Config_handler
from id_manager import ID_Manager

class Startup_manager:
    def __init__(self):
        self.id_manager = ID_Manager()

    def run_program(program):
        """
        opens one program, moves to desktp and position
        has to be dict with command, desktop and position
        """
        subprocess.Popen(program['command'])

        # TODO: maby better way than sleep
        subprocess.run(['sleep', '2'])

        # get id for program
        # TODO: rename to get program id
        id = self.id_manager.get_new_id()

        self.move_program_to_position(id, program['position'])
        self.move_program_to_desktop(id, program['desktop'])

    def run_command(self, command):
        """
        runs command with subprocess
        has to be array of strings
        """
        subprocess.run(command)

    def move_program_to_position(self, program_id, position):
        """
        moves program to position by id
        """
        subprocess.run(['wmctrl', '-i', '-r', program_id, '-e', position])

    def move_program_to_desktop(self, program_id, desktop_number):
        """
        moves program to desktop by id
        """
        subprocess.run(['wmctrl', '-i', '-r', program_id, '-t', desktop_number])

    def go_to_window_0(self):
        subprocess.run(['wmctrl', '-s', '0'])

if __name__=='__main__':
    cf_handler = Config_handler()
    stup_manager = Startup_manager()

    # prompt user with choices of configs
    cf_handler.select_config()

    # get list of commands and programs + settings
    commands = cf_handler.get_commands()
    programs = cf_handler.get_programs()

    for command in commands:
        stup_manager.run_command(command)

    for program in programs:
        stup_manager.run_program(program)

    stup_manager.go_to_window_0()
