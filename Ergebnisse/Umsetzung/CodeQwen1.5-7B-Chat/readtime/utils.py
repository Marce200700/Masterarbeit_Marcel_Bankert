from bs4 import BeautifulSoup
import markdown2
import pyquery

def read_time(content, format, wpm):
    if format == 'text':
        return read_time_as_seconds(content, 0, wpm)
    elif format == 'html':
        return read_time_as_seconds(parse_html(BeautifulSoup(content, 'lxml')), 0, wpm)
    elif format == 'markdown':
        return read_time_as_seconds(markdown2.markdown(content), 0, wpm)
    else:
        raise ValueError("Unsupported format")

def read_time_as_seconds(text, images, wpm):
    words = text.split()
    return len(words) / wpm * 60

def parse_html(el):
    pq = pyquery.PyQuery(el)
    text = pq.text()
    images = len(pq('img'))
    return text, images