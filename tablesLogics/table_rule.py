
import camelot
import numpy as np

tables = camelot.read_pdf('pdftab.pdf',process_background=True)

# FIND OUT NO. OF TABLES IN A PDF DOCUMENT
tablecount = len(tables) # this will return the tables in the pdf 
print("No. of tables in the document :",tablecount)

# FIND OUT THE NUMBER OF ROWS AND COLUMNS
(tablerow,tablecolumn) = np.shape(tables[0])
print ("Table[0] ROW",tablerow)
print ("Table[0] COLUMN",tablecolumn)

# WE CAN ACCESS THE TABLE DATA CONTENT USING THE NUMPY ARRAY
dataArray = tables[0].df
print(dataArray)

print(dataArray[0][0])
print(dataArray[5][2]) # [Column][row]

#========== FINAL CODE END =========