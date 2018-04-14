#!/bin/bash
sudo apt-get install python3
sudo apt-get install python3-django
sudo apt-get install pip3
sudo pip3 install virtualenv virtualenvwrapper
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3">> .bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh">> .bashrc


