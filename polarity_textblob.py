#!/usr/bin/python3
# Polarity Detection of Normalised Text
# Created by Team Axenhammer, https://github.com/Axenhammer
# Licensed as MIT

import re, os, shutil, sys
from textblob import TextBlob

def main():
    num = 0
    Input_String = sys.argv[1]

    # For Splitting Paragraphs into List of Sentences
    products = Input_String.split(".")
    postive = 0
    negative = 0
    print("Polarity ranges from (-1 -> 1)")
    for product in products:
        product = product.strip()
        if (product != ""):
            blob = TextBlob(product)
            Polarity = float(blob.sentiment.polarity)
            print("\"" + product + "\" -> ", Polarity)
            if (Polarity > 0):
                if (Polarity < 0.5):
                    print("Emotion: Mildly Positive")
                else:
                    print("Emotion: Strongly Positive")

            elif (Polarity < 0):
                Polarity = (-1)*Polarity
                if (Polarity < 0.5):
                    print("Emotion: Mildly Negative")
                else:
                    print("Emotion: Strongly Negative")

            else:
                print("Emotion: Impassive")
            num += 1


if __name__ == '__main__':
    main()
