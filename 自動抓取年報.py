def annual_report(stock_id,year):
    url = "https://doc.twse.com.tw/server-java/t57sb01"

    data  = {
        'id':'',
        'key':'', 
        'step':'1',
        'co_id': stock_id,
        'year': year,
        'seamon':'', 
        'mtype':'F',
        'dtype':'F04'
    }
    try:
        response = requests.post(url,data=data)
        link = BeautifulSoup(response.text,'html.parser')
        filname = link.find('a').text   # 可抓出檔名(為了丟給第二個payload使用)
    except Exception as e:
        print(f'發生{e}錯誤')
    
    # 建立第二個POST request
    data2 = {
        'step': '9',
        'kind': 'F',
        'co_id': stock_id,
        'filename': filname
        }
    
    try:
        response = requests.post(url, data=data2)
        link = BeautifulSoup(response.text,'html.parser')
        link = link.find('a')  # 抓出<a>~~</a>整個標籤內容
        link = link.get('href') # 再從裡面抓出href的內容(正是我們要的)
    except Exception as e:
        print(f'發生{e}錯誤')

    try:
        response = requests.get('https://doc.twse.com.tw' + link)
        with open(f'{stock_id}_{year}.pdf','wb') as f:
            f.write(response.content)
    except Exception as e:
        print(f'發生{e}錯誤')



# 日後直接輸入(代號、年份)即可
annual_report(2382,112)
    
