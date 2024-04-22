# Import the translate function from the mtranslate module
from mtranslate import translate
# from mtranslate import *
import colorama  # Importing colorama for colorful console outputs

# Initializing colorama for automatic reset of colors
colorama.init(autoreset=True)

# Define a Hinglish phrase to be translated
hinglish_phrase = "kaise ho to ap log"

# Use the translate function to translate the Hinglish phrase to English
# Parameters: source text, target language code ("en" for English), source language code ("auto" for automatic detection)
english_trans = translate(hinglish_phrase, "en", "auto")

# Print the translated phrase
print("TRANSLATED:", english_trans)
