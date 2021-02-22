#!/bin/sh

echo '***IMPORTANT: make sure you have installed Python3 on your system***'
curl -O https://bootstrap.pypa.io/ez_setup.py
python3 ez_setup.py
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py

pip install -r requirements.txt

echo 'set-up successful. you may now run the scraper with the following command:'
echo 'these sample commands will follow Mac syntax'
echo 'python3 ./google-trend-scraper.py [list of proxies separated by comma. no spaces] [list of keywords separated by comma. no spaces] [starting_date] [end_date]'
echo 'example: python3 ./google-trend-scraper.py https://34.203.233.13:80,https://34.203.233.14:81 blockchain,basketball,facebook 2018-1-1 2018-2-1'
echo 'if you do not want to use a proxy, put "no_proxy" in lieu of the list of proxies'
echo 'example: python3 ./google-trend-scraper.py no_proxy blockchain,basketball,facebook 2018-1-1 2018-2-1'