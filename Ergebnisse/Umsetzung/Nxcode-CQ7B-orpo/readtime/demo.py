from readtime import api

# Calculate reading time for a given text
text = "This is a sample text."
result = api.of_text(text, wpm=265)
print(result)
```

# Testing Design
The testing design is based on the pytest library. The test cases are stored in the `tests` directory. The test cases are written in the `test_api.py` file.

```python
import pytest
from readtime import api

def test_of_text():
    text = "This is a sample text."
    result = api.of_text(text, wpm=265)
    assert result.minutes() == 1.0

def test_of_html():
    html = "<html><body><p>This is a sample text.</p></body></html>"
    result = api.of_html(html, wpm=265)
    assert result.minutes() == 1.0

def test_of_markdown():
    markdown = "This is a sample text."
    result = api.of_markdown(markdown, wpm=265)
    assert result.minutes() == 1.0