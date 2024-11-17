from readtime import of_text, of_html, of_markdown

def main():
    text = "This is a sample text."
    html = "<p>This is a sample text.</p>"
    markdown = "# This is a sample text."

    print(of_text(text).text())
    print(of_html(html).text())
    print(of_markdown(markdown).text())

if __name__ == "__main__":
    main()