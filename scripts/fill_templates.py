from weasyprint import HTML
import os
from flask import render_template

def generate_pdf_weasyprint(html_content, output_path):
    HTML(string=html_content).write_pdf(output_path)

def fill_templates(json_data):
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    # Renderizar template1
    rendered_html1 = render_template('template1.html', **json_data)
    output_path1 = os.path.join(output_dir, 'plantilla1.pdf')
    generate_pdf_weasyprint(rendered_html1, output_path1)

    # Renderizar template2
    rendered_html2 = render_template('template2.html', **json_data)
    output_path2 = os.path.join(output_dir, 'plantilla2.pdf')
    generate_pdf_weasyprint(rendered_html2, output_path2)

    return [output_path1, output_path2]
