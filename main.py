from tkinter import *
from tkinter import filedialog, ttk
from tkinter.ttk import Style
import requests
from bs4 import BeautifulSoup
import random
import time

from customtkinter import CTkButton

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


def start():
    initial_text_field.grid_forget()
    text_field.insert(END, text)
    text_field.grid(row=1, column=1, columnspan=4)
    text_entry_field.grid(row=2, column=1, columnspan=4, padx=10, pady=10)
    start_button.grid_forget()
    stop_button.grid(row=3, column=1, columnspan=4, padx=10, pady=10)


def stop():
    text_field.grid_forget()
    stop_button.grid_forget()
    text_entry_field.grid_forget()
    results = f"""Your Test Results
    
        Words Per Minute (WPM): [Your WPM Score]

        Accuracy: [Your Accuracy Percentage]
    """
    results_text_field.insert(END, results)
    results_text_field.grid(row=1, column=1, columnspan=4)
    retry_button.grid(row=3, column=1, columnspan=4, padx=10, pady=10)


def retry():
    global text
    text = generate_text()
    results_text_field.grid_forget()
    retry_button.grid_forget()
    results_text_field.delete(1.0, END)
    initial_text_field.grid(row=1, column=1, columnspan=4)
    start_button.grid(row=3, column=1, columnspan=4, padx=10, pady=10)



# ---------------------------- MAIN  ------------------------------- #

text = generate_text()

# ---------------------------- UI SETUP ------------------------------- #

# CREATE A WINDOW
window = Tk()
window.title("Typing Speed Test")
window.geometry("900x800")
window.config(padx=25, pady=25, bg=LIGHT_MINT)

# CREATE CUSTOM STYLE FOR ENTRY WIDGET
style = Style()
style.configure('Custom.TEntry', bordercolor=MIDDLE_TURQUOISE, borderwidth=3, relief='solid', fieldbackground='white',
                foreground="black", padding=5, focuscolor=MIDDLE_TURQUOISE)

# CREATE HEADER LABEL
heading = Label(text="Typing Speed Test ", fg=DARK_TURQUOISE, bg=LIGHT_MINT, font=(FONT_NAME, 35, "bold"))
heading.grid(column=1, row=0, columnspan=4, pady=50)

# CREATE INITIAL TEXT
initial_text_field = Text(window, bg=LIGHT_MINT, font=(FONT_NAME, 12), wrap=WORD, height=10, borderwidth=0,
                          state=NORMAL)
initial_text = """Welcome to the Typing Speed Test!

This application allows you to test your typing speed and accuracy. When you're ready, click on the "Start" button. You'll then be presented with a text that you need to type into the text field. Once you're finished, click "Stop" to view your results.

Best of luck testing your typing skills!

"""
initial_text_field.insert(END, initial_text)
initial_text_field.grid(row=1, column=1, columnspan=4)

# CREATE TEXT
text_field = Text(window, bg=LIGHT_MINT, font=(FONT_NAME, 12), wrap=WORD, height=10, borderwidth=0)
# text_field.insert(END, text)

# CREATE TEXT ENTRY FIELD
text_entry_field = Text(window, width=80, font=('Arial', 12), wrap='word', height=10, borderwidth=2)

# CREATE A START BUTTON
start_button = CTkButton(window, text="Start")
start_button.configure(text_color="white", fg_color=MIDDLE_TURQUOISE, bg_color=LIGHT_MINT, hover_color=DARK_TURQUOISE,
                       corner_radius=50, width=220, command=start,
                       font=(FONT_NAME, 15, "bold"))
start_button.grid(row=3, column=1, columnspan=4, padx=10, pady=10)

# CREATE A STOP BUTTON
stop_button = CTkButton(window, text="Stop")
stop_button.configure(text_color="white", fg_color=MIDDLE_TURQUOISE, bg_color=LIGHT_MINT, hover_color=DARK_TURQUOISE,
                      corner_radius=50, width=220, command=stop,
                      font=(FONT_NAME, 15, "bold"))

# CREATE TEXT FOR TEST RESULTS
results_text_field = Text(window, bg=LIGHT_MINT, font=(FONT_NAME, 12), wrap=WORD, height=10, borderwidth=0,
                          state=NORMAL)

# CREATE A STOP BUTTON
retry_button = CTkButton(window, text="Try gain!")
retry_button.configure(text_color="white", fg_color=MIDDLE_TURQUOISE, bg_color=LIGHT_MINT, hover_color=DARK_TURQUOISE,
                       corner_radius=50, width=220, command=retry,
                       font=(FONT_NAME, 15, "bold"))

window.mainloop()
