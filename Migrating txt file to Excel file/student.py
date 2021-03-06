#Importing module
from openpyxl import Workbook
from openpyxl.styles import *
from openpyxl.worksheet.table import Table, TableStyleInfo

#Opening the text file for reading
text_file = open("E:\\PYTHON\\[Tutsgalaxy.com] - Python 3 Complete Masterclass - Make Your Job Tasks Easier!\\19. SUPERHERO LEVEL Automate Excel Tasks with Python 3\\students.txt")

#Creating an empty list for storing the records as a list of lists
records = []

#Making sure we are reading the file from the very beginning
text_file.seek(0)

#Splitting each line in the file by the ";" delimiter and appending each list generated by readlines() to the new list, records 
for record in text_file.readlines():
    records.append(record.rstrip("\n").split(";"))



#Creating a new workbook object, by initializing the Workbook() class
workbook = Workbook()

#Setting the path to (location of) the new Excel workbook
#Note: we should escape the "\" characters inside the path using a "\", in order to avoid any conflicts with Python's special characters, like \n (new line ) or \t (tab).
file_path = "E:\\PYTHON\\[Tutsgalaxy.com] - Python 3 Complete Masterclass - Make Your Job Tasks Easier!\\19. SUPERHERO LEVEL Automate Excel Tasks with Python 3\\newstudent.xlsx"

#Saving the workbook
workbook.save(file_path)



#Renaming the default sheet to 'Student info'
sheet = workbook['Sheet']

sheet.title = 'Student info'

#Referencing the sheet
sheet = workbook['Student info']

#Populating the sheet with the rows from the text file
#Note that the table header will be created from the first row in the text file
for row in records:
    sheet.append(row)

#Creating a table inside the sheet
table = Table(displayName = "Table", ref = "A1:G7")

#Defining a style for the table (default style name, row/column stripes)
#Choose your table style from the default styles of openpyxl
#Just type in openpyxl.worksheet.table.TABLESTYLES in the Python interpreter
style = TableStyleInfo(name = "TableStyleMedium9", showRowStripes = True, showColumnStripes = True)

#Applying the style to the table
table.tableStyleInfo = style

#Adding the newly created table to the sheet
sheet.add_table(table)


    
#Saving the changes made to the workbook
workbook.save(file_path)

#Closing the text file
text_file.close()

#Closing the workbook
workbook.close()


#End of Program