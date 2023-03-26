# TODO: idmanager überabreiten
import subprocess

from id_manager import ID_Manager

class Program_manager:
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

        self.move_to_position(id, program['position'])
        self.move_to_desktop(id, program['desktop'])

    def run_command(self, command):
        """
        runs command with subprocess
        has to be array of strings
        """
        subprocess.run(command)

    def move_to_position(self, id, position):
        """
        moves program to position by id
        """
        subprocess.run(['wmctrl', '-i', '-r', id, '-e', position])

    def move_to_desktop(self, id, desktopNumber):
        """
        moves program to desktop by id
        """
        subprocess.run(['wmctrl', '-i', '-r', id, '-t', desktopNumber])

    def to_window_0(self):
        subprocess.run(['wmctrl', '-s', '0'])
