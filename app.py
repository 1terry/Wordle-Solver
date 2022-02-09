import time
from tracemalloc import start

from pynput.keyboard import Key, Controller
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

keyboard = Controller()

'''
https://matt-rickard.com/wordle-whats-the-best-starting-word/
#:~:text=I'm%20sure%20with%20enough,be%20present%20in%20each%20guess.
'''

# We know that the first word is completely random, so we pick the word that can eliminate the most
# Possibilities as a result of the position of it's vowels

starting_word = "SOARE"

# This will be the thing we are interested in writing
# time.sleep(5)
# for i in starting_word:
#     keyboard.press(i)
#     keyboard.release(i)

path = "body/game-app/game-theme-manager/"

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.powerlanguage.co.uk/wordle/")
# elem = driver.find_element_by_id('board')
assert "Wordle" in driver.title


# driver.send_keys(starting_word)
# driver.send_keys(Keys.RETURN)
for i in starting_word:
    keyboard.press(i)
    keyboard.release(i)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(10)

driver.close()
print("\nclosed")
# with open("https://www.powerlanguage.co.uk/wordle/") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')

# soup = BeautifulSoup("<html>a web page</html>", 'html.parser')

'''
Algorithm

- After inputting soare, look at what vowels are accepted
- change the position of the accepted vowels and find words in the dictionary that match
- Find the word with the most vowels
- If we have equals, we randomize
- Alternatively, could keep track of which words are the most common

'''


# Game help is the window to close, game instructions is the class
