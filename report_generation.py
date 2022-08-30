from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph


### =========Function========
def wraptext(row):
    arr = []
    for value in row:
        arr.append(Paragraph(value,styles['Normal']))
    return arr

def read_file():
    with open('report_variables.txt') as f:
        values = f.read().split()
    return values
# ==========================


styles = getSampleStyleSheet()
headings =  ['Standard Readings In °C', 'UUC Readings In °C', 'Deviation / Error In °C', 'Expanded Uncertainty In ±°C']
values = read_file()
headings = wraptext(headings)
values = wraptext(values)

document = SimpleDocTemplate("PDFs/table.pdf", pagesize=A4)
items = []
data= [headings, values]
t=Table(data, [1*inch,1*inch,1*inch,1*inch])
t.setStyle(TableStyle(
    [
    #('ALIGN',(1,1),(-2,-2),'RIGHT'),
    # ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
    # ('VALIGN',(0,0),(0,-1),'TOP'),
    # ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    # ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
    # ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, -1), (-1, -1), 20),
    ('INNERGRID', (0,0), (-1,-1), 1, colors.black),
    ('BOX', (0,0), (-1,-1), 1, colors.black),
    ]
))
items.append(t)
document.build(items)

class ExtractPDF:
    def __init__(self, filename='generated-pdf.pdf'):
        pass
    def create_table(self):
        pass
    def generate_pdf():
        pass
    def save_pdf(self):
        pass