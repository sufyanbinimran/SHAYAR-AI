import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

def load_resources():
    model = load_model("shairimodel.keras")
    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    return model, tokenizer

def generate_shair(seed_word, num_shair, model, tokenizer, max_seq_length, temperature=0.8):
    shairi = set()
    num_lines = num_shair * 2
    context_words = seed_word.split()
    
    while len(shairi) < num_lines:
        seed_text = " ".join(context_words)
        words = seed_text.split()
        while len(words) < 8:
            sequence = tokenizer.texts_to_sequences([seed_text])[0]
            sequence = pad_sequences([sequence], maxlen=max_seq_length - 1, padding='pre')
            predictions = model.predict(sequence, verbose=0)[0]
            predictions = np.log(predictions + 1e-8) / temperature
            exp_preds = np.exp(predictions)
            probabilities = exp_preds / np.sum(exp_preds)
            next_index = np.random.choice(len(probabilities), p=probabilities)
            next_word = tokenizer.index_word.get(next_index, "")
            if next_word:
                position = np.random.randint(0, len(words) + 1)
                words.insert(position, next_word)
                seed_text = " ".join(words)
        shairi.add(seed_text)
    
    return "\n\n".join(list(shairi)[:num_lines])

st.set_page_config(page_title="Poetry Generator", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #eae7dc;
        font-family: 'Georgia', serif;
    }
    .main-container {
        background: #fefefe;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 3px 3px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    .stTextInput, .stSlider, .stButton {
        font-size: 18px;
        color: #333;
    }
    textarea {
        font-family: 'Georgia', serif;
        font-size: 20px;
        background-color: #f7f5f2;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #d3c6a8;
    }
    h1 {
        color: #5d4037;
        font-size: 34px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("✨ SHAYAR AI ✨")

st.write("Generate beautiful poetry with a single word.")

model, tokenizer = load_resources()
max_seq_length = model.input_shape[1] + 1

seed_word = st.text_input("Enter a starting word (e.g., dil, pyar, ishq):", "ishq")
num_shair = st.slider("Select number of couplets (Each has 2 lines)", 1, 5, 2)

if st.button("🌿 Generate Poetry 🌿"):  
    poetry = generate_shair(seed_word, num_shair, model, tokenizer, max_seq_length)
    st.text_area("📜 Your Poetry:", poetry, height=200)

st.markdown("</div>", unsafe_allow_html=True)
