import re

with open('index.html', 'r') as f:
    text = f.read()

# Replace <SearchableSelect ... loading={advLd} /> with just removing loading
text = re.sub(r'loading={advLd}', '', text)

with open('index.html', 'w') as f:
    f.write(text)
