import sys
import pandas as pd
import tensorflow as tf
from utils.build_data import data_set
from utils.process_data import word_tokens, padded_sequences, normalize_numbers
from utils.predictions import load_h5_file, predict_number, predict_word

# Create a DataFrame
data = pd.DataFrame(data_set(["num_words.json","numbers.json"]))
print(data.head())

# Step 2: Processing the Data
# Tokenize the words
tokenizer, word_to_sequence = word_tokens(data)

# # Convert words to sequences

sequences, word_index = word_to_sequence(data)

max_length, padded_seq = padded_sequences(sequences)

# Normalize numbers (we'll use the numbers as is for simplicity)
normalized_numbers = normalize_numbers(data)

print(padded_seq[:5])
print(normalized_numbers[:5])

# Step 3: Load the Saved Model
model = load_h5_file('number_word.h5')

# Terminal application
def main():
    print("Number to Word translator \n")
    print("Enter a number or word between 1 and 1000 to predict.")
    print("Press Ctrl + C to exit.")
    
    while True:
        try:
            user_input = input("Enter number or word: ")
            
            if user_input.isdigit():
                number = int(user_input)
                result = predict_word(number, normalized_numbers, data)
                print(f"The word for {number} is '{result}'.")
            else:
                word = user_input.strip()
                result = predict_number(word,tokenizer, max_length, model)
                print(f"The number for '{word}' is '{result}'.")
        
        except KeyboardInterrupt:
            print("\nExiting the program.")
            sys.exit()

if __name__ == "__main__":
    main()