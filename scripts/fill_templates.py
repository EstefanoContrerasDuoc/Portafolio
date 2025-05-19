import os
from weasyprint import HTML, CSS
from flask import render_template

def generate_pdf_weasyprint(html_content, output_path,css_path=None):

    print(f"Generando PDF para: {output_path} con CSS: {css_path}")
    if css_path:

        css_stylesheet = CSS(filename=css_path)

        HTML(string=html_content).write_pdf(output_path, stylesheets=[css_stylesheet])

    else:

        print(f"Error al cargar el CSS {css_path}: {e}")

        HTML(string=html_content).write_pdf(output_path)

def fill_templates(json_data):
    

    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    css_path = os.path.join(BASE_DIR, 'static', 'css', 'estilos.css')
    css_path_absoluto = os.path.abspath(css_path)
    css_path1 = os.path.join(BASE_DIR, 'static', 'css', 'estilos1.css')
    css_path_absoluto1 = os.path.abspath(css_path1)
    print("--------------TEST: Ruta CSS:--------------", css_path_absoluto)
    print("--------------TEST: Existe?--------------", os.path.isfile(css_path_absoluto))
    # Renderizar template1
    rendered_html1 = render_template('template1.html', **json_data)
    output_path1 = os.path.join(output_dir, 'plantilla1.pdf')
    generate_pdf_weasyprint(rendered_html1, output_path1, css_path_absoluto)

    # Renderizar template2
    rendered_html2 = render_template('template2.html', **json_data)
    output_path2 = os.path.join(output_dir, 'plantilla2.pdf')
    generate_pdf_weasyprint(rendered_html2, output_path2, css_path_absoluto1)


    return [output_path1, output_path2]


