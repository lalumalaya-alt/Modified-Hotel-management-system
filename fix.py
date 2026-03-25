import re

with open('index.html', 'r') as f:
    text = f.read()

text = text.replace('loading={advLd}', '')

with open('index.html', 'w') as f:
    f.write(text)
