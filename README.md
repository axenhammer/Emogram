Emogram (Text Analysis for unstructured text)
============
[![Language](https://img.shields.io/badge/language-python-blue.svg?style=flat
)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/axenhammer/Emogram/blob/master/LICENSE)


A small set of tools that'll normalize and extract values from unstructured text messages using concepts of NLP. Other Applications can use these modules to extract information and public opinions from Surveys, Social Networking sites, etc.

## Functions
### Acronym Resolution
Expands acronyms that are present in the text as the first step of text normalization.

![Output](https://raw.githubusercontent.com/axenhammer/Emogram/master/docs/acronym_res.PNG)


### Auto Correct
Autocorrects misspelt words/typos present in the text as a part of text normalization.


### Key Phrases Extraction
Rapid Automatic Keyword Extraction (RAKE) algorithm to determine key phrases in a body of text by analyzing the frequency of word appearance and its co-occurance with other words in the text.

![Output](https://raw.githubusercontent.com/axenhammer/Emogram/master/docs/keyword_extract.PNG)


### Polarity Detection
Using TextBlob to detect Polarity of normalized text that ranges from -1 (Strongly Negative) to 1 (Strongly Positive).

### Installing Dependencies (using pip)
```bash
pip install textblob
pip install spellchecker
```
