from bs4 import BeautifulSoup
from markdown2 import markdown
from pyquery import PyQuery

def read_time(content, format, wpm):
    if format == 'markdown':
        content = markdown(content)
    words = content.split()
    return len(words) / wpm * 60

def read_time_as_seconds(text, images, wpm):
    words = text.split()
    return (len(words) + images) / wpm * 60

def parse_html(el):
    soup = BeautifulSoup(el, 'lxml')
    text = soup.get_text()
    images = len(soup.find_all('img'))
    return text, images