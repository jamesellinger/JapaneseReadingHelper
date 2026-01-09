Goals/reasons/purpose for creating application: 
- built for my personal study of Japanese, but can be used for other languages
- 
- 

majority of the code written by Claude.ai (Sonnet 4.5)

tested in python 3.14 & ???

## Install

```
git clone https://github.com/jamesellinger/JapaneseReadingHelper.git
cd JapaneseReadingHelper
python -m venv env
pip install -r requirements.txt
```

## Run

From a terminal:
```
cd JapaneseReadingHelper
source env/bin/activate
python app.python
```

Open a web browser then navigate to the URL shown in the terminal (probably: http://127.0.0.1:5000 )

## Misc

Prompt is the same as the one used by the [Language Reactor](https://www.languagereactor.com) Netflix plugin:

```
Please explain the use of the word '{word}' in this sentence: {context}
```
