# Forex-Converter

## Purpose/Information:

- This app is an simple foreign currency converter which uses the forex-python API to convert between various foreign currencies and display the results
  - Note: Not all world currencies are supported by the API so in those cases, an error message of "Invalid Country Code: " will show.

## Steps to run the Forex Converter on a local device

- Create and activate a virtual environment
  - For Mac/Ubuntu/WSL (with Python 3):
     1. python3 -m venv venv (To create an virtual environment named venv)
     2. source venv/bin/activate (To activate it)
  - On Windows, follow directions per <https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html>
- Install dependencies as listed on requirements.txt via pip using the command *pip install -r requirements.txt*
- Use pip to install the forex-python library in the virtual environment via *pip install forex-python*
- With Flask installed, run the backend server via the command *flask run*

