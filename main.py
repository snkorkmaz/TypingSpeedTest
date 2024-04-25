from difflib import SequenceMatcher
from tkinter import *
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
NEWS_API_KEY = "YOUR_API_KEY"
text = ""
start_time = time.time()
elapsed_time = time.time() - start_time


# ---------------------------- FUNCTIONS ------------------------------- #

def center_window(window, width, height):
    """
        Centers the Tkinter window on the screen.
    """
    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate position window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set window position
    window.geometry(f"{width}x{height}+{x}+{y}")


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
    """
        Retrieves a random article URL from the TechCrunch news source using the News API and returns the URL of that
        article.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")  # Find the text paragraphs
    extracted_text = " ".join([p.get_text() for p in paragraphs])  # Create text string from paragraphs
    return extracted_text


def generate_text():
    """
        Generates a text containing at most 100 words extracted from a random article and returns a string containing at
        most 100 words from that article.
    """
    random_article_url = get_random_article_url()
    extracted_text = extract_text(random_article_url)
    words = extracted_text.split()

    # Ensure that the text contains at most 100 words
    if len(words) >= 100:
        generated_text = ' '.join(words[:100])
    else:
        generated_text = ' '.join(words)

    return generated_text


def start():
    """
        Starts the typing speed test.
        This function generates the text for the typing test, hides the initial text and start button,
        displays the generated text, entry field, and stop button, and records the start time of the test.
    """
    global text, start_time
    text = generate_text()  # generate the text
    initial_text_field.grid_forget()  # remove initial text from window
    start_button.grid_forget()  # remove start button
    text_field.insert(END, text)
    text_field.grid(row=1, column=1, columnspan=4)  # display generated text
    text_entry_field.grid(row=2, column=1, columnspan=4, padx=10, pady=10)  # display entry field
    stop_button.grid(row=3, column=1, columnspan=4, padx=10, pady=10)  # display stop button
    start_time = time.time()


def stop():
    """
        Stops the typing speed test, calculates results, and displays them.
        This function calculates results of the typing test by calling calculate_results function,
        removes the text, entry field, and stop button from the window, displays the test results,
        and displays the retry button.
    """
    global elapsed_time
    elapsed_time = time.time() - start_time
    text_field.grid_forget()  # remove text from window
    stop_button.grid_forget()  # remove stop button from window
    text_entry_field.grid_forget()  # remove entry field from window
    wpm, accuracy = calculate_results(text_field.get("1.0", END), text_entry_field.get("1.0", END))
    results = f"""Your Test Results
    
        Words Per Minute (WPM): {wpm}

        Accuracy: {accuracy} %
    """
    results_text_field.insert(END, results)
    results_text_field.grid(row=1, column=1, columnspan=4)  # display results
    retry_button.grid(row=3, column=1, columnspan=4, padx=10, pady=10)  # display retry button


def retry():
    """
        Resets the typing speed test to its initial state for another attempt.

        This function removes the test results and retry button from the window,
        clears the entry field, and displays the initial text and start button.
    """
    results_text_field.grid_forget()  # remove results from display
    retry_button.grid_forget()  # remove retry button from display
    results_text_field.delete(1.0, END)  # clear results
    text_entry_field.delete(1.0, END)
    initial_text_field.grid(row=1, column=1, columnspan=4)  # display initial text
    start_button.grid(row=3, column=1, columnspan=4, padx=10, pady=10)  # display start button


def calculate_results(generated_text, input_text):
    """
        Calculates the words per minute (WPM) and accuracy of the typing speed test and returns a tuple containing the
        words per minute (WPM) and accuracy ratio.
    """
    if len(input_text) - 1 == 0:
        wpm = 0
        similarity_ratio = 0
    else:
        # Words per minute (WPM) = (Total Typed Characters) / (5 * elapsed time  in minutes)
        wpm = len(input_text) - 1 / (5 * elapsed_time)

        # Calculate accuracy
        seq_matcher = SequenceMatcher(None, generated_text, input_text)
        similarity_ratio = seq_matcher.ratio()

    return wpm, similarity_ratio


# ---------------------------- UI SETUP ------------------------------- #

# CREATE A WINDOW
window = Tk()
window.title("Typing Speed Test")
window.config(padx=25, pady=25, bg=LIGHT_MINT)
center_window(window, 900, 800)

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
