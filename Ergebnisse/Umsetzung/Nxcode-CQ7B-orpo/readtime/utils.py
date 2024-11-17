from bs4 import BeautifulSoup
import markdown2
import re

def read_time(content, format, wpm):
    if format == 'text':
        return Result(read_time_as_seconds(content, 0, wpm), wpm)
    elif format == 'html':
        return Result(read_time_as_seconds(parse_html(BeautifulSoup(content, 'lxml'))[0], parse_html(BeautifulSoup(content, 'lxml'))[1], wpm), wpm)
    elif format == 'markdown':
        return Result(read_time_as_seconds(markdown2.markdown(content), 0, wpm), wpm)
    else:
        raise ValueError("Unsupported format")

def read_time_as_seconds(text, images, wpm):
    words = len(text.split())
    return (words + images) / wpm * 60

def parse_html(el):
    text = el.get_text()
    images = len(el.find_all('img'))
    return text, images