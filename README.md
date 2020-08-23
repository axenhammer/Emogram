<h1 align="center">
  Emogram (Text Analysis for unstructured text)
</h1>

<p align="center">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/language-python-blue.svg?style=flat"></a>
  <a href="#"><img src="https://img.shields.io/github/last-commit/axenhammer/Emogram.svg"></a>
  <a href="/LICENSE.md"><img src="https://img.shields.io/github/license/axenhammer/Emogram.svg?color=blue"></a>
</p>

## Introduction
A small set of tools that'll normalize and extract values from unstructured text messages using concepts of NLP. Other Applications can use these modules to extract information and public opinions from Surveys, Social Networking sites, etc.


## Getting Started
### Prerequisites
What things you need to run the program:
- Python Compiler (3.7 Recommended)
- A clone of this repository :P
- Install all the necessary packages form pypi by using the following command:
 ```bash
pip install textblob
pip install spellchecker
```


## Functions
### Acronym Resolution
Expands acronyms that are present in the text as the first step of text normalization.

<img src="/docs/acronym_res.PNG" width="400" height="160"/>


### Key Phrases Extraction
Rapid Automatic Keyword Extraction (RAKE) algorithm to determine key phrases in a body of text by analyzing the frequency of word appearance and its co-occurance with other words in the text.

<img src="/docs/keyword_extract.PNG"/>


### Polarity Detection
Using TextBlob to detect Polarity of normalized text that ranges from -1 (Strongly Negative) to 1 (Strongly Positive).


### Auto Correct
Autocorrects misspelt words/typos present in the text as a part of text normalization.



## Authors
* **Krishna Alagiri** - [bearlike](https://github.com/bearlike/)
* **Vignesh S** - [Vignesh0404](https://github.com/Vignesh0404/)
* **Ajay Krishnan** - [ajaykrishnan23](https://github.com/ajaykrishnan23/)
* **Anan Mohamed** - [ananmohamed786](https://github.com/ananmohamed786/)
* **Shravan Deep** - [Shravandheep4](https://github.com/Shravandheep4/)


<br><br>
<p align="center">
  Made with ❤️ by <a href="https://github.com/axenhammer"> Axemhammer</a>
</p>

![wave](http://cdn.thekrishna.in/img/common/border.png)
