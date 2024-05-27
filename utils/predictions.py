"""Make Predictions of number to word and word to number for numbers between 1 and 1000"""

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


def load_h5_file(file_path):
    """Load the saved model"""
    model = load_model(file_path)
    return model

def predict_number(word, tokenizer, max_length, model):
    seq = tokenizer.texts_to_sequences([word])
    padded = pad_sequences(seq, maxlen=max_length, padding='post')
    
    pred = model.predict(padded)
    return pred[0][0]

def predict_word(number, normalized_numbers, data):
    idx = (abs(normalized_numbers - number)).argmin()
    return data['word'].iloc[idx]