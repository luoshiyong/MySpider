import requests
import unicodedata
from lxml import etree
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
    }
mulu_url = 'https://www.bqg5.cc/5_5157/'
main_url='https://www.bqg5.cc'
rep = requests.get(url = mulu_url,headers=headers)
if rep.status_code==200:
    print('请求目录页成功！')
    mulu_html = etree.HTML(rep.text)
    mulu_array= mulu_html.xpath('//div[@class="box_con"]//dl/dd/a/@href')
    num = len(mulu_array)   #章节一共有多少章
for i in range(9,num):
    #rint('i='+str(i))
    xiazai_url = main_url+mulu_array[i]
    #print(xiazai_url)
    res = requests.get(url = xiazai_url,headers=headers)
    if res.status_code==200:
        print('请求成功!')
        print('正在下载',i-8)
        html = etree.HTML(res.text)
        data = html.xpath('/html/body/div[@id="wrapper"]/div[@class="content_read"]/div[@class="box_con"]/div[@id="content"]/p/text()')
        mystr = '\n'.join(data)
        #print(mystr)
        if i==9:
            with open('C:/Users/lsy/Desktop/蛊真人1.txt','w') as fp:
                fp.write(mystr)
        else:
            with open('C:/Users/lsy/Desktop/蛊真人1.txt','a') as fp:
                fp.write(mystr)
    else:
        print('请求失败！'+xiazai_url)