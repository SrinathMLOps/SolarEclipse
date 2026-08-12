#!/usr/bin/env python3
# Scan for remaining garbled sequences and show their byte patterns

file = r"C:\Users\SRINATH\Desktop\SolarEclipse\index.html"

with open(file, 'rb') as f:
    data = f.read()

text = data.decode('utf-8')

import re
# Find sequences that look like mojibake: non-ASCII chars that aren't real emojis
# Pattern: sequences of characters in latin-1 extended range that shouldn't be there
# Look for common mojibake markers

# Find all occurrences of â, ã, ð, Ã, Â etc followed by other odd chars
pattern = re.compile(r'[âãðÃÂ][^\x00-\x7F\s<>&"=]{1,8}')
matches = set(pattern.findall(text))

print("Remaining garbled sequences:")
for m in sorted(matches):
    try:
        b = m.encode('utf-8')
        print(f"  Text: {repr(m)}")
        print(f"  Bytes: {b.hex()}")
        # Try to recover
        try:
            recovered = m.encode('latin-1').decode('utf-8')
            print(f"  -> Recovered: {recovered} ({repr(recovered)})")
        except:
            pass
        print()
    except Exception as e:
        print(f"  Error: {e}")

# Also show context for lines with garbled text
print("\n--- Lines with garbled content ---")
for i, line in enumerate(text.split('\n'), 1):
    if re.search(r'[âãðÃÂ][^\x00-\x7F\s<>&"=]', line):
        stripped = line.strip()
        if len(stripped) > 5 and not stripped.startswith('//') and 'rgba' not in stripped:
            print(f"Line {i}: {stripped[:120]}")
