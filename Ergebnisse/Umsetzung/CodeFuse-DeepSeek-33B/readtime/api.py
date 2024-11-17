from .result import Result
from .utils import read_time_as_seconds

def of_text(text, wpm=265):
    """
    Calculate the reading time of a given text.

    Parameters:
    text (str): The text to calculate the reading time for.
    wpm (int): The words per minute rate to use for the calculation.

    Returns:
    Result: The estimated reading time in seconds.
    """
    seconds = read_time_as_seconds(text, 0, wpm)
    return Result(seconds, wpm)

def of_html(html, wpm=265):
    """
    Calculate the reading time of an HTML document.

    Parameters:
    html (str): The HTML document to calculate the reading time for.
    wpm (int): The words per minute rate to use for the calculation.

    Returns:
    Result: The estimated reading time in seconds.
    """
    seconds = read_time_as_seconds(html, 0, wpm)
    return Result(seconds, wpm)

def of_markdown(markdown, wpm=265):
    """
    Calculate the reading time of a markdown text.

    Parameters:
    markdown (str): The markdown text to calculate the reading time for.
    wpm (int): The words per minute rate to use for the calculation.

    Returns:
    Result: The estimated reading time in seconds.
    """
    seconds = read_time_as_seconds(markdown, 0, wpm)
    return Result(seconds, wpm)