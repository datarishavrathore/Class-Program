

















data = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged.
"""

clean_text = ""

for ch in data:
    if ch.isalpha() or ch.isspace():
        clean_text += ch

with open("output.txt", "w") as file:
    file.write(clean_text)

print(clean_text)