
import extract_data



extraer = extract_data.extract_raw_data

filepath = "C:\\Users\\Estefano\\Downloads\\QA_Test_Report_Index.docx"  # O "cv.docx"
texto = extraer(filepath)
print(texto)
