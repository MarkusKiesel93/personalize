import sys
from pathlib import Path
import subprocess as sp
# TODO: find better way runs only from setup/syslinks.py
print(Path(__file__).parent.parent.resolve().as_posix())
sys.path.append(Path(__file__).parent.parent.resolve().as_posix())

# TODO: make path relative
# TODO: remove old links

from configs.config import Config

class Syslinks:
    def __init__(self):
        self.config = Config()
        self.exc_scripts_dict = self.config.get_section('executable_scripts')
        self.usr_bin_path = Path().home() / '.local' / 'bin'
        self.path_scripts = Path().home() / self.config.get_section('path')['scripts']
        self.exc_scripts_path_list = self.__create_exc_scripts_path_list()

    def create(self):
        print('creating syslinks to executable scripts in {}'.format(self.usr_bin_path))
        for script_path in self.exc_scripts_path_list:
            sp.run(['ln', '-s', script_path, self.usr_bin_path])
            print('created sysling to {}'.format(script_path))

    def __create_exc_scripts_path_list(self):
        path_list = []
        for rep in self.exc_scripts_dict:
            path_rep = self.path_scripts / rep
            for script in self.exc_scripts_dict[rep]:
                path = path_rep / script
                path = path.resolve().as_posix()
                path_list.append(path)
        return path_list

if __name__=='__main__':
    s = Syslinks()
    print(s.exc_scripts_dict)
    print(s.usr_bin_path)
    print(s.path_scripts)
    print(s.exc_scripts_path_list)
    s.create()
