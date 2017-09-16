#Script: Merge_PDF.py				   #
#author: Vaibhav Murkute			   #
########################################
import PyPDF2

pathPDF = []
numPDFs = input("Enter number of PDFs to Merge: ")
for i in range(int(numPDFs)):
	pathPDF.append(input("Enter the path for PDF "+str(i+1)+": "))

firstPath = open(pathPDF[0],'rb')
firstPdf = PyPDF2.PdfFileReader(firstPath)
mergedPdf = PyPDF2.PdfFileWriter()

for pageNum in range(firstPdf.getNumPages()):
	mergedPdf.addPage(firstPdf.getPage(pageNum))

for path in pathPDF[1:]:
	nextPdf = open(path,'rb')
	readPDF = PyPDF2.PdfFileReader(nextPdf)
	for p in range(readPDF.getNumPages()):
		mergedPdf.addPage(readPDF.getPage(p))

pdfOutputFile = open('MergedPdf.pdf','wb+')
mergedPdf.write(pdfOutputFile)
pdfOutputFile.close()
firstPath.close()

print('Files Merged...Saved in the same directory')
	

