from gingerit.gingerit import GingerIt

def correct_and_count_words(sentence):
    # Use GingerIt to parse and correct the input sentence
    parsed_result = GingerIt().parse(sentence)
    
    # Extract the corrected text from the GingerIt result
    corrected_text = parsed_result['result']
    
    # Count the number of words in the original and corrected sentences
    original_word_count = len(sentence.split())
    corrected_word_count = len(corrected_text.split())
    
    # Print the original and corrected sentences along with word counts
    print(f"Original Sentence: {sentence}")
    print(f"Corrected Sentence: {corrected_text}")
    print(f"Original Word Count: {original_word_count}")
    print(f"Corrected Word Count: {corrected_word_count}")

# Take user input for a sentence
user_sentence = input("Enter a sentence >>: ")

# Call the function to correct and count words in the sentence
correct_and_count_words(user_sentence)
