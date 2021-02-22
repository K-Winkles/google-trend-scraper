#! /usr/bin/Python

from pytrends.request import TrendReq
import sys

def main(proxies=None, keywords=None, timeframe=None):
    # get command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == 'no_proxy':
        proxy = None
        keywords = sys.argv[2].split(',')
        timeframe = sys.argv[3] + ' ' + sys.argv[4]
    elif len(sys.argv) == 5:
        proxies = sys.argv[1].split(',')
        keywords = sys.argv[2].split(',')
        timeframe = sys.argv[3] + ' ' + sys.argv[4]
    else:
        print('missing arguments!')
    
    print(proxies)
    print(keywords)
    print(timeframe)

    if proxies:
        try:
            pytrends = TrendReq(
                hl='en-US', 
                tz=360, 
                timeout=(10,25), 
                proxies=proxies, 
                retries=3, 
                backoff_factor=0.2, 
                requests_args={'verify':False}
            )
        except:
            print('there is something wrong with your proxies')
    else:
        pytrends = TrendReq(
            hl='en-US',
            tz=360,
            timeout=(10,25),
            retries=3,
            backoff_factor=0.2,
            requests_args={'verify':False}
        )

    if keywords and timeframe:
        try:
            pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo='US', gprop='')
            timeframe = timeframe.split(' ')

            date_to = timeframe[1]
            date_from = timeframe[0]

            date_to = date_to.split('-')
            date_from = date_from.split('-')

            # get hour value
            day_hour_from = date_from[2].split('T')
            day_from = int(day_hour_from[0])
            hour_from = int(day_hour_from[1])

            day_hour_to = date_to[2].split('T')
            day_to = int(day_hour_to[0])
            hour_to = int(day_hour_to[1])

            results = pytrends.get_historical_interest(
                keywords, 
                year_start=int(date_from[0]), 
                month_start=int(date_from[1]), 
                day_start=day_from, 
                hour_start=hour_from, 
                year_end=int(date_to[0]), 
                month_end=int(date_to[1]), 
                day_end=day_to, 
                hour_end=hour_to, 
                cat=0, 
                geo='US', 
                gprop='', 
                sleep=0.1
            )

            results = results.transpose()
            results['keywords'] = results.index
            results.reset_index(drop=True, inplace=True)
            results = results.head(-1)
            results.to_excel('results.xlsx')
            print(results)
        except:
            print('something went wrong')

# sample args
main(proxies=None, keywords=['basketball', 'baseball', 'blockchain'], timeframe='2018-1-1 2018-2-1')