from urllib.request import Request, urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
from conf import settings


class Result:
    def __init__(self, url, title, snippet):
        self.url = url
        self.title = title
        self.snippet = snippet


def duck(query):
    url = 'https://duckduckgo.com/html/?q=' + quote(query) + '&kl=' + settings.gl_duck
    head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    req = Request(url, headers=head)
    page = urlopen(req)
    soup = BeautifulSoup(page, 'lxml')
    urls_raw = soup.find_all('a', {'class': 'result__url'})
    urls = ['https://' + url.text.strip() for url in urls_raw]
    titles_raw = soup.find_all('a', {'class': 'result__a'})
    titles = [title.text.strip() for title in titles_raw]
    snippets_raw = soup.find_all('a', {'class': 'result__snippet'})
    snippets = [snippet.text.strip() for snippet in snippets_raw]
    results = []

    for i in range(0, len(snippets)):
        results.append(Result(urls[i], titles[i], snippets[i]))

    return results


def bing(query):
    # url = 'https://www.bing.com/search?q=' + quote(query) + '&count=50'  # + '&cc=us'
    # url_first = 'https://www.bing.com/search?q=' + quote(query) + '&first=1' + '&count=1' + '&setLang=en-GB' + '&cc=en-GB'
    # url = 'https://www.bing.com/search?q=' + quote(query) + '&first=2' + '&count=50' + '&setLang=en' + '&cc=US'

    url_first = 'https://www.bing.com/search?q=' + quote(query) + '&first=1' + '&count=1' + '&mkt=en-CA'
    url = 'https://www.bing.com/search?q=' + quote(query) + '&first=2' + '&count=50' + '&mkt=en-CA'

    head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}

    req_first = Request(url_first, headers=head)
    req = Request(url, headers=head)

    page_first = urlopen(req_first)
    page = urlopen(req)

    soup_first = BeautifulSoup(page_first, 'lxml')
    soup = BeautifulSoup(page, 'lxml')

    first_entry = soup_first.find_all('li', {'class': 'b_algo'})
    entries = soup.find_all('li', {'class': 'b_algo'})

    urls = []
    urls.append(first_entry[0].a['href'])
    for url in entries:
        urls.append(url.a['href'])

    # urls = [url.a['href'] for url in entries]
    # titles = [entry.find('div', class_='ellip').text for entry in entries]

    titles = []

    try:
        titl = first_entry[0].find('a').text
    except Exception as e:
        titl = ''
    titles.append(titl)

    for j in range(0, len(entries)):
        try:
            # titl = entries[j].find('div', class_='b_title').text
            titl = entries[j].find('a').text
        except Exception as e:
            titl = ''
        titles.append(titl)

    snippets = []

    try:
        snip = first_entry[0].find('p').text
    except Exception as e:
        snip = ''
    snippets.append(snip)

    for i in range(0, len(entries)):
        try:
            # snip = entries[i].find('span', class_='st').text
            snip = entries[i].find('p').text
        except Exception as e:
            snip = ''
        snippets.append(snip)

    results = []

    for i in range(0, len(snippets)):
        results.append(Result(urls[i], titles[i], snippets[i]))

    if len(results) >= 10:
        return results
    else:
        return bing(query)


def google(query):
    url = 'https://www.google.com/search?q=' + quote(query) + '&hl=en' + '&num=100' + '&gl=' + settings.gl_google
    head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    req = Request(url, headers=head)
    page = urlopen(req)
    soup = BeautifulSoup(page, 'lxml')
    entries = soup.find_all('div', {'class': 'rc'})
    urls = [url.a['href'] for url in entries]

    # titles = [entry.find('div', class_='ellip').text for entry in entries]
    titles = []

    for j in range(0, len(entries)):
        try:
            # titl = entries[j].find('div', class_='ellip').text
            titl = entries[j].find('h3', class_='LC20lb').text
        except Exception as e:
            titl = ''
        titles.append(titl)

    snippets = []

    for i in range(0, len(entries)):
        try:
            snip = entries[i].find('span', class_='st').text
        except Exception as e:
            snip = ''
        snippets.append(snip)

    results = []

    for i in range(0, len(snippets)):
        results.append(Result(urls[i], titles[i], snippets[i]))

    return results
