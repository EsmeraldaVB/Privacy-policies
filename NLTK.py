# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:29:50 2021

@author: esmer
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import nltk

nltk.download ('stopwords')
nltk.download ('punkt')

example_sent = "This is a sample sentence, showing off the stop words filtration."
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example_sent)

###################

from nltk.tokenize import sent_tokenize
text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_text=sent_tokenize(text)
print(tokenized_text)

#############



#Cookie analysis
#cookie text = text4

example_sent = "This is a sample sentence, showing off the stop words filtration."
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(text4)