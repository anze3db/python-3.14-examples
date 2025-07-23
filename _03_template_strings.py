from html import escape
from string.templatelib import Interpolation, Template

name = "World"
greeting: Template = t"Hello, {name}!"

string = []
for item in greeting:
    if isinstance(item, Interpolation):
        string.append(item.value)
    else:
        string.append(item)

print("".join(string))

# python3.14 _03_template_strings.py
