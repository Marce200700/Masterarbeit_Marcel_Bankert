from readtime import utils

def of_text(text, wpm):
    return utils.read_time(text, 'text', wpm)

def of_html(html, wpm):
    return utils.read_time(html, 'html', wpm)

def of_markdown(markdown, wpm):
    return utils.read_time(markdown, 'markdown', wpm)
