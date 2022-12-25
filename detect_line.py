

import pdfplumber
from pdfminer.layout import LTTextBoxHorizontal,LTChar


# ---------Logic Implementation of number of line detected----------------
def extract_text_line(filename, page):
    pdf = pdfplumber.open(filename, laparams={})
    pages = pdf.pages[int(page)].layout
    text_line = []
    for element in pages:

        if isinstance(element, LTTextBoxHorizontal):
            for line in element:
                charset = False
                for character in line:
                    if isinstance(character, LTChar):
                        fontsize = character.size
                        if int(float(fontsize))==30:
                            charset = True
                            print(fontsize)
                            print(int(float(fontsize)))
                
                            print(line.get_text())
                            text_line.append(line.get_text())
                else:
                    #print("Number of line not detected")
                    pass
    print("#####Number of line detected ############################")
    print(text_line)
    print(len(text_line))
    no_line = False
    if 0 < len(text_line) < 6:
        no_line = True
        pass
    print(no_line)
    return no_line

extract_text_line("rahul.pdf",4)