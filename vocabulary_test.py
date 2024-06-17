import random
import time
import os
import json

def main():
    directory = 'data_directory'
    file_path = os.path.join(directory, 'user_data.json')
    if not os.path.exists(directory):
        os.makedirs(directory)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            words_sentences = json.load(file)
    else:
        words_sentences = {}
    words_explaination = {}
    # user can choose which function they want to use, including inputting new words, having quiz and delete words
    function_option = input("Enter 1 to input new word. Enter 2 to take quizz. Enter 3 to delete word.: ")
    while function_option != "1" and function_option != "2": # make sure user only enter 1 or 2
        if function_option == "3":
            break
        print("Please enter 1 or 2 or 3")
        function_option = input("Enter 1 to input new word. Enter 2 to take quizz. Enter 3 to delete word.: ")
    if function_option == "1":
        input_new_words(words_sentences, words_explaination)
    elif function_option == "2":
        quiz_sentence(words_sentences)
    elif function_option == "3":
        delete_word(words_sentences)
    with open(file_path, 'w') as file:
        json.dump(words_sentences, file)
    
        

def input_new_words(words_sentences, words_explaination):
    # add pairs in dictionary. Words as keys; sentences as values.
    input_sentences = input("Please enter a sentence:")
    while input_sentences != "":
        input_words = input("Please enter the word from the sentence:").lower()
        while input_words != "":
            input_explaination = input("Your own explaination of the word in English:")
            words_sentences[input_words] = input_sentences
            words_explaination[input_words] = input_explaination
            print(input_words, ':', input_sentences)
            input_words = input("Enter another word from the sentence or press enter to next sentence:")
            if input_words == "":
                input_sentences = input("Enter another sentences or press enter to end:")

def quiz_sentence(words_sentences):
    # generate the question
    # choose a random key in dictionary and found its value to make a list. Compare list elements and keys to delete the word we want to test.
    while True:
        choose_words = random.choice(list(words_sentences.keys())) # random choose from keys of dictionary
        choose_sentence = words_sentences[choose_words]
        table = str.maketrans("", "", ",!.?") # remove all punctuation
        sentence_without_mark = choose_sentence.translate(table)
        lst_sentence = sentence_without_mark.split(" ")
        for i in range(len(lst_sentence)):
            elem = lst_sentence[i]
            if elem == choose_words:
                lst_sentence[i] = "____"
        question_sentence = " ".join(lst_sentence)
        print(question_sentence)
        # ask user to answer the question
        user_answer = input("Fill in the blank:").lower()
        if user_answer == "":
            break
        while user_answer.lower() != choose_words.lower():
            if user_answer != "":
                user_answer = input("Try again or press enter to see answer:")
            else:
                print(choose_sentence)
                user_answer = input("Try again:")
                
        print("You're right!", "{", choose_sentence, "}")
        time.sleep(0.8)
        print("")
        print("【Test again or press enter to exit】")

def delete_word(words_sentences):
    # delete words that have been inputted
    for key, value in words_sentences.items():
        print(str(key), ":", str(value))
    user_input = input("Please enter the word you want to delete:")
    while user_input != "":
        if user_input in words_sentences.keys(): # check input are valid
            del words_sentences[user_input]
            print("Successfully deleted!")
            print("All vocabularies:", list(words_sentences.keys()))
        else:
            print("There isn't a word '", user_input, " '")
        user_input = input("Enter the word you want to delete or press enter to exit:")
    


if __name__ == "__main__":
    main()