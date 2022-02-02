DESCRIPTION - Describe the package in a few paragraphs

Green Analytics is a unique and creative platform to analyze, visualize and identify the socio-economic factors
that are most relevant to the changes of Forest cover rate. It is a user-friendly visual tool that determines
correlations against Forest cover changes  and socio-economic factors, over the course of past 30 years.

Tech used - Jupyter Notebook, Python 3.7 or higher, Tableau Desktop 2021 or higher

Contents

- CODE - Parent directory for all code and data
 | - data - All input and output data is collected here
 | - viz - Contains "Tableau" visualization file - "green_analytics_v2.twbx"
 | - Correlation.ipynb - Creates Pearson's correlation coefficients for all the countries - Output -> data_relationship.csv
 | - data-clustering.ipynb - Does Principal component analysis and clustering for countries - Output -> data-clustering.csv
 | - Project_Wrangling.ipynb - Reading and cleaning of downloaded and web scraped data - Output -> data_countries.csv, data_measurements.csv

- DOC
 | - Poster - Project Poster
 | - Report - Project Report

INSTALLATION - How to install and setup your code

 - Install Jupyter notebook - https://jupyter.org/install
 - Install Python 3 (3.7 or higher) - https://realpython.com/installing-python/
 - Install Tableau Desktop 2021 (or higher) - https://www.tableau.com/products/desktop

EXECUTION - How to run a demo on your code - The input and output files are already included in the "data" folder,
            so execution is "Optional"

 - Navigate to the "CODE" folder and launch / run Jupyter Notebook
    - SAMPLE - CODE> Jupyter Notebook

 - Within the Jupyter - Open Project_Wrangling.ipynb
    - Go to Cell menu and Run All
    - Output files - data_countries.csv, data_measurements.csv would be created in the data folder

 - Within the Jupyter - Open Correlation.ipynb
    - Go to Cell menu and Run All
    - Output files - data_relationship.csv would be created in the data folder

 - Within the Jupyter - Open data-clustering.ipynb
    - Go to Cell menu and Run All
    - Output files - data-clustering.csv would be created in the data folder

 - Now open "green_analytics_v2.twbx" which has pre-created dashboards and preloaded data
    - If required the data sources can be remapped by going to "Data Source" in the bottom left corner of the tableau
      dashboard
        - Map the data sources in the "data" folder.