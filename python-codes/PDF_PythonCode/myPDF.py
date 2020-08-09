from fpdf import FPDF
import datetime
title = 'Order Report for Customers'
spacing=2
pdf=FPDF(format='letter', unit='in')
pdf.add_page()
pdf.set_font('Arial','',10.0) 

epw = pdf.w - 4*pdf.l_margin
col_width = epw/5
data = [['Date', 'Customer Name', 'No of Orders', 'Submitted Orders','Incomple Orders'],
            ['04-08-19', 'ZCP', '57', '15','35'],
            ['04-08-19', 'ZCP', '59','32','23'],
            ['04-08-19', 'ZCP', '88','28','21']
            ]

pdf.set_font('Arial','B',14.0)
#pdf.cell(w, h = 0, txt = '', border = 0, ln = 0, align = '', fill = False, link = '')
pdf.cell(epw, 1.0, 'Order Report', align='C')
pdf.set_font('Arial','',10.0)
pdf.ln(1)
row_h = pdf.font_size
th=row_h*spacing
for row in data:
	print(row)
	for datum in row:
		print(datum)
		#pdf.cell(5, 1, str(datum), border=1, align='C')
		pdf.cell(col_width, th, str(datum), border=1, align='C')
		#pdf.cell(50, 10, 'Question', 1, 0, 'C')
	pdf.ln(th)
	
#pdf.ln(5*th)

pdf.output('report/order_report ' +datetime.datetime.now().strftime("%Y-%m-%d")+'.pdf','F')
import os
from os import path
#path.exists("order_report43.pdf")
print ("file exist:"+str(path.exists("order_report43.pdf")))
#if os.path.isfile('C:\\Users\\jytripat\\Desktop\\PDF_PythonCode\\report')
print (os.path)