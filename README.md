# google-trend-scraper

## Instructions (Mac):
1. Download and install Python 3.9 from here: https://www.python.org/downloads/release/python-392/. Scroll down and download "macOS 64-bit universal2 installer"
2. Run the installer and follow instructions
3. Open the folder containing the scraper files
4. Right click and choose 'open terminal here'
5. Type ./install.sh
6. Hit enter
7. Wait for the set up to complete
8. You may now use the scraper

## HOW TO USE THE SCRAPER
On your command line, run the scraper by typing: 
`python3 google-trend-scraper.py [list of proxies separated by comma. no spaces] [list of keywords separated by comma. no spaces] [starting_date] [end_date]`
The words enclosed in square brackets are the arguments that you can pass to the scraper. For example, if you want to scrape from January 1, 2018 up to January 10, 2018 then you must replace `[starting_date]` with `2018-1-1` and `[end_date] with 2018-10-1`

For the proxies, you must provide them in list form. For example, if I have two proxies `https://34.203.233.13:80` and `https://34.203.233.14:81`, I should replace `[list of proxies separated by comma. no spaces]` with `https://34.203.233.13:80,https://34.203.233.14:81`. Remember to not put any spaces in between. Just separate the proxies with a comma.

Same concept applies to the keywords. If I have 5 keywords that I want to scrape like basketball,blockchain,baseball,golf,soccer, and elections then I will simply replace `[list of keywords separated by comma. no spaces]` with `basketball,blockchain,baseball,golf,soccer,elections`. Again, do not place spaces in between the commas. 

A sample command would look like this:
`python3 google-trend-scraper.py https://34.203.233.13:80,https://34.203.233.14:81 blockchain,basketball,facebook 2018-1-1 2018-2-1`

If you do not want to use a proxy, simply replace `[list of proxies separated by comma. no spaces]` with `no_proxy`




