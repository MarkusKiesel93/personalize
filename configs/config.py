import yaml

from pathlib import Path

class Config:
    """
    handles the loading and returning of data from the config file
    """
    def __init__(self):
        self.cfg_file_name = 'config.yml'
        self.config_yml = Path(__file__).parent / self.cfg_file_name
        self.config_yml = self.config_yml.resolve().as_posix() # resolve and return as string
        self.config_dict = self.__load_config_dict()

    def get(self):
        """
        returns the config as dictionary
        """
        return self.config_dict

    def get_section(self, section):
        """
        returns a section of the config dictionary
        """
        if section not in self.config_dict.keys():
            raise KeyError('no sction {} in config file'.format(section))
        return self.config_dict[section]


    def get_path(self):
        """
        returns the path of the config file
        """
        return self.config_yml

    # loads the config file with yaml
    def __load_config_dict(self):
        with open(self.config_yml, 'r') as cfg_file:
            cfg = yaml.safe_load(cfg_file)
        return cfg

# test
if __name__=='__main__':
    c = Config()
    print(c.get())
    print(c.get_path())
    print(c.get_section('database'))
    print(c.get_section('p'))
