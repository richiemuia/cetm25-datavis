
# Information

**Name :** Richard Muia

**Project:** CETM25 Data Visualisation

---

# Access The Built Application

The application is hosted on Streamlit cloud services for easy access, check it out!.
Note, the application may take some time to 'wake-up' if it hasn't been acccesed in the last 7 days.

[https://richiemuia-cetm25-datavis-main-nh87n3.streamlit.app/](https://richiemuia-cetm25-datavis-main-nh87n3.streamlit.app/)

# Data Sources

The dashboard uses the following data sources to build the visualisations.

<https://www.gov.uk/government/statistics/gas-section-4-energy-trends>

<https://www.gov.uk/government/statistics/electricity-section-5-energy-trends>

Accessed 22-February-2023, offline copies of the specific data files were obtained to ensure the application runs without dependency on the gov.uk website.

ET_4.4_JAN_23.xlsx

ET_5.4_JAN_23.xlsx

---

# Installing System to Run Locally

If you need to install and run the dashboard locally, follow the instructions below.

## Pre-requisites

Python 3.9+ installed. See Install instructions [Here](https://wiki.python.org/moin/BeginnersGuide/Download)

## Code Structure

The Code is structured in the following way:

    project
    ¦---data
    ¦   ¦   ET_4.4_JAN_23.xlsx
    ¦   ¦   ET_5.4_JAN_23.xlsx
    ¦
    ¦---src
    ¦   ¦   main.py
    ¦
    ¦   readme.md
    ¦   requirements.txt
    ¦   run.bat

## Dependencies Install

Extract the code to a suitable location on your computer.

Open a command prompt or terminal and change to the root directory of the project and type:

    pip install - r requirements.txt

This will retrieve the required modules for the application to run.

Once complete, run the following command:

    .\run.bat

For Info. The above batch script will run the following command:

    streamlit run .\src\main.py

This will then start a local server accessible via: <http://localhost:8501>

To stop the server, Press **Ctrl + C** in the terminal window.
