# include aliases
copy config/aliases to ~/.bash_aliases
run source ~/.bashrc

# link all scripts to HOME/.local/bin/
sudo ln -s ~/personalize/scripts/timer/timer HOME/.local/bin/
sudo ln -s ~/personalize/scripts/timer/pomodoro HOME/.local/bin/

# TODO: remove last line for MyScripts

# create link from database to cloud
# in db folder
# take database link from config.yml
ln -s  ~/Cloud/database/postgres_data/ postgres_data
