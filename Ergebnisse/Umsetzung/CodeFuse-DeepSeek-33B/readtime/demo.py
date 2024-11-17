from readtime import api

# Read the content from a file
with open('./samples/plain_text.txt', 'r') as f:
    content = f.read()

# Calculate the reading time
reading_time = api.of_text(content, wpm=265)

# Print the result
print(f"Reading time: {reading_time}")