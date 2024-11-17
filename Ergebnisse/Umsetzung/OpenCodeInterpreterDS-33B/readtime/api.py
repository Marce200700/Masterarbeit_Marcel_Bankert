from .result import Result
from .utils import read_time, read_time_as_seconds, parse_html

def of_text(text, wpm=265):
    seconds = read_time_as_seconds(text, 0, wpm)
    return Result(seconds, wpm)

def of_html(html, wpm=265):
    text, images = parse_html(html)
    seconds = read_time_as_seconds(text, images, wpm)
    return Result(seconds, wpm)

def of_markdown(markdown, wpm=265):
    seconds = read_time(markdown, 'markdown', wpm)
    return Result(seconds, wpm)