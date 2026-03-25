import re

with open('index.html', 'r') as f:
    text = f.read()

text = text.replace('<h3 style={{color: \'var(--navy-primary)\'}}>\n              \n            <button type="button"',
                    '<h3 style={{color: \'var(--navy-primary)\'}}>\n<i className={mode===\'advance\'?\'fas fa-calendar-check\':\'fas fa-walking\'}></i> \n              {editRowIndex ? \' Edit Check-In\' : mode===\'advance\' ? \' Advance Booking Check-In\' : \' Walk-In Check-In\'}\n            </h3>\n<button type="button"')

with open('index.html', 'w') as f:
    f.write(text)
