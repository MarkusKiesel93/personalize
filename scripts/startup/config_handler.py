from os import listdir
from os.path import isfile, join, dirname, abspath, splitext
import json
import inquirer

class Config_handler():
    def __init__(self):
        # abspath gives the path of the current file with __file__
        # dirname gives the dir of the path
        # join joins a path
        self.configs_path = join(dirname(abspath(__file__)), 'configs')
        # using list comprehension to list all items in dir and check if they are files
        # splitext splits file name and extension
        self.config_choices = [splitext(f)[0] for f in listdir(self.configs_path) if isfile(join(self.configs_path, f)) and splitext(f)[1] == '.json']
        self.config_files_loaded = []
        self.commands = []
        self.programs = []

    def select_config(self):
        """
        prompts user with choices of configs and stores file to self.selected_config
        """
        message = 'Select config to load'
        questions = [inquirer.List('config', message=message, choices=self.config_choices)]
        # use inquirer to let user select choice and store to answer
        answers = inquirer.prompt(questions)
        # load configs and create commands and programs
        self.__load_config(answers['config'])
        self.__create_commands()
        self.__create_programs()


    def get_commands(self):
        """
        returns list of commands
        """
        return self.commands

    def get_programs(self):
        """
        returns list of programs with settings
        """
        return self.programs

    def __load_config(self, config_file_name):
        """
        load selected config file from name and
        load all config files it builds on specifyed in useConfig
        """
        config = self.__load_config_file(config_file_name)
        self.config_files_loaded.append(config)
        # check if selected config builds on another config
        while 'useConfig' in config.keys():
            # load every file in the useConfig list, start from last
            for useConfig in config['useConfig'].reverse():
                config = self.__load_config_file(useConfig)
                self.config_files_loaded.append(config)
        # reverse list of config files to start with the first file we build on
        self.config_files_loaded.reverse()

    def __load_config_file(self, config_file_name):
        """
        loads and retruns one config json file
        """
        config_file = '.'.join((config_file_name, 'json'))
        with open(join(self.configs_path, config_file)) as json_file:
            return json.load(json_file)

    def __create_commands(self):
        """
        create list of commands from loaded config files list
        """
        for config in self.config_files_loaded:
            if 'commands' in config.keys():
                for command in config['commands']:
                    # splitt command in array of strings to be executed by subprocess
                    self.commands.append(command.split())

    def __create_programs(self):
        """
        create list of programs from loaded config files list
        each program is a dict with command, desktop and position as keys
        """
        for config in self.config_files_loaded:
            if 'programs' in config.keys():
                for program in config['programs']:
                    self.programs.append(self.__format_program(program))

    def __format_program(self, program):
        """
        returns a dict with all commands and programs to be executed by subprocess
         programs: {
            command: "command",
            desktop: "desktop",
            position: "position"
         }
        }
        """
        # turn the command in a [] of strings
        program['command'] = program['command'].split()
        # cast desktop number to string
        program['desktop'] = str(program['desktop'])
        # create string as 'gravity,x,y,width,height'
        # gravity always 0
        # and cast numbers to string
        if 'position' in program.keys():
            program['position'] = ','.join([
                '0',
                str(program['position']['x']),
                str(program['position']['y']),
                str(program['position']['width']),
                str(program['position']['height'])])
        return program
