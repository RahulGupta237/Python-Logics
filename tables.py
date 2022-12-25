
import pdfplumber
from pdfminer.layout import LTTextBoxHorizontal


#---------Logic Implementation of number of line detected----------------
def extract_text_line(filename,page):
    pdf = pdfplumber.open(filename, laparams={})
    pages = pdf.pages[int(page)].layout
    text_line=[]
    for element in pages:
    
        if isinstance(element, LTTextBoxHorizontal):
            for line in element:
                charset=False
                print(line.get_text())
                text_line.append(line.get_text())
                if charset:    
                    print(line.get_text())
                    text_line.append(line.get_text())
                else:
                    #print("Number of line not detected")
                    pass   
    print("#####Number of line detected ############################")       
    print(len(text_line))
    no_line=False
    if 0<len(text_line)<3:
        no_line=True
        pass
    print(no_line)
    return no_line
    
print(extract_text_line('content.pdf','3'))