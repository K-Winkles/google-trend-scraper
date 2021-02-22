# google-trend-scraper

## Instructions (Mac):
1. Download and install Python 3.9 from here: https://www.python.org/downloads/release/python-392/. Scroll down and download "macOS 64-bit universal2 installer"
2. Run the installer and follow instructions
3. Head into System Preferences and select Keyboard > Shortcuts > Services. Find "New Terminal at Folder" in the settings and click the box. Now, when you're in Finder, just right-click a folder and you're shown the open to open Terminal. When you do, it'll start right in the folder you're in.
4. (Need to run this command only once) Type sudo chmod a+x install.sh
5. Hit enter
6. Type sudo ./install.sh
7. Hit enter
8. Wait for the set up to complete
9. Type sudo chmod a+x google-trend-scraper.py
10. Hit enter
11. You may now use the scraper

## HOW TO USE THE SCRAPER
On your command line, run the scraper by typing: 
`python3 ./google-trend-scraper.py [list of proxies separated by comma. no spaces] [list of keywords separated by comma. no spaces] [starting_date] [end_date]`
The words enclosed in square brackets are the arguments that you can pass to the scraper. For example, if you want to scrape from January 1, 2018 1 AM up to January 10, 2018 11 PM then you must replace `[starting_date]` with `2018-1-1T1` and `[end_date] with 2018-10-1T23`

For the proxies, you must provide them in list form. For example, if I have two proxies `https://34.203.233.13:80` and `https://34.203.233.14:81`, I should replace `[list of proxies separated by comma. no spaces]` with `https://34.203.233.13:80,https://34.203.233.14:81`. Remember to not put any spaces in between. Just separate the proxies with a comma.

Same concept applies to the keywords. If I have 5 keywords that I want to scrape like basketball,blockchain,baseball,golf,soccer, and elections then I will simply replace `[list of keywords separated by comma. no spaces]` with `basketball,blockchain,baseball,golf,soccer,elections`. Again, do not place spaces in between the commas. 

A sample command would look like this:
`python3 ./google-trend-scraper.py https://34.203.233.13:80,https://34.203.233.14:81 blockchain,basketball,facebook 2018-1-1T1 2018-2-1T23`

If you do not want to use a proxy, simply replace `[list of proxies separated by comma. no spaces]` with `no_proxy`




