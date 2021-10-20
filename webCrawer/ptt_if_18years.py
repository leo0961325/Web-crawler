import requests
from bs4 import BeautifulSoup
import time
import datetime

today = time.strftime('%m/%d').lstrip('0')  # 時間格式以及移除日期多於前面為0的月份
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1))
yesterday = yesterday.strftime("%m/%d").lstrip('0')


# 改成加上輸入我要的日期
def pttURL_if18(url, day):
    # 參考文章
    # https://medium.com/%E8%AA%A4%E9%97%96%E6%95%B8%E6%93%9A%E5%8F%A2%E6%9E%97%E7%9A%84%E5%95%86%E7%AE%A1%E4%BA%BAzino/cookic-%E7%AA%81%E7%A0%B4ptt-%E5%85%AB%E5%8D%A6%E7%89%88%E5%8D%81%E5%85%AB%E7%A6%81%E9%99%90%E5%88%B6-%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2%E7%B3%BB%E5%88%97-%E5%90%AB%E5%BD%B1%E7%89%87%E8%88%87%E7%A8%8B%E5%BC%8F%E7%A2%BC-5f4615031d4b
    #破除要訪問18歲才能進入的個版
    my_header = {'cookie' : 'over18=1;'}
    response = requests.get(url,headers = my_header)
    if response.status_code != 200:  # server不一定正常是200
        print('URL發生錯誤: ', url)
        return
    soup = BeautifulSoup(response.text, 'html5lib')
    # 取得上一頁
    paging = soup.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href']
    articles = []
    rents = soup.find_all('div', 'r-ent')
    for rent in rents:
        title = rent.find('div', 'title').text.strip()
        # 推文數
        count = rent.find('div', 'nrec').text.strip()
        # 日期有meta 跟 date兩層
        date = rent.find('div', 'meta').find('div', 'date').text.strip()
        # article = '%s %s:%s' %(date,count,title)
        article = '{0} {1}:{2}'.format(date, count, title)

        try:
            # 必須是 今天 以及 推文數>10
            if day == date and int(count) > 10:
                articles.append(article)
        except:
            # 推文是'爆'也印出來
            if day == date and count == '爆':
                articles.append(article)
    # 如果文章數不是0 就印出來
    if len(articles) != 0:
        for article in articles:
            print(article)
        # 繼續爬上一頁，必須為 網域+paging (path)
        pttURL_if18('https://www.ptt.cc' + paging, day)
    else:
        return


# pttURL_if18('https://www.ptt.cc/bbs/Beauty/index.html', today)
print(today)
pttURL_if18('https://www.ptt.cc/bbs/Gossiping/index.html',today)

