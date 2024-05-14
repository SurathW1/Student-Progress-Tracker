# Student Progress Tracker

This Python script is designed to track and analyze the academic progress of students based on their earned credits. It allows users (staff or students) to input credit values for passed, deferred, and failed courses, and then predicts the overall outcome (progress, trailer, retriever, or exclude) based on those values.

## Features

- User-friendly command-line interface for inputting credit values
- Validation checks for correct credit value ranges and total credit sum
- Prediction of academic outcome based on credit distribution
- Histogram visualization of outcome distribution (staff only)
- Data storage of outcomes and associated credits in a text file
- Printing of stored outcome data to the console

## Prerequisites

- Python 3.x
- `graphics` module (included in the Python standard library)

## Usage

1. Run the `w2052104.py` script.
2. Enter your role as either "staff" or "student".
3. Follow the prompts to input credit values for passed, deferred, and failed courses.
4. The script will predict the academic outcome based on the input credits.
5. For staff members, the option to generate a histogram visualization will be available.
6. The outcome data will be written to a text file (`outcome_credits.txt`) and printed to the console.

## File Structure

- `w2052104.py`: The main Python script containing the code for the Student Progress Tracker
- `outcome_credits.txt`: A text file created by the script to store the outcome data

## References

The code utilizes the following resources and references:

- Graphics module from the Python standard library
- W3Schools tutorials for Python concepts (while loops, tuples, dictionaries, functions)
- YouTube tutorials for graphics.py module

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Wartburg College for the graphics.py module reference
- W3Schools for the Python tutorials
- YouTube for the graphics.py module tutorials
