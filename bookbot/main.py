def main():
    with open("/Users/emingani/workspace/github.com/Plymouther/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        count = word_count(file_contents)
        print(f"--- Begin report of books/frankenstein.txt---")
        char_count = character_count(file_contents)
        
        print(f"{count} words found in the document")
        print("Character count:")
        print_formatted_character_count(char_count)

def word_count(file_contents):
    words = file_contents.split()  
    return len(words)

def character_count(file_contents):
    counter = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}
    for char in file_contents.lower():
        if char in counter:  
            counter[char] += 1       
    return counter

def print_formatted_character_count(counter):
    items = list(counter.items())

    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j][1] < items[j + 1][1]: 
                items[j], items[j + 1] = items[j + 1], items[j] 

    for char, count in items:
        print(f"The '{char}' character was found {count} times")

main()
