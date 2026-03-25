import re

with open('index.html', 'r') as f:
    text = f.read()

# Let's verify that CheckInModal renders correctly. Oh, wait, look at the signature of CheckInModal:
# function CheckInModal({ initialMode, editCiRowIndex, activeCis, rooms, onClose, onRefresh }) {
# I see a 'loading' prop passed to SearchableSelect inside CheckInModal.
# Check SearchableSelect signature:
# function SearchableSelect({ value, onChange, options, placeholder, className, required, disabled }) {
# There is NO 'loading' prop in SearchableSelect.
