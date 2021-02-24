#! /usr/bin/Python

from pytrends.request import TrendReq
from functools import reduce
import pandas as pd
import sys

# this is the version without a control keyword
def main(proxies=None, keywords=None, timeframe=None):
    print('starting the scraper...')
    # get command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == 'no_proxy':
        proxies = None
        keywords = sys.argv[2].split(',')
        timeframe = sys.argv[3] + ' ' + sys.argv[4]
    elif len(sys.argv) == 4:
        proxies = sys.argv[1].split(',')
        keywords = sys.argv[2].split(',')
        timeframe = sys.argv[3] + ' ' + sys.argv[4]
    else:
        print('missing arguments!')

    kw_list = []

    # handle multi line keywords
    for i in range(len(keywords)):
        if '_' in keywords[i]:
            keywords[i] = keywords[i].replace('_',' ')
    j = -1
    # build list of lists of keywords
    for i in range(len(keywords)):
        if i % 4 == 0:
            kw_list.append([])
            kw_list[j].append(keywords[i])
            j += 1
        else:
            kw_list[j].append(keywords[i])
            if(len(kw_list[j]) == 5):
                j=0

    """
    print(proxies)
    print(keywords)
    print(control_keyword)
    print(timeframe)
    """
    results = []
    for item in kw_list:
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
        cnt = 0
        if keywords and timeframe:
            try:
                pytrends.build_payload(item, cat=0, timeframe=timeframe, geo='US', gprop='')
                results.append(pytrends.interest_over_time().drop(columns=['isPartial']))
            except:
                print('something went wrong')
    # merge dataframes
    overall_results = reduce(lambda left,right: pd.merge(left,right,on=['date'],how='outer'), results)

    # print results to excel file
    overall_results = overall_results.transpose()
    overall_results['keywords'] = overall_results.index
    overall_results.reset_index(drop=True, inplace=True)
    overall_results.to_excel('results.xlsx')
    print(overall_results)
    print('scraping complete')

# sample args
main(proxies=None, keywords=None, timeframe=None)