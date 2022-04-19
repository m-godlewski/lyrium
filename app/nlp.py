"""
Script that contains classes responsible for NLP.
"""


import copy
import re
import string

import nltk
import pandas as pd
from textblob import TextBlob

from app.utills import POSMapper


class NLP:
    """Class that contains NLP methods."""

    # non-words strings that occurs in lyrics
    NON_WORDS_STRINGS = ("urlcopyembedcopy", "embedshare", "\u2026", "\u2019")

    # english stopwords
    STOPWORDS = set(nltk.corpus.stopwords.words("english"))

    @classmethod
    def text_process(cls, text: str) -> str:
        """Performs given text processing."""
        # making copy of given text
        processed_text = copy.deepcopy(text)
        # lowercasing text
        processed_text = processed_text.lower()
        # removing parts of strings in brackets
        processed_text = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", processed_text)
        # removing non-word parts of strings
        for non_word in cls.NON_WORDS_STRINGS:
            processed_text = processed_text.replace(non_word, "")
        # removing punctuation
        processed_text = processed_text.translate(str.maketrans("", "", string.punctuation))
        # removing digits
        processed_text = processed_text.translate(str.maketrans("", "", string.digits))
        # removing whitespaces and new line marks
        processed_text = processed_text.strip()
        processed_text = processed_text.replace("\n", " ")
        processed_text = re.sub(" +", " ", processed_text)
        return processed_text

    @classmethod
    def text_analyse(cls, text: str) -> dict:
        """Performs given text analysis.
        Returns dictionary that contains results of following analysis:
        - most common words.
        - part of speech frequency.
        - text sentiment analysis.
        """

        # analysis results dictionary
        results = {
            "mcw": {},
            "pos": {},
            "sentiment": {}
        }
        # making copy of given text
        analysed_text = copy.deepcopy(text)
        # lyrics tokenization
        text_tokenized = nltk.word_tokenize(analysed_text)
        # removing stopwords
        text_tokenized = [word for word in text_tokenized if word.casefold() not in cls.STOPWORDS]

        # MOST COMMON WORDS
        # creating pandas.Series object base on words list
        text_series = pd.Series(text_tokenized)
        # five most occuring words in analysed lyrics
        most_common_words = text_series.value_counts().head(5).to_dict()
        # assigning most common words and their occurences to results dictionary
        results["mcw"]["x"] = list(most_common_words.keys())
        results["mcw"]["y"] = list(most_common_words.values())

        # PART OF SPEECH FREQUENCY
        # creating pandas.DataFrame object with part of speech tags
        pos_series = pd.Series([word[1] for word in nltk.pos_tag(text_tokenized, tagset="universal")])
        # five most occuring part of speech tags
        pos_frequency = pos_series.value_counts().head(10).to_dict()
        # assigning part of speech tags and their occurences to results dictionary
        results["pos"]["x"] = list(pos_frequency.keys())
        results["pos"]["y"] = list(pos_frequency.values())
        results["pos"]["n"] = len(results["pos"]["y"])
        # maps part of speech tags to their longer versions
        results["pos"]["x"] = [POSMapper.map_pos_(tag=tag) for tag in results["pos"]["x"]]

        # TEXT SENTIMENT ANALYSIS
        # creating TextBlob object base on lyrics string
        lyrics_blob = TextBlob(text)
        # making text sentiment analysis
        text_sentiment = {
            "polarity": lyrics_blob.sentiment.polarity,
            "subjectivity": lyrics_blob.sentiment.subjectivity
        }
        # assigning text sentiment types and their values to results dictionary
        results["sentiment"]["x"] = list(text_sentiment.keys())
        results["sentiment"]["y"] = list(text_sentiment.values())

        return results
