##  TODO: Implement the main function
def main():

    ##  TODO: Asks the user to type in some text
    text = get_text()

    ## TODO: Get the necessary variables
    words = get_words(text)
    print(words)
    letters = get_letters(text)
    print(letters)
    sentences = get_sentences(text)
    print(sentences)

    ## TODO: Outputs the grade level for the text
    grade = get_grade(words, letters, sentences)
    print(grade)

    if grade >= 16:
        print(f"Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")

def get_text():

    # TODO: Get the text
    text = str(input(("Text: ")))
    return text

def get_words(text):

    # TODO: Get the number of words
    text = text.split()
    words = len(text)
    return words

def get_letters(text):

    # TODO: Get the number of letters
    text = text.split()
    letters = 0
    for word in text:
        for letter in word:
            if letter in ".!?":
                letters += 0
            else:
                letters += 1
    return letters

def get_sentences(text):

    # TODO: Get the number of sentences
    sentences = text.count(".") + text.count("!") + text.count("?")
    return sentences

def get_grade(words, letters, sentences):

    ## TODO: Get L = the average number of letters per 100 words
    L = (letters / words) * 100

    ## TODO: Get S =  the average number of sentences per 100 words in the text
    S = (sentences / words) * 100

    ## TODO: Get Grade = 0.0588 * L - 0.296 * S - 15.8
    grade = 0.0588 * L - 0.296 * S - 15.8

    dec = float(f'{grade:.2f}') - int(grade)
    if dec >= 0.90:
        return round(grade)
    else:
        return grade

if __name__ == "__main__":
    main()