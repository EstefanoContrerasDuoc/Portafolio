from flask import Flask, request, render_template, redirect, url_for, send_file
import os
from scripts.extract_data import extract_raw_data
from scripts.format_json import formatear_datos
from scripts.fill_templates import fill_templates, generate_pdf_weasyprint


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'output'

# Ruta principal (Inicio)
@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        
        file = request.files['cv']
        if file and file.filename.endswith(('.pdf', '.docx')):
            limpiar_carpeta_uploads()
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            raw_data = extract_raw_data(filepath)
            json_data = formatear_datos(raw_data)
            output_paths = fill_templates(json_data)

            return redirect(url_for('download', file1=os.path.basename(output_paths[0]), file2=os.path.basename(output_paths[1])))

    return render_template('index.html')

# Descargar archivos
@app.route('/download')
def download():
    file1 = request.args.get('file1')
    file2 = request.args.get('file2')

    if not file1 or not file2:
        return "Error: Archivos no encontrados", 400

    return render_template('download.html', file1=file1, file2=file2)

@app.route('/download/<filename>')
def download_file(filename):
    path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if not os.path.exists(path):
        return f"Archivo no encontrado: {filename}", 404
    return send_file(path, as_attachment=True)

# Rutas estáticas sin funcionalidad
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def limpiar_carpeta_uploads():
    folder = app.config['UPLOAD_FOLDER']
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error eliminando {file_path}: {e}")


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
    app.run(debug=True)

