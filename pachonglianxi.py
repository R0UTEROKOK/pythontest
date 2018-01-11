
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from lxml import etree
import time
import json


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "DNT": "1",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "dywez=95841923.1512036182.1.1.dywecsr=google.com.sg|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/; LastCity=%e5%8c%97%e4%ba%ac; LastCity%5Fid=530; JSSearchModel=0; LastJobTag=%e4%ba%94%e9%99%a9%e4%b8%80%e9%87%91%7c%e5%b8%a6%e8%96%aa%e5%b9%b4%e5%81%87%7c%e9%a4%90%e8%a1%a5%7c%e8%8a%82%e6%97%a5%e7%a6%8f%e5%88%a9%7c%e5%ae%9a%e6%9c%9f%e4%bd%93%e6%a3%80%7c%e8%a1%a5%e5%85%85%e5%8c%bb%e7%96%97%e4%bf%9d%e9%99%a9%7c%e5%b9%b4%e5%ba%95%e5%8f%8c%e8%96%aa%7c%e7%bb%a9%e6%95%88%e5%a5%96%e9%87%91%7c%e4%ba%a4%e9%80%9a%e8%a1%a5%e5%8a%a9%7c%e9%80%9a%e8%ae%af%e8%a1%a5%e8%b4%b4%7c%e6%88%bf%e8%a1%a5%7c%e5%91%98%e5%b7%a5%e6%97%85%e6%b8%b8%7c%e5%85%8d%e8%b4%b9%e7%8f%ad%e8%bd%a6%7c%e5%bc%b9%e6%80%a7%e5%b7%a5%e4%bd%9c%7c%e5%8a%a0%e7%8f%ad%e8%a1%a5%e5%8a%a9%7c%e5%85%a8%e5%8b%a4%e5%a5%96%7c%e8%82%a1%e7%a5%a8%e6%9c%9f%e6%9d%83%7c%e5%8c%85%e5%90%83%7c%e9%ab%98%e6%b8%a9%e8%a1%a5%e8%b4%b4%7c%e5%b9%b4%e7%bb%88%e5%88%86%e7%ba%a2%7c%e9%87%87%e6%9a%96%e8%a1%a5%e8%b4%b4%7c%e5%8c%85%e4%bd%8f%7c%e6%af%8f%e5%b9%b4%e5%a4%9a%e6%ac%a1%e8%b0%83%e8%96%aa%7c14%e8%96%aa%7c%e5%88%9b%e4%b8%9a%e5%85%ac%e5%8f%b8%7c%e4%b8%8d%e5%8a%a0%e7%8f%ad%7c%e5%81%a5%e8%ba%ab%e4%bf%b1%e4%b9%90%e9%83%a8%7c%e4%bd%8f%e6%88%bf%e8%a1%a5%e8%b4%b4%7c%e5%85%8d%e6%81%af%e6%88%bf%e8%b4%b7%7c%e6%97%a0%e8%af%95%e7%94%a8%e6%9c%9f; LastSearchHistory=%7b%22Id%22%3a%224c63e319-1c41-4d05-98be-1e49f80b4d17%22%2c%22Name%22%3a%22%e4%bf%a1%e6%81%af%e5%ae%89%e5%85%a8%e5%b7%a5%e7%a8%8b%e5%b8%88+%2b+%e5%8c%97%e4%ba%ac%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e5%258c%2597%25e4%25ba%25ac%26kw%3d%25e4%25bf%25a1%25e6%2581%25af%25e5%25ae%2589%25e5%2585%25a8%25e5%25b7%25a5%25e7%25a8%258b%25e5%25b8%2588%26sm%3d0%26sg%3dbb86eea0f7114efaa2be05e4f5c76859%26p%3d8%22%2c%22SaveTime%22%3a%22%5c%2fDate(1512037191605%2b0800)%5c%2f%22%7d; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; adfbid=0; adfbid2=0; dywea=95841923.1061578720936527700.1512036182.1512036182.1512036182.1; dywec=95841923; dyweb=95841923.7.9.1512036195609; __utma=269921210.651373671.1512036182.1512036182.1512036182.1; __utmb=269921210.7.9.1512036195612; __utmc=269921210; __utmz=269921210.1512036182.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); Hm_lvt_38ba284938d5eddca645bb5e02a02006=1512036182; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1512037224"
}


def match_class(target):
    def do_match(tag):
        classes = tag.get('class', [])
        return all(c in classes for c in target)
    return do_match


x = PrettyTable(["title", "company", "wages",
                 "workplace", "academic", "experience", "category", "desc"])
url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8%E5%B7%A5%E7%A8%8B%E5%B8%88&p={0}"
session = requests.session()
for i in range(1, 2):
    page = session.get(url.format(i), headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    tables = soup.find_all(match_class(["newlist"]))
    print(tables[0:1])
    for table in tables[1:8]:
        zwmc = table.find_all(match_class(["zwmc"]))[0].text.strip()
        print(zwmc)
        url_zw = table.find_all(match_class(["zwmc"]))[
            0].find('a').attrs['href']
        gsmc = table.find_all(match_class(["gsmc"]))[0].text.strip()
        zwyx = table.find_all(match_class(["zwyx"]))[0].text.strip()
        gzdd = table.find_all(match_class(["gzdd"]))[0].text.strip()
        time.sleep(0.5)
        page = session.get(url_zw, headers=headers)
        html = etree.fromstring(page.text, parser=etree.HTMLParser())
        academic = html.xpath(
            '/html/body/div[6]/div[1]/ul/li[6]/strong')[0].text
        experience = html.xpath(
            '/html/body/div[6]/div[1]/ul/li[5]/strong')[0].text
        category = html.xpath(
            '/html/body/div[6]/div[1]/ul/li[8]/strong/a')[0].text
        desc = BeautifulSoup(page.text, 'lxml').find(
            'div', {'class': 'tab-inner-cont'}).text.strip()[:100]
        x.add_row([zwmc,gsmc, zwyx, gzdd,academic, experience,category, desc])

print (x)



