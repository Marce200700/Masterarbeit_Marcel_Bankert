from readtime.result import Result
from bs4 import BeautifulSoup
from markdown2 import markdown
import re

def read_time(content, format, wpm):
    if format == 'text':
        return read_time_as_seconds(content, 0, wpm)
    elif format == 'html':
        soup = BeautifulSoup(content, 'lxml')
        text, images = parse_html(soup)
        return read_time_as_seconds(text, images, wpm)
    elif format == 'markdown':
        html = markdown(content)
        soup = BeautifulSoup(html, 'lxml')
        text, images = parse_html(soup)
        return read_time_as_seconds(text, images, wpm)

def read_time_as_seconds(text, images, wpm):
    words = len(re.findall(r'\w+', text))
    seconds = (words / wpm) * 60
    return Result(seconds)

def parse_html(el):
    text = el.get_text()
    images = el.find_all('img')
    return text, len(images)