from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def save_pdf(text):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate("testcases.pdf")

    story = []

    for line in text.split("\n"):

        story.append(Paragraph(line, styles['Normal']))

    doc.build(story)