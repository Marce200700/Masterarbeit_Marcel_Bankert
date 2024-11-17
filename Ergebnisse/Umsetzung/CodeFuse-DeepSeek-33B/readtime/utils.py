from bs4 import BeautifulSoup
from markdown2 import markdown
from pyquery import PyQuery

def read_time(content, format, wpm=265):
    """
    Calculate the estimated reading time for the given content.

    Parameters:
    content (str): The content to calculate the reading time for.
    format (str): The format of the content (plain_text, html, or markdown).
    wpm (int): The words per minute rate to use for the calculation.

    Returns:
    Result: The estimated reading time in seconds.
    """
    if format == "plain_text":
        return read_time_as_seconds(content, 0, wpm)
    elif format == "html":
        return read_time_as_seconds(content, 0, wpm)
    elif format == "markdown":
        return read_time_as_seconds(markdown(content), 0, wpm)
    else:
        raise ValueError("Unsupported format")

def read_time_as_seconds(text, images, wpm):
    """
    Calculate the estimated reading time in seconds for a given text.

    Parameters:
    text (str): The text to calculate the reading time for.
    images (int): The number of images in the text.
    wpm (int): The words per minute rate to use for the calculation.

    Returns:
    int: The estimated reading time in seconds.
    """
    word_count = len(text.split())
    image_count = images
    total_words = word_count + image_count * 100
    return total_words / wpm * 60

def parse_html(el):
    """
    Parse an HTML element and extract text and image information.

    Parameters:
    el (str): The HTML element to parse.

    Returns:
    tuple: A tuple containing the text and image count of the element.
    """
    soup = BeautifulSoup(el, "html.parser")
    text = soup.get_text()
    images = len(soup.find_all("img"))
    return text, images