import tabula
import pandas as pd
file1 = "22972_Form 16_2021-22.pdf" 
lst = tabula.read_pdf(file1,pages='all',password='BCZPT7096P20111996')
# df = pd.DataFrame(lst)
# df.to_excel("testPDF.xlsx")
print(lst)