import requests
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlparse


def crawInfo(url):
    data = requests.get(url)
    if data.status_code is 200:
        html = bs4(data.text, 'html.parser')
        dic_info = {}
        for item in (html.find('head', {'id': 'ctl00_header'})).findAll('title'):
            dic_info['title'] = item.text.strip()
            
        dic_info['url'] = url
        dic_info['author'] = (html.find('span', {'id': 'ctl00_mobile_newsdetail_Lbl_Author'})).text
        dic_info['date'] = (html.find('span', {'id': 'ctl00_mobile_newsdetail_lblCreateDate'})).text
        return dic_info
    else:
        raise(":: could not reach url")


def listAll(url):
    data = requests.get(url)
    if data.status_code is 200:
        # from urlparse import urlparse  # Python 2
        parsed_uri = urlparse(url)
        main_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        html = bs4(data.text, 'html.parser')
        list_urls = [url]
        for item in html.findAll('div', attrs = {'class':'Item1'}):
            for a_elm in item.find_all("a", attrs = {'class':'NOtherTitle'}):
                sub_url = main_url[:-1] + a_elm.attrs["href"]
                list_urls.append(sub_url)
        return list_urls
    else:
        raise(":: could not reach url")


if __name__ == "__main__":
    url = 'https://www.thesaigontimes.vn/121624/Cuoc-cach-mang-dau-khi-da-phien.html'

    list_data = []
    for url in listAll(url):
        data = crawInfo(url)
        list_data.append(data)

    if len(list_data) > 0:
        print("URL,Title,Author,Date")
        for data in list_data:
            print("{},{},{},{}".format(
                data.get('url'),
                data.get('title'),
                data.get('author'),
                data.get('date')
            ))
