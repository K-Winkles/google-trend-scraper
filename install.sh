#!/bin/sh

echo '***IMPORTANT: make sure you have installed Python3 on your system***'
curl -O https://bootstrap.pypa.io/ez_setup.py
python3 ez_setup.py
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py

pip install -r requirements.txt

echo 'set-up successful. you may now run the scraper.'
echo 'please read the README for instructions on how to run the scraper'