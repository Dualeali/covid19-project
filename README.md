🦠 COVID-19 Global Data Tracker Project
📄 Description
This project is part of my final submission for the Python Development Module. It involves analyzing COVID-19 data for selected countries using real-world datasets. The goal was to clean, filter, and process the data using Python and gain insights through computation and (optionally) visualization.

🎯 Project Objectives
Analyze COVID-19 trends in different countries

Convert raw date strings into usable datetime objects

Filter data by specific countries

Calculate a 7-day rolling average for new COVID-19 cases

Sort and organize data chronologically

Handle warnings like SettingWithCopyWarning properly using .copy()

🛠️ Tools & Libraries Used
Python 3 – Programming language used for data analysis

Jupyter Notebook – For writing and running the project code step-by-step

pandas – For data loading, filtering, and processing

matplotlib – For visualizing COVID-19 trends using line plots

seaborn – For enhancing visualizations with cleaner styling (sns.set_style("whitegrid"))


🚀 How to Run the Project
Clone or download the repository from GitHub

Open the notebook file (covid_analysis.ipynb) using Jupyter Notebook

Make sure your dataset file (e.g., owid-covid-data.csv) is in the same directory

Run each cell in order from top to bottom

If needed, install pandas:

bash
Copy
Edit
pip install pandas
View the output and rolling average results

🌍 Countries Analyzed
United States

India

Germany

You can modify the countries list in the notebook to include other countries as well.

🔍 Insights & Reflections
Working with real-world data requires attention to data types and cleaning steps

Using .copy() is important when working with filtered DataFrames to avoid warnings and bugs

The 7-day rolling average helps clearly see trends without daily fluctuations

This project helped strengthen my pandas skills and built confidence in handling time-series data

✅ Notebook Status
✔️ All cells run from start to finish

✔️ No errors in the notebook

✔️ All outputs display correctly

Let me know if you'd like help writing a short project summary for the GitHub description or need help publishing it to GitHub.
