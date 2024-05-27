import pandas as pd
import tensorflow as tf
from utils.build_data import data_set
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Step 1: Data Preparation
# Create a DataFrame
data = pd.DataFrame(data_set("num_words.json"))
print(data.head())

# Step 2: Processing the Data

# Tokenize the words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(data['word'])

# Convert words to sequences
sequences = tokenizer.texts_to_sequences(data['word'])
word_index = tokenizer.word_index

# Pad sequences
max_length = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

# Normalize numbers (we'll use the numbers as is for simplicity)
normalized_numbers = data['number'].values

print(padded_sequences[:5])
print(normalized_numbers[:5])

# Step 3 Build the Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Define the model
model = Sequential([
    Embedding(input_dim=len(word_index) + 1, output_dim=64, input_length=max_length),
    LSTM(128),
    Dense(1, activation='linear')  # Output is a single number
])

model.compile(optimizer='adam', loss='mean_squared_error')

model.summary()

# Step 4 Train the Model
# Train the model
model.fit(padded_sequences, normalized_numbers, epochs=50, batch_size=16)


# Step 5 Make Predictions
def predict_number(word):
    seq = tokenizer.texts_to_sequences([word])
    padded = pad_sequences(seq, maxlen=max_length, padding='post')
    pred = model.predict(padded)
    return pred[0][0]

def predict_word(number):
    idx = (abs(normalized_numbers - number)).argmin()
    return data['word'].iloc[idx]

# Examples
print("\n--------------------------------\n")
num = predict_number("twenty")
print(f"{num:.0f}")  # Should be close to 20
print(predict_word(25))  # Should be "twenty-five"
print("\n--------------------------------\n")
num = predict_number("one hundred thirty-seven")
print(f"{num:.0f}")   # Should be close to 137
print(predict_word(137))  # Should be "one hundred thirty-seven"
print("\n--------------------------------\n")

# Save the model in HDF5 format
model.save('number_word.h5')
# Download the model file
# files.download('number_word.h5')
