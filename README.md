## Project Overview

This project demonstrates the use of Python for data cleaning and analysis. The dataset used in this project contains information about Netflix shows and movies, including titles, release dates, genres, and more. The project involves:

- Identifying and handling missing values.
- Converting date columns to proper datetime formats.
- Cleaning categorical data.
- Creating new features for enhanced analysis.
- Visualizing data using bar charts.

## Key Features

- **Data Cleaning:** Handled missing values, removed irrelevant columns, and converted data types for better analysis.
- **Data Transformation:** Converted `date_added` to UNIX timestamp and extracted primary genre information.
- **Visualization:** Visualized the number of Netflix titles released per year.

## Tools and Libraries Used

- **Pandas:** For data manipulation and cleaning.
- **Matplotlib:** For data visualization.
- **NumPy:** For numerical operations.
- **DateTime:** For handling date and time conversions.
- **Regular Expressions (re):** For string manipulation and extracting specific data.

## Installation

To run this project, you will need Python installed on your machine. You can install the required libraries using pip:

```bash
pip install pandas matplotlib numpy
