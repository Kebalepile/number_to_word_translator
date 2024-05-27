# import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
def word_tokens(data):
    """Tokeniz the words"""
    
    # Ensure 'data' contains the key 'word'
    if "word" not in data:
        raise ValueError("The data dictionary must contain the key 'word'")

    
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(data["word"])
     
    # Convert words to sequences
    def word_to_sequence(data):
        """Convert words to sequences"""
        
        # Ensure 'data' contains the key 'word'
        if "word" not in data:
            raise ValueError("The data dictionary must contain the key 'word'")

        
        sequences = tokenizer.texts_to_sequences(data['word'])
        word_index = tokenizer.word_index
        return sequences, word_index
    
    return tokenizer, word_to_sequence

def padded_sequences(sequences):
    """pad sequnces"""
    max_length = max(len(seq) for seq in sequences)
    padded_seq = pad_sequences(sequences, maxlen=max_length, padding='post')
    
    return max_length, padded_seq


def normalize_numbers(data):
    """Normalize numbers (we'll use the numbers as is for simplicity)"""
   
    return data["number"].values
    