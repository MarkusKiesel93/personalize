import subprocess

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
