from fpdf import FPDF
import pandas as pd
import datetime
now = datetime.datetime.now()
title = 'Order Report for Customers'

class PDF(FPDF):
    def header(self, spacing=2):
        # Arial bold 15
        self.set_font('Arial', 'B', 10)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)
        self.data=[['Date', 'Customer Name', 'No of Orders', 'Submitted Orders','Incomple Orders'],
                   ['04-08-19', 'ZCP', '57', '15','35'],['04-08-19', 'ZCP', '59','32','23'],
                   ['04-08-19', 'ZCP', '88','28','21']]
        self.col_width = pdf.w / 4.5
        self.row_height = pdf.font_size
        col_width = pdf.w / 4.5
        row_height = pdf.font_size
        for row in self.data:
            print(row)
            for item in row:
                print(item)
                pdf.cell(self.col_width, self.row_height * spacing,
                         txt=item, border=1)
        #pdf.output('report/simple_table.pdf')

        df = pd.DataFrame()
        df['Date'] = ["now"]

spacing=2
pdf = PDF()
pdf.set_title(title)
pdf.set_author('Jyotismita Tripathy')
#pdf.set_font("Arial", size=10)
#pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_c1.txt')
#pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
pdf.output('report/tuto1.pdf', 'F')
#print (pdf.self.data)
col_width = pdf.w / 4.5
#row_height = pdf.font_size

