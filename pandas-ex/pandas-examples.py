import pandas as pd

# initialise dataframe
df = pd.DataFrame(columns=['something'])

# read excel
df = pd.read_excel('some/file.xlsx', sheet_name='sheet')
