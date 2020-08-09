from fpdf import FPDF
title = 'Order Report for Customers'
def simple_table(spacing=2):
    data = [['Date', 'Customer Name', 'No of Orders', 'Submitted Orders','Incomple Orders'],
            ['04-08-19', 'ZCP', '57', '15','35'],
            ['04-08-19', 'ZCP', '59','32','23'],
            ['04-08-19', 'ZCP', '88','28','21']
            ]
 
    pdf = FPDF()
	#pdf.set_title(title)
    pdf.set_font("Arial", size=10)
    pdf.add_page()
	#pdf.cell(40, 10, 'Hello World!')
	#pdf.cell(75, 10, "Order Report for Users ZCP", 0, 2, 'C')
 
    col_width = pdf.w / 5
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1)
        pdf.ln(row_height*spacing)
 
    pdf.output('report/simple_table1.pdf')
 
if __name__ == '__main__':
    simple_table()
