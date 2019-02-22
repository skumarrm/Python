import PyPDF2
pdfFileObj = open('C:\\Users\\smallisudarsan@paypal.com\\Desktop\\IBM_DOJ_Letter.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()

# C:\Users\smallisudarsan@paypal.com\Desktop\IBM_DOJ_Letter