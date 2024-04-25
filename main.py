from tkinter import *
from tkinter import filedialog, ttk
from tkinter.ttk import Style
import requests
from bs4 import BeautifulSoup
import random

# ---------------------------- CONSTANTS ------------------------------- #

DARK_TURQUOISE = "#003C43"
MIDDLE_TURQUOISE = "#135D66"
MINT = "#77B0AA"
LIGHT_MINT = "#E3FEF7"
FONT_NAME = "Arial"

# SET UP API CONSTANTS
NEWS_ENDPOINT = "http://newsapi.org/v2/top-headlines"
NEWS_API_KEY = "c5b72e2ce9f84dc1af0d050a1da5fa54"


# ---------------------------- FUNCTIONS ------------------------------- #

def get_random_article_url():
    params = {
        "apiKey": NEWS_API_KEY,
        "sources": "techcrunch"
    }
    response = requests.get(NEWS_ENDPOINT, params=params)
    data = response.json()  # save response as json
    articles = data["articles"]  # get the articles
    random_article = random.choice(articles)  # select random article
    random_article_url = random_article["url"]  # get article url
    return random_article_url


def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")  # Find the text paragraphs
    extracted_text = " ".join([p.get_text() for p in paragraphs])  # Create text string from paragraphs
    return extracted_text


def generate_text():
    random_article_url = get_random_article_url()
    extracted_text = extract_text(random_article_url)
    words = extracted_text.split()
    return ' '.join(words[:100])


# ---------------------------- MAIN  ------------------------------- #

text = generate_text()

# ---------------------------- UI SETUP ------------------------------- #

# CREATE A WINDOW
window = Tk()
window.title("Image Watermark")
window.geometry("900x800")
window.config(padx=25, pady=25, bg=LIGHT_MINT)

# CREATE CUSTOM STYLE FOR ENTRY WIDGET
style = Style()
style.configure('Custom.TEntry', bordercolor=MIDDLE_TURQUOISE, borderwidth=3, relief='solid', fieldbackground='white',
                foreground="black", padding=5, focuscolor=MIDDLE_TURQUOISE)

# CREATE HEADER LABEL
heading = Label(text="Typing Speed Test ", fg=DARK_TURQUOISE, bg=LIGHT_MINT, font=(FONT_NAME, 35, "bold"))
heading.grid(column=1, row=0, columnspan=4, pady=50)

# CREATE TEXT
text_field = Text(window, bg=LIGHT_MINT, font=(FONT_NAME, 12), state=NORMAL, wrap=WORD, height=10)
text_field.insert(END, text)
text_field.grid(row=1, column=1, columnspan=4)

# CREATE TEXT ENTRY FIELD
# CREATE TEXT ENTRY FIELD
# CREATE TEXT ENTRY FIELD
text_entry_field = Text(window, width=80, height=10, font=('Arial', 12), wrap='word')
text_entry_field.grid(row=2, column=1, columnspan=4, padx=10, pady=10)

# Create a button to retrieve the entered text
# button = Button(window, text="Get Text", command=on_button_click)
# button.pack()

window.mainloop()
