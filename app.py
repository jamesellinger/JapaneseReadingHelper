from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from datetime import datetime
import deepl
import json
import configparser
import os

app = Flask(__name__)

# Load configuration
config = configparser.ConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), 'settings.ini')
if not os.path.exists(config_file_path):
    print(f"Error: Configuration file '{config_file_path}' does not exist.")
    exit(1)

config.read(config_file_path)

# Get settings for OpenRouter stuff
base_url = config.get('OpenRouter', 'base_url')
openrouter_api_key = config.get('OpenRouter', 'openrouter_api_key')
model = config.get('OpenRouter', 'model')
model_file_inf = config.get('OpenRouter', 'model_file_inf')

# Get settings for DeepL stuff
deepl_API_key = config.get('DeepL', 'deepl_API_key')
source_lang = config.get('DeepL', 'source_lang')
target_lang = config.get('DeepL', 'target_lang')
model_type = config.get('DeepL','model_type')

# Check for folder that holds explanation histories, create if does not exist
explanation_history_folder = os.path.join(os.getcwd(), "explanation_history")

if not os.path.exists(explanation_history_folder):
    os.makedirs(explanation_history_folder)

# Check for folder that holds translation histories, create if does not exist
translation_history_folder = os.path.join(os.getcwd(), "translation_history")

if not os.path.exists(translation_history_folder):
    os.makedirs(translation_history_folder)

def explainWordContext(context, word):
    """
    Explains the use of a specific word or phrase within a given context using an AI model.
    Saves the context, word, and explanation to a JSON file with a timestamp.
    """
    client = OpenAI(
        base_url=base_url,
        api_key=openrouter_api_key
    )

    user_message = f"Please explain the use of the word '{word}' in this sentence: {context}"

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    response_content = completion.choices[0].message.content

    # Save to JSON file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"explanation_history/{model_file_inf}_{timestamp}.json"

    output_data = {
        "CONTEXT": context,
        "WORD": word,
        "response": response_content
    }

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(output_data, file, ensure_ascii=False, indent=2)

    return response_content

def deeplTranslate(context):
    """
    Translates the given context text using the DeepL API.
    Uses settings from the configuration file for API key, source and target languages.
    """
    translator = deepl.Translator(deepl_API_key)
    result = translator.translate_text(context,
                                        source_lang = source_lang,
                                        target_lang = target_lang,
                                        model_type = model_type)
    
     # Save to JSON file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"translation_history/DeepL_{timestamp}.json"

    output_data = {
        "CONTEXT": context,
        "TRANSLATION": result.text
    }

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(output_data, file, ensure_ascii=False, indent=2)
    
    return result.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/explain', methods=['POST'])
def explain():
    data = request.json
    context = data.get('context', '')
    word = data.get('word', '')

    if not context or not word:
        return jsonify({'error': 'Context and word are required'}), 400

    try:
        explanation = explainWordContext(context, word)
        return jsonify({'explanation': explanation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    context = data.get('context', '')

    if not context:
        return jsonify({'error': 'Context is required'}), 400

    try:
        translation = deeplTranslate(context)
        return jsonify({'translation': translation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)