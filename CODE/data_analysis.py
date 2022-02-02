import pandas as pd
import io

buffer = io.StringIO()

#Forest area (% of land area) https://data.worldbank.org/indicator/AG.LND.FRST.ZS
df = pd.read_csv("Project/Code/data/forest_area/API_AG.LND.FRST.ZS_DS2_en_csv_v2_2917381.csv", skiprows=4)
#print(df.info(verbose=True))
df.info(verbose=True, buf=buffer)
s = buffer.getvalue()
with open("Project/Code/stats.txt", "w", encoding="utf-8") as f: 
    f.write("**********Forest area (% of land area) https://data.worldbank.org/indicator/AG.LND.FRST.ZS******************\n") 
    f.write(s)
buffer = io.StringIO()
#GDP per capita (current US$) - https://data.worldbank.org/indicator/NY.GDP.PCAP.CD
df = pd.read_csv("Project/Code/data/gdp/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_2916517.csv", skiprows=4)
#print(df.info(verbose=True))
df.info(verbose=True, buf=buffer)
s = buffer.getvalue()
with open("Project/Code/stats.txt", "a", encoding="utf-8") as f: 
    f.write("**********GDP per capita (current US$) - https://data.worldbank.org/indicator/NY.GDP.PCAP.CD******************\n") 
    f.write(s)
buffer = io.StringIO()
#GNI per capita, Atlas method (current US$) - https://data.worldbank.org/indicator/NY.GNP.PCAP.CD
df = pd.read_csv("Project/Code/data/gni/API_NY.GNP.PCAP.CD_DS2_en_csv_v2_2924224.csv", skiprows=4)
#print(df.info(verbose=True))
df.info(verbose=True, buf=buffer)
s = buffer.getvalue()
with open("Project/Code/stats.txt", "a", encoding="utf-8") as f: 
    f.write("**********GNI per capita, Atlas method (current US$) - https://data.worldbank.org/indicator/NY.GNP.PCAP.CD******************\n") 
    f.write(s)
buffer = io.StringIO()
#Inflation, consumer prices (annual %) - https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG
df = pd.read_csv("Project/Code/data/inflation/API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_2917215.csv", skiprows=4)
#print(df.info(verbose=True))
df.info(verbose=True, buf=buffer)
s = buffer.getvalue()
with open("Project/Code/stats.txt", "a", encoding="utf-8") as f: 
    f.write("**********Inflation, consumer prices (annual %) - https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG******************\n") 
    f.write(s)
buffer = io.StringIO()
#Population density (people per sq. km of land area) - https://data.worldbank.org/indicator/EN.POP.DNST
df = pd.read_csv("Project/Code/data/population/API_EN.POP.DNST_DS2_en_csv_v2_2917301.csv", skiprows=4)
#print(df.info(verbose=True))
df.info(verbose=True, buf=buffer)
s = buffer.getvalue()
with open("Project/Code/stats.txt", "a", encoding="utf-8") as f: 
    f.write("**********Population density (people per sq. km of land area) - https://data.worldbank.org/indicator/EN.POP.DNST******************\n") 
    f.write(s)
buffer = io.StringIO()

#Human Development Index (HDI) - http://hdr.undp.org/en/indicators/137506#
df = pd.read_csv("Project/Code/data/hdi/Human Development Index (HDI).csv", skiprows=5, encoding='latin-1')
#print(df.info(verbose=True))
df.info(verbose=True, buf=buffer)
s = buffer.getvalue()
with open("Project/Code/stats.txt", "a", encoding="utf-8") as f: 
    f.write("**********Human Development Index (HDI) - http://hdr.undp.org/en/indicators/137506#******************\n") 
    f.write(s)
buffer = io.StringIO()
