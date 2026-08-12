#!/usr/bin/env python3
# Complete fix for all garbled sequences

file = r"C:\Users\SRINATH\Desktop\SolarEclipse\index.html"

with open(file, 'rb') as f:
    data = f.read()

replacements = [
    # ⏸ (U+23F8) - â¸ (partial) 
    (b'\xc3\xa2\xc2\x8f\xc2\xb8', '⏸'.encode('utf-8')),
    # 🔴 (U+1F534)
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9d\xc2\xb4', '🔴'.encode('utf-8')),
    # 🔭 (U+1F52D)
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9d\xc2\xad', '🔭'.encode('utf-8')),
    # 🔬 (U+1F52C)
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9d\xc2\xac', '🔬'.encode('utf-8')),
    # 🔍 (U+1F50D) - search/zoom
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9d\xc2\x8d', '🔍'.encode('utf-8')),
    # 🔐 (U+1F510)
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9d\xc2\x90', '🔐'.encode('utf-8')),
    # 🔺 (U+1F53A)
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9d\xc2\xba', '🔺'.encode('utf-8')),
    # 📍 (U+1F4CD) - map pin used for location icon
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9c\xc2\x8d', '📍'.encode('utf-8')),
    # 🌑 (U+1F311)
    (b'\xc3\xb0\xc5\xb8\xc5\x92\xe2\x80\x98', '🌑'.encode('utf-8')),
    # 🌍 (U+1F30D)
    (b'\xc3\xb0\xc5\xb8\xc5\x92\xc2\x8d', '🌍'.encode('utf-8')),
    # 🕐 (U+1F550) - clock
    (b'\xc3\xb0\xc5\xb8\xe2\x80\xa2\xc2\x90', '🕐'.encode('utf-8')),
    # 📺 (U+1F4FA) - TV
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9c\xc2\xba', '📺'.encode('utf-8')),
    # 🇮🇸 (Iceland flag - regional indicator I+S)
    (b'\xc3\xb0\xc5\xb8\xe2\x80\xa1\xc2\xae\xc3\xb0\xc5\xb8\xe2\x80\xa1\xc2\xb8', '🇮🇸'.encode('utf-8')),
    # 🇬🇧 (UK flag)
    (b'\xc3\xb0\xc5\xb8\xe2\x80\xa1\xc2\xac\xc3\xb0\xc5\xb8\xe2\x80\xa1\xc2\xa7', '🇬🇧'.encode('utf-8')),
    # 🇪🇸 (Spain flag)
    (b'\xc3\xb0\xc5\xb8\xe2\x80\xa1\xc2\xaa\xc3\xb0\xc5\xb8\xe2\x80\xa1\xc2\xb8', '🇪🇸'.encode('utf-8')),
    # ✓ checkmark
    (b'\xc3\xa2\xc5\x93\xe2\x80\x9c', '✓'.encode('utf-8')),
    # ó (Gijón)
    (b'\xc3\x83\xc2\xb3', 'ó'.encode('utf-8')),
]

count = 0
for bad, good in replacements:
    if bad in data:
        n = data.count(bad)
        data = data.replace(bad, good)
        count += n
        print(f"Replaced {n}x: -> {good.decode('utf-8')}")

print(f"\nTotal: {count} replacements")

# Also handle the remaining ðŸ sequences that weren't caught - 
# try to auto-fix remaining ð patterns by decoding their bytes
import re

text = data.decode('utf-8')

# Find remaining garbled sequences
garbled = re.findall(r'[ðÃ][^\x00-\x7F\s<>&"=\-+]{1,10}', text)
remaining = set(garbled)
if remaining:
    print(f"\nStill garbled ({len(remaining)} unique):")
    for g in sorted(remaining)[:20]:
        print(f"  {repr(g)} -> bytes: {g.encode('utf-8').hex()}")
else:
    print("\n✓ No more garbled sequences!")

with open(file, 'wb') as f:
    f.write(data)
print("\nSaved.")

# Show final sample
body_idx = text.find('<body>')
print("\nFinal sample:")
print(text[body_idx:body_idx+400])
