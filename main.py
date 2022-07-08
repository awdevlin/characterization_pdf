# Python program to create
# a pdf file
from fpdf import FPDF

# define constants for the document

chip_id = 'SM21A-AUR-R02-L128H2'
fab_date = 'YYYY-MMMM-DD'
assembly_date = 'YYYY-MMMM-DD'
title_line = 1

# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font for the title
pdf.set_font("comicsans", style='B', size=15)

# create title
pdf.cell(200, 10, txt="Characterization report for chip " + chip_id,
         ln=title_line, align='C')

# set style and size of font for the rest of the document
pdf.set_font("Arial", size=11)

# fabrication date
fab_line = title_line + 3
pdf.cell(200, 10, txt="Chip fabrication date: " + fab_date,
         ln=fab_line, align='L')


# assembly date
assembly_line = fab_line + 1
pdf.cell(200, 10, txt="Chip fabrication date: " + assembly_date,
         ln=assembly_line, align='L')

# name = "fab_details.png"
# pdf.image(name, x=None, y=None, w=0, h=0)

# save the pdf with name .pdf
pdf.output("Characterization Report - " + chip_id + ".pdf")
