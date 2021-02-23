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
`python3 ./google-trend-scraper.py [list of proxies separated by comma. no spaces] [list of keywords separated by comma. no spaces] [control keyword] now [hours, days, or months before now]`

### Keywords

If I have 5 keywords that I want to scrape like basketball,blockchain,baseball,golf,soccer, and elections then I will simply replace `[list of keywords separated by comma. no spaces]` with `basketball,blockchain,baseball,golf,soccer,elections`. Again, do not place spaces in between the commas. 

If your keywords have spaces such as 'game of thrones', simply type it with underscores like this: game_of_thrones

### Timeframe
The words enclosed in square brackets are the arguments that you can pass to the scraper. For example, if you want to scrape from now to 7 days before then you must replace `[hours, days, or months before now]` with `7-d` to get `now 7-d`

Current Time Minus Time Pattern:

By Month: `today #-m` where # is the number of months from that date to pull data for

For example: `today 3-m` would get data from today to 3months ago
NOTE Google uses UTC date as `today`
Works for 1, 3, 12 months only!
Daily: `now #-d` where # is the number of days from that date to pull data for

For example: `now 7-d` would get data from the last week
Works for 1, 7 days only!
Hourly: `now #-H` where # is the number of hours from that date to pull data for

For example: `now 1-H` would get data from the last hour
Works for 1, 4 hours only!

### Control keyword

The control keyword is the keyword in your dataset that is the most popular. We need this keyword because of the limitations of the API. The API cannot allow more than 5 keywords at a time so what will happen is that we will compare each keyword with the control keyword and combine the lists at the end so that the scraper will work for more than 5 keywords. Note that for best results, choose a control keyword that is the most popular. 

A sample command with more than 5 keywords would look like this:
`python3 ./google-trend-scraper.py no_proxy stranger_things,friends,riverdale,game_of_thrones,breaking_bad,money_heist,peaky_blinders,black_mirror the_office now 7-d`

Note that the office was chosen as the control keyword because out of all the shows listed in the keyword list, it is objectively the most popular one. 

If you have less than 5 keywords and do not need to use a control keyword, simply type `no_control_keyword`

### Proxies

For the proxies, you must provide them in list form. For example, if I have two proxies `https://34.203.233.13:80` and `https://34.203.233.14:81`, I should replace `[list of proxies separated by comma. no spaces]` with `https://34.203.233.13:80,https://34.203.233.14:81`. Remember to not put any spaces in between. Just separate the proxies with a comma.

If you do not want to use a proxy, simply replace `[list of proxies separated by comma. no spaces]` with `no_proxy`

### Sample commands

1. With a proxy, 3 keywords, no control keyword, time frame of past 7 days
`python3 ./google-trend-scraper.py https://34.203.233.13:80,https://34.203.233.14:81 blockchain,basketball,facebook no_control_keyword now 7-d`

2. Without a proxy, more than 5 keywords, with a control keyword, time frame of past month
`python3 ./google-trend-scraper.py no_proxy stranger_things,friends,riverdale,game_of_thrones,breaking_bad,money_heist,peaky_blinders,black_mirror the_office today 1-m`

### Caveats

The values you will get are relative to the keywords used. For example, in a query with both The Office and Stranger Things, The Office is definitely going to have higher scores relative to Stranger Things. This is reflective of their relationship with each other. However, if you check the Google Trends site for yourself and look up either one of those keywords, it might not be the same. Why? This is because Google gives values relative to their entire database. 

What this scraper does is give values relative to the group of keywords that you have requested. It is not possible to do what Google does simply because their database is not publicly available. What this API guarantees is that though the values might not exactly be the same as what is being shown on the Google Trends website, the statistical meaning and significance remains the same.