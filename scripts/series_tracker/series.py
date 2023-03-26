class Series():
    def __init__(self, name, season, episode, link):
        self.name = name
        self.season = int(season)
        self.episode = int(episode)
        self.link = link

    def get_csv_arr(self):
        arr = [self.name, self.season, self.episode, self.link]
        return arr

    def get_name(self):
        return self.name

    def get_season(self):
        return self.season

    def next_season(self):
        self.season += 1
        self.episode = 1

    def get_episode(self):
        return self.episode

    def next_episode(self):
        self.episode += 1

    def get_link(self):
        link = self.link
        link = link.replace('{{e}}', str(self.episode))
        link = link.replace('{{s}}', str(self.season))
        return link

    def get_str_arr(self):
        return [self.name, str(self.season), str(self.episode), self.link]

    def __str__(self):
        str = '{} | {} | {} | {}'.format(self.name, self.season, self.episode, self.link)
        return str
