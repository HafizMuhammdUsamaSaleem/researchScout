from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "AI Research Assistant Report", ln=True, align='C')
        self.ln(10)

def add_section_title(pdf, title):
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, title, ln=True)
    pdf.ln(4)

def add_subsection(pdf, heading, content):
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, heading, ln=True)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 6, content)
    pdf.ln(3)

def generate_pdf(query, search_results, summary_results, relevance_results):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(15, 15, 15)

    # Query
    add_section_title(pdf, "Query:")
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 6, query)
    pdf.ln(6)

    # Search Results
    add_section_title(pdf, "Search Results:")
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 6, search_results)
    pdf.ln(6)

    # Summary
    add_section_title(pdf, "Summary:")
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 6, summary_results)
    pdf.ln(6)

    # Relevance
    add_section_title(pdf, "Relevance Evaluation:")
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 6, relevance_results)

    return pdf.output(dest="S").encode("latin-1")
