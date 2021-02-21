from pytrends.request import TrendReq

# proxy is an array of ip addresses
def main(proxy=None, keywords=None, timeframe=None):
    if proxy:
        pytrends = TrendReq(
            hl='en-US', 
            tz=360, 
            timeout=(10,25), 
            proxies=proxy, 
            retries=3, 
            backoff_factor=0.2, 
            requests_args={'verify':False}
        )
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
            pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo='', gprop='')
            timeframe = timeframe.split(' ')

            date_to = timeframe[1]
            date_from = timeframe[0]

            date_to = date_to.split('-')
            date_from = date_from.split('-')

            results = pytrends.get_historical_interest(
                keywords, 
                year_start=int(date_from[0]), 
                month_start=int(date_from[1]), 
                day_start=int(date_from[2]), 
                hour_start=0, 
                year_end=int(date_to[0]), 
                month_end=int(date_to[1]), 
                day_end=int(date_to[2]), 
                hour_end=0, 
                cat=0, 
                geo='', 
                gprop='', 
                sleep=0.1
            )

            results = results.transpose()

            results['keywords'] = results.index
            results.reset_index(drop=True, inplace=True)
            results = results.head(-1)
            results.to_excel('results.xlsx')
        except:
            print('Something went wrong')

main(proxy=None, keywords=['basketball', 'baseball', 'blockchain'], timeframe='2018-1-1 2018-2-1')