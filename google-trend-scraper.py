#! /usr/bin/Python

from pytrends.request import TrendReq
import pandas as pd
import sys

def main(proxies=None, keywords=None, control_keyword=None, timeframe=None):
    print('starting the scraper...')

    # get command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == 'no_proxy':
        proxies = None
        keywords = sys.argv[2].split(',')
        control_keyword = sys.argv[3]
        timeframe = sys.argv[4] + ' ' + sys.argv[5]
    elif len(sys.argv) == 5:
        proxies = sys.argv[1].split(',')
        keywords = sys.argv[2].split(',')
        control_keyword = sys.argv[3]
        timeframe = sys.argv[4] + ' ' + sys.argv[5]
    else:
        print('missing arguments!')

    if control_keyword == 'no_control_keyword':
        control_keyword = None

    # handle multi line keywords
    for i in range(len(keywords)):
        if '_' in keywords[i]:
            keywords[i] = keywords[i].replace('_',' ')

    if control_keyword and '_' in control_keyword:
        control_keyword = control_keyword.replace('_', ' ')
    """
    print(proxies)
    print(keywords)
    print(control_keyword)
    print(timeframe)
    """
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
            #control check
            if len(keywords) > 5 and not control_keyword:
                print('you need to include a control keyword to make sure that your queries are statistically accurate')
                return

            if control_keyword:
                trends = []
                headers = []
                data = []
                dates = []
                results = {}

                # fetch each query
                for keyword in keywords:
                    pytrends.build_payload([control_keyword, keyword], cat=0, timeframe=timeframe, geo='US', gprop='')
                    trends.append(pytrends.interest_over_time())
                headers.append('')
                data.append(trends[0].index.values)
                
                for trend in trends:
                    column = trend[trend.columns[-2]]
                    headers.append(column.name)
                    data.append(column.values)

                headers.append('the office')
                data.append(trends[0]['the office'].values)

                for i in range(len(headers)):
                    results[headers[i]] = data[i]
                
                results = pd.DataFrame.from_dict(results)
            else:
                pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo='US', gprop='')
                results = pytrends.interest_over_time()

            # print results to excel file
            results = results.transpose()
            results['keywords'] = results.index
            results.reset_index(drop=True, inplace=True)
            results.to_excel('results.xlsx')
            print(results)
            print('scraping complete')
        except:
            print('something went wrong')

# sample args
main(proxies=None, keywords=None, timeframe=None)