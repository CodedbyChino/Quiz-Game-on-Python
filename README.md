# Quiz Game Project

Welcome to the Quiz Game project! This project is a simple Python quiz game where users can answer multiple-choice questions and receive feedback on their answers.

## Overview

The main goal of this project is to create an interactive quiz game that prompts users with questions and provides feedback based on their answers. The game should keep track of correct and incorrect answers, display the final score, and provide feedback messages for incorrect answers.

## Features

- User-friendly interface for answering questions.
- Feedback messages for correct and incorrect answers.
- Score tracking and display at the end of the game.
- Error handling for invalid inputs and unexpected behavior.

## How to Play

1. Clone this repository to your local machine.
2. Open the terminal or command prompt and navigate to the project directory.
3. Run the Python script `quiz_game.py`.
4. Follow the prompts to play the game.
5. Answer each question by typing the corresponding letter or option.
6. Receive feedback on your answers and see your final score at the end of the game.

## Issues and Resolutions

### Issue 1: Incorrect answer handling

**Description:** Initially, the program didn't handle incorrect answers properly. It didn't provide feedback or keep track of incorrect attempts.

**Solution:** Implemented error handling and feedback messages for incorrect answers. Used a loop to allow multiple attempts and a counter to track incorrect attempts.

### Issue 2: Score calculation

**Description:** The program didn't correctly calculate the final score at the end of the game.

**Solution:** Modified the score calculation logic to ensure that each correct answer increments the score correctly. Adjusted the code to calculate the percentage of questions answered correctly.

### Issue 3: User experience

**Description:** The user experience could be improved with better messaging and formatting.

**Solution:** Added informative messages for the user, such as feedback for incorrect answers and final score display. Formatted the output to make it more visually appealing and readable.
