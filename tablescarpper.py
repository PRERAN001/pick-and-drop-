import pandas as pd 
data=pd.read_html("https://www.w3schools.com/html/html_tables.asp",match="Company")
print(data)