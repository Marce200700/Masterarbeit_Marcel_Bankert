from readtime.result import Result
from readtime.utils import read_time

def of_text(text, wpm=265):
    return Result(read_time(text, 'text', wpm))

def of_html(html, wpm=265):
    return Result(read_time(html, 'html', wpm))

def of_markdown(markdown, wpm=265):
    return Result(read_time(markdown, 'markdown', wpm))