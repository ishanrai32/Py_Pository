# -*- coding: utf-8 -*-
"""P2Q1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fNLVy4Lfbigrcro7SRrbe67BaKCCc3T6
"""

import numpy as np
import pandas as pd
import torch
import sys

!pip install transformers

data = pd.read_csv('review_data.csv')
data.dropna(inplace = True)

from transformers import GPT2Tokenizer, GPT2LMHeadModel
# Load pre-trained model (weights)
with torch.no_grad():
        model = GPT2LMHeadModel.from_pretrained('gpt2')
        model.eval()
# Load pre-trained model tokenizer (vocabulary)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
 
def score(sentence):
    tokenize_input = tokenizer.encode(sentence)
    tokenize_input = tokenize_input[0:1024]
    tensor_input = torch.tensor([tokenize_input])
    loss=model(tensor_input, labels=tensor_input)[0]
    return np.exp(loss.detach().numpy())

data['grammar_score'] = data['text'].apply(score)

data.to_csv('grammar_scores.csv')

from google.colab import files
files.download("grammar_scores.csv")

