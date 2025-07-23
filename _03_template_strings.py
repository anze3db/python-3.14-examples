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
