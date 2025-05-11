# Unique Character Finder

This project contains a Python function that finds all unique characters in a string. A unique character is defined as one that appears only once in the given string. 

## Functionality:
- The function iterates over the string, adding each character to a set if it appears for the first time and removing it if it appears again.
- The final result is a set of characters that appear only once in the string.

## Example:

```python
def uniqueCharacterFinder(text):
    uniqueChar = set()
    for ch in text:
        if ch in uniqueChar:
            uniqueChar.remove(ch)
        else:
            uniqueChar.add(ch)
    return uniqueChar

# Example usage
print(uniqueCharacterFinder("alii"))  # Output: {'a', 'i'}

```

#### © 2025, All rights reserved. Developed by Ho3ein Tahan