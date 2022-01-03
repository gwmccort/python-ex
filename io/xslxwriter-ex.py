# read & write xls files via pandas
# from: Udemy - Python for Excel 2021.zip
####################################

import pandas as pd

# read in csv file
# cerDF = pd.read_csv('Data/cereals.csv')
# print(cerDF.head())

# read xls file
inFname = 'Data/input.xlsx'
inXlsFile = pd.ExcelFile(inFname)
myDF = pd.read_excel(inXlsFile)
print(myDF.head())

# write data frame to xls
outFP = 'Data/output.xlsx'
writer = pd.ExcelWriter(outFP)
myDF.to_excel(writer)
writer.save()

# origXlsFile = 'data/my.xlsx'
# myXlsFile = pd.ExcelFile(origXlsFile)
# xDf = pd.read_excel(myXlsFile, sheet_name=0)
# print(xDf)
