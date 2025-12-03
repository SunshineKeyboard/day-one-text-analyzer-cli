# Day 1 – Python Foundations + Text Analyzer CLI

**Goal:** Learn Python fundamentals and build your first real project: a Text Analyzer CLI tool.

## Concepts for Today
- What a Python script is and how it runs
- Variables, strings, numbers
- Lists and dictionaries
- Loops (`for`, `while`)
- Functions (defining and calling)
- Reading from and writing to files

## Practice Warmups (Do These First)
1. Print `"Hello, world"`.
2. Create two variables, `name` and `age`, and print a sentence using both.
3. Make a list of three favorite foods and loop over them, printing each one.
4. Write a function `greet(name)` that prints a greeting.
5. Create a dictionary with keys `title`, `author`, `year` for a favorite book.

## Project: Text Analyzer CLI

You will build a script that:
- Asks the user for a path to a `.txt` file.
- Reads the file.
- Counts:
  - Total number of characters
  - Total number of words
  - Total number of lines
- Finds the 10 most common words and how many times they appear.
- Prints a simple text report to the terminal.

### Suggested Steps
1. Open `text_analyzer.py`.
2. Write code to ask the user for a file path.
3. Write a function to read the file contents.
4. Write a function to compute basic stats (characters, words, lines).
5. Write a function to compute the 10 most common words.
6. In `main()`, glue everything together and print the report.

### Stretch Goals
- Ignore capitalization (treat "The" and "the" as the same word).
- Ignore common stop words like "the", "and", "a", "to".
- Allow the user to optionally save the report to a new file.

During our chat, we will:
- Break down each step.
- Talk through your code.
- Improve structure and readability together.