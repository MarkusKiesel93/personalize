from config import Config
from pathlib import Path

class DB_PATH:
    """
    handles links to the my databases
    needs specifyed database home (db_home)
    and names for each database
    """
    def __init__(self):
        self.config = Config()
        self.db_home = 'db_home'
        self.db_dict = self.config.get_section('database')

    def get(self, db_name):
        """
        db_name = name specifyed in config file for specific data file
        returns absolute path for database files as string
        """
        if db_name not in self.db_dict.keys():
            raise KeyError('no db with name {} in config file'.format(db_name))
        path = Path().home() # get home dir
        # add db_home and db file path
        path = path / self.db_dict[self.db_home] / self.db_dict[db_name]
        # resolve path and return as string
        path = path.resolve().as_posix()
        return path

# test
if __name__=='__main__':
    d = DB_PATH()
    print(d.get('series'))
    print(d.get('asdf'))
