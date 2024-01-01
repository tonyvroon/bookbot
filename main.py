filename = "books/frankenstein.txt"
with open(filename) as f:
    file_contents = f.read()
    print(file_contents)
    words = len(file_contents.split())
    characters = dict()
    for x in file_contents.lower():
        characters[x] = characters.get(x, 0) + 1

    charcount = list()
    for character, count in characters.items():
        if character.isalpha():
            charcount.append([character,count])
    charcount.sort(key=lambda x: x[1], reverse=True)
     
    print(f"--- Begin report of {filename} ---")
    print(f"{words} words found in the document")
    print()
    for data in charcount:
        print(f"The '{data[0]}' character was found {data[1]} times")

    print("--- End report ---")
