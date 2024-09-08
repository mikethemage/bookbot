def output_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def number_of_words(text):
    words = text.split()
    return len(words)

def count_words():
     with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return number_of_words(file_contents)

def sort_on(dict):
            return dict["Count"]

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(f"{number_of_words(file_contents)} words found in the document")
        print()

        file_contents = file_contents.lower()
        letterdict = dict()
        for letter in file_contents:
            currentcount = letterdict.setdefault(letter, 0)
            letterdict.update({letter: currentcount + 1})

        resultList = []
        # traversing through each key value pair of a dictionary using items() function
        for key, val in letterdict.items():
            # appending list of corresponding key-value pair to a list
            if key.isalpha():
                resultList.append({"Letter": key, "Count": val})           
        
        resultList.sort(reverse=True, key=sort_on)

        for result in resultList:
            print(f"The '{result['Letter']}' character was found {result['Count']} times")


main()