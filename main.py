# Python program to create
# a pdf file
from fpdf import FPDF

# define constants for the document

chip_id = 'SM21A-AUR-R02-L128H2'
fab_date = '2022-June-20'
assembly_date = '2022-June-20'
title_line = 1

def default_font():
    pdf.set_font("Arial", style='', size=11)

def title_font():
    pdf.set_font("Arial", style='B', size=15)

def header_font():
    pdf.set_font("Arial", style='BU', size=13)


def create_table_header(col_names, col_width, line_height):
    pdf.set_font("Arial", style="B")  # enabling bold text
    pdf.set_fill_color(150)
    for col_name in col_names:
        pdf.cell(col_width, line_height, col_name, border=1, fill=True, align='C')
    pdf.ln(line_height)
    default_font()


def create_table(col_names, data):
    line_height = pdf.font_size * 1.5
    col_width = pdf.w / 2 * 0.90
    fill = False
    create_table_header(col_names, col_width, line_height)
    for _ in range(1):  # repeat data rows
        for row in data:
            fill = ~fill
            for datum in row:
                if fill:
                    pdf.set_fill_color(220)
                    pdf.cell(col_width, line_height, datum, border=1, fill=True)
                else:
                    pdf.cell(col_width, line_height, datum, border=1)
            pdf.ln(line_height)
        pdf.ln(line_height)


# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font for the title
title_font()

# create title
pdf.cell(200, 10, txt="Characterization report for chip " + chip_id,
         ln=title_line, align='C')

# set style and size of font for the rest of the document
default_font()

# fabrication date
fab_line = title_line + 3
pdf.cell(200, 10, txt="Chip fabrication date: " + fab_date,
         ln=fab_line, align='L')

# assembly date
assembly_line = fab_line + 1
pdf.cell(200, 10, txt="Chip fabrication date: " + assembly_date,
         ln=assembly_line, align='L')


transducer_design_line = assembly_line + 1
header_font()
pdf.cell(200, 10, txt="1. Transducer Design",
         ln=assembly_line, align='L')

# create a table with fabrication details
fab_col_names = ("Parameter", "Value")
fab_data = (
    ("#of channels", "128"),
    ("Chip footprint", "43 x 11mm"),
    ("Array footprint", "41.009 x 8.086mm"),
    ("Element spacing (kerf)", "5um"),
    ("Pitch", "320um"),
    ("Cells per element", "4 x 141 = 564"),
    ("Fill Factor", "85.5%"),
    ("Membrane / electrode diameter", "58um, 50um"),
    ("Spacing between cells", "8um"),
    ("Cell-to-cell distance (min / max)", "66um / 66um"),
    ("Electrode interconnection width", "20um"),
    ("Contact pad size", "500 x 700um"),
    ("Etch channel width", "6um"),
    ("Polymer 2 membrane diameter", "78um"),
)

create_table(fab_col_names, fab_data)

# include images of a chip, elements, and cells
name = "demo_images.jpg"
pdf.image(name, x=None, y=None, w=pdf.w * 0.9, h=0)

# save the pdf with name .pdf
pdf.output("Characterization Report - " + chip_id + ".pdf")
