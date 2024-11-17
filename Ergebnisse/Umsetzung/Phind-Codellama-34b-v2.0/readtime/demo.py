from readtime.api import of_text, of_html, of_markdown

text = "This is a sample text."
html = "<html><body><p>This is a sample html.</p></body></html>"
markdown = "This is a sample markdown."

print("Text reading time:", of_text(text))
print("HTML reading time:", of_html(html))
print("Markdown reading time:", of_markdown(markdown))
