# Duck Latin Translator

## Overview

Duck Latin is a simple Python program that takes a phrase from the user and translates it into a playful version of Pig Latin, called "Duck Latin." This program provides a graphical user interface (GUI) where users can enter a phrase, and it will output the translated version. The GUI also includes "Quack!" and "Quit!" buttons to translate or exit the program.

## Features

- **Graphical Interface**: Built using `graphics.py` to create an easy-to-use GUI for entering and translating text.
- **Translation Rules**:
  - Words starting with vowels get "wack" appended to the end.
  - Words starting with common consonant blends are modified accordingly with "ack."
  - Other words have their first letter moved to the end followed by "ack."
- **Interactive Buttons**: Users can click "Quack!" to see the translation or "Quit!" to close the application.

## Requirements

- Python 3.x
- `graphics.py` library (available [here](http://mcsp.wartburg.edu/zelle/python/graphics.py))
- `math` standard Python library

## How to Use

1. Clone or download this repository.
2. Install the required `graphics.py` library if you haven't already.
3. Run the script using Python:

    ```sh
    python duck_latin.py
    ```

4. Enter a phrase in the text entry box and click "Quack!" to see the Duck Latin translation.
5. Click "Quit!" to close the application.

## Duck Latin Rules

1. **Words Starting with a Vowel**: The word will have "wack" appended.
    - Example: "apple" → "applewack"
2. **Words Starting with a Blend of Three Letters**: The blend is moved to the end of the word, followed by "ack."
    - Example: "string" → "ingstrack"
3. **Words Starting with a Blend of Two Letters**: The blend is moved to the end, followed by "ack."
    - Example: "chase" → "asechack"
4. **Other Words**: The first letter is moved to the end of the word, followed by "ack."
    - Example: "dog" → "ogdack"

## Code Structure

- `main()`: Main function that initializes the game and handles the user input and click interactions.
- **GUI Elements**:
  - **Text Entry**: For the user to input their phrase.
  - **Buttons**: "Quack!" to translate and "Quit!" to close the application.
  - **Output**: Displays the translated text.

## Future Improvements

- **Error Handling**: Better handling of empty input or special characters.
- **Enhanced UI**: Improve the visual elements for a more interactive and fun experience.
- **Additional Features**: Add a reset button to clear the input and output text fields.

## Notes

- The translation is a playful twist on Pig Latin, adding a fun touch for users.
- Make sure to click "Quack!" only after entering a phrase for translation.

## License

This project is open source and available under the MIT License.

---

**Author**: Alexander Harshman

Feel free to contribute or suggest improvements!
