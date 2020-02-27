"""
Author: yaming
Email: wei_ym@yeah.net
Wechat: ahrztj_wei


date: 2019/10/24 19:48
desc: auto download the data
"""

import requests
from bs4 import BeautifulSoup
import time


if __name__ == '__main__':
    # url = 'https://data.ngdc.noaa.gov/platforms/ocean/ships/natsushima/NT05-11/multibeam/data/version1/MB/SBAT8160_00_2005_200_201805_oic.mb84.gz'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
        'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;wd=&amp;eqid=c3435a7d00006bd600000003582bfd1f'
        }

    folder = r'./data/all_data/'  ## targeted folder
    htmlfile = open('wei.html', 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    soup = BeautifulSoup(htmlhandle, 'html.parser')

    tbody = soup.find_all('table', attrs={'class':'aborder'})
    td = tbody[0].find_all('td', attrs={'class':'cborder'})
    urls = 'urls.txt'


    count = 1
    for item in td:

        url = item.a.attrs['href']

        ## get the all links
        with open(urls, 'a') as test:
            test.write(url)
            test.write('\n')

        # path = folder + '/' + item.a.string
        # res = requests.get(url=url, headers=headers, timeout=10)
        #
        # ## download the data
        # with open(path, 'wb') as file:
        #     file.write(res.content)

        print(' %d is right.' % count)
        count = count + 1
        time.sleep(2)
    print('all is right.')