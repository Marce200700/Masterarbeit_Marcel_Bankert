from readtime import api

def main():
    text = "Your text here"
    html = "<html><body>Your HTML here</body></html>"
    markdown = "Your markdown here"
    wpm = 265

    result_text = api.of_text(text, wpm)
    result_html = api.of_html(html, wpm)
    result_markdown = api.of_markdown(markdown, wpm)

    print(f"Text: {result_text}")
    print(f"HTML: {result_html}")
    print(f"Markdown: {result_markdown}")

if __name__ == "__main__":
    main()