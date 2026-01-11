Goals/reasons/purpose for creating application: built for my personal study of Japanese, but can be used for other languages.

- uses OpenRouter and sends request to OpenAI for AI-assisted reading
- uses DeepL for translation

Ways to use:

1.  Open a visual novel and hook the text with [Textractor](https://github.com/Artikash/Textractor) or [newer branch](https://github.com/Chenx221/Textractor). Text is sent via websocket using the [Textractor Websocket plugin](https://github.com/kuroahna/textractor_websocket).
2. Simply copy-and-paste text into the 'Input' field.

Instructions for use are displayed once the application is running.

A majority of the code was written by Claude.ai (Sonnet 4.5)

Tested in python 3.12 & 3.14  


## Install

From a terminal:

```
git clone https://github.com/jamesellinger/JapaneseReadingHelper.git

cd JapaneseReadingHelper

python -m venv env

pip install -r requirements.txt
```

Open ```settings.ini``` and add API keys for OpenRouter and DeepL.

## Run

From a terminal:
```
cd JapaneseReadingHelper

source env/bin/activate

python app.python
```

Open a web browser then navigate to the URL shown in the terminal (probably: `http://127.0.0.1:5000`)

## Misc

Prompt is the same as the one used by the [Language Reactor](https://www.languagereactor.com) Netflix plugin:

```
Please explain the use of the word '{word}' in this sentence: {context}
```
