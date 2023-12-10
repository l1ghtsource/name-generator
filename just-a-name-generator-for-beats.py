# Тексты беру отсюда: https://www.hplovecraft.com/writings/texts/
# average Lovecraft enjoyer

import requests
from bs4 import BeautifulSoup
import spacy
import random
from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import ttk

nlp = spacy.load("en_core_web_sm")


def extract_random_adjective_noun(text):
    doc = nlp(text)

    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    nouns = [token.text for token in doc if token.pos_ == "NOUN"]

    if adjectives and nouns:
        random_adjective = random.choice(adjectives)
        random_noun = random.choice(nouns)
        return f"{random_adjective} {random_noun}"
    else:
        return None


def fetch_and_translate():
    url = url_entry.get()

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()

        result_text.delete(1.0, tk.END)

        for _ in range(5):
            random_phrase = extract_random_adjective_noun(text)

            if random_phrase:
                translator = GoogleTranslator(source='auto', target='ru')
                translated_phrase = translator.translate(random_phrase)
                result_text.insert(tk.END, translated_phrase + "\n\n")
            else:
                result_text.insert(tk.END, "Не удалось найти подходящее словосочетание.\n\n")
    else:
        result_text.insert(tk.END, "Не удалось загрузить страницу.")


root = tk.Tk()
root.title("Average Lovecraft Enjoyer")

style = ttk.Style()
style.configure("TButton", padding=(5, 5, 12, 12))

url_label = ttk.Label(root, text="Введите URL:")
url_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky="w")

url_entry = ttk.Entry(root, width=50)
url_entry.grid(column=2, row=0, padx=10, pady=10, sticky="w")

fetch_button = ttk.Button(root, text="Just generate...", command=fetch_and_translate)
fetch_button.grid(column=0, row=1, columnspan=3, padx=10, pady=10)

result_text = tk.Text(root, height=10, width=50)
result_text.grid(column=0, row=2, columnspan=3, padx=10, pady=10)

root.mainloop()
