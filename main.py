def main():
    with open("./books/frankenstein.txt") as f:
        file_contents=f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    words = file_contents.split()
    print(f"{len(words)} words found in the document")

    map={}
    for word in words:
        for letter in word:
            lower_letter = letter.lower()

            if lower_letter.isalpha() == False:
                continue

            if lower_letter in map:
                map[lower_letter] += 1
            else:
                map[lower_letter] = 1


    map = sorted(map.items(), key=lambda x: x[1], reverse=True)

    for (letter, count) in map:
        print(f"the '{letter}' character was found {count} times")

main()

