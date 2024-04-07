# Import the translate function from the mtranslate module
from mtranslate import translate
import colorama  # Importing colorama for colorful console outputs

# Initializing colorama for automatic reset of colors
colorama.init(autoreset=True)

# Define an English phrase to be translated
english_phrase = "One piece is an anime series that has been running for over 20 years."

# Use the translate function to translate the English phrase to Hindi
# Parameters: source text, target language code ("hi" for Hindi), source language code ("auto" for automatic detection)
hindi_trans = translate(english_phrase, "hi", "auto")

# Print the translated phrase
print("TRANSLATED:", hindi_trans)

