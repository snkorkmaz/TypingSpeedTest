# Typing Speed Test

The Typing Speed Test is a Python application that allows users to test their typing speed and accuracy. It presents users with a passage of text, which they must type into an input field. After completing the test, the application calculates and displays the user's typing speed in words per minute (WPM) and accuracy.
## Features 
- Generates random passages of text from online articles for typing practice.
- Calculates typing speed and accuracy based on user input.
- Provides feedback on typing performance in real-time.
- Allows users to retry the test for additional practice.

## How to Run
To use the Typing Speed Test application, follow these steps:

1. Clone this repository to your local machine.

```bash
git clone https://github.com/snkorkmaz/TypingSpeedTest.git
```
2. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

3. Make sure you have obtained an API key for the News API. If you don't have one, you can sign up for an account and get your API key from [News API](https://newsapi.org/).
   1. Visit the [News API website](https://newsapi.org/) and sign up for an account if you haven't already.
   2. Once logged in, navigate to your account dashboard.
   3. You will find your API key listed on the dashboard. Copy the API key.

5. Once you have obtained your API key, open the `main.py` file in a text editor.
   
6. Locate the `NEWS_API_KEY` variable in the code and replace `"YOUR_API_KEY"` with your actual API key.

```bash
NEWS_API_KEY = "YOUR_API_KEY"
```
    
7. Save the `main.py` file after making the changes.

8. Run the application by executing the `main.py` file:
```bash
python main.py
```


## Usage

1. Starting the Test: Click on the "Start" button to begin the typing test.
2. Typing: Type the displayed text accurately and quickly into the input field.
3. Stopping the Test: Click on the "Stop" button to end the test and view your results.
4. Retry: Optionally, click on the "Try again!" button to retry the typing test.

## Contribution
Contributions, bug reports, and feature requests are welcome! Please feel free to open an issue.

## Author

- snkorkmaz
