from fpdf import FPDF
import csv,xlwt,xlsxwriter,sys, datetime
def generate_pdf():
    #print(result)
    spacing=2
    title = 'Order Report for Customers'
    pdf = FPDF(format='letter', unit='in')
    pdf.add_page()
    pdf.set_font('Arial', '', 10.0)

    epw = pdf.w - 4 * pdf.l_margin
    col_width = epw / 5
    data = [['Date', 'Customer Name', 'No of Orders', 'Submitted Orders', 'Incomplete Orders'],
            ['04-08-19', 'ZCP', '57', '15', '35'],
            ['04-08-19', 'ZCP', '59', '32', '23'],
            ['04-08-19', 'ZCP', '88', '28', '21']
            ]

    pdf.set_font('Arial', 'B', 14.0)
    # pdf.cell(w, h = 0, txt = '', border = 0, ln = 0, align = '', fill = False, link = '')
    pdf.cell(epw, 1.0, 'Order Report', align='C')
    pdf.set_font('Arial', '', 10.0)
    pdf.ln(1)
    row_h = pdf.font_size
    th=row_h*spacing
    for row in data:
        for datum in row:
            pdf.cell(col_width, th, str(datum), border=1, align='C')
        pdf.ln(th)

    # pdf.ln(5*th)

    pdf.output('order_report ' + datetime.datetime.now().strftime("%Y-%m-%d") + '.pdf', 'F')
generate_pdf()

def generate_csv(result):
    print("IN GENRATE CSV**********")
    #handle = open(sys.argv[1])
    data = [['Date', 'Customer Name', 'No of Orders', 'Submitted Orders', 'Incomplete Orders'],
            ['04-08-19', 'ZCP', '57', '15', '35'],
            ['04-08-19', 'ZCP', '59', '32', '23'],
            ['04-08-19', 'ZCP', '88', '28', '21']
            ]

    with open(('order_report ' + datetime.datetime.now().strftime("%Y-%m-%d") + '.csv'), 'w') as fp:
            writer=csv.writer(fp,delimiter=',')
            writer.writerow(['Date', 'Customer Name', 'No of Orders', 'Submitted Orders', 'Incomplete Orders'])
            for row in data:
                writer.writerow(row)

#generate_csv()

def generate_excel(result):
    wb=xlsxwriter.Workbook('order_report ' + datetime.datetime.now().strftime("%Y-%m-%d") + '.xlsx')
    ws=wb.add_worksheet()
    row = 0
    column =0
    data = (['Date', 'Customer Name', 'No of Orders', 'Submitted Orders', 'Incomplete Orders'],
            ['04-08-19', 'ZCP', '57', '15', '35'],
            ['04-08-19', 'ZCP', '59', '32', '23'],
            ['04-08-19', 'ZCP', '88', '28', '21']
            )
    for date,cname,no,so,io in data:
        #ws.write(row,column,item)
        ws.write(row, column,date)
        ws.write(row, column+1,cname)
        ws.write(row, column + 2, no)
        ws.write(row, column + 3, so)
        ws.write(row, column + 4, io)
        row+=1
    wb.close()
#generate_excel()