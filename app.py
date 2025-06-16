from flask import Flask, request, render_template, redirect, url_for, send_file, flash, send_from_directory
import os
from werkzeug.utils import secure_filename
from scripts.extract_data import extract_raw_data
from scripts.format_json import formatear_datos
from scripts.fill_templates import fill_templates

app = Flask(__name__)
app.secret_key = 'una_clave_muy_secreta_aleatoria'

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'output'
ALLOWED_EXTENSIONS = {'.pdf', '.docx'}

# Verifica que el archivo tenga una extensión válida
def allowed_file(filename):
    return os.path.splitext(filename)[1].lower() in ALLOWED_EXTENSIONS

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('cv')

        if file and allowed_file(file.filename):
            limpiar_carpeta(app.config['UPLOAD_FOLDER'])
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            try:
                raw_data = extract_raw_data(filepath)
                print("Texto extraído del archivo:\n", raw_data)

                json_data = formatear_datos(raw_data)
                print("✅ JSON generado correctamente.")

                output_paths = fill_templates(json_data)
                print("Archivos generados:", output_paths)

                # Validar que los archivos realmente existan
                if len(output_paths) < 2 or not all(os.path.exists(p) for p in output_paths):
                    raise Exception("❌ No se generaron correctamente los archivos PDF.")

                return redirect(url_for('download',
                                        file1=os.path.basename(output_paths[0]),
                                        file2=os.path.basename(output_paths[1])))

            except Exception as e:
                print(f"❌ Error en procesamiento: {e}")
                flash(f"Error al procesar el CV: {e}")
                return render_template('index.html')

        else:
            flash("Por favor, sube un archivo válido (.pdf o .docx)")
            return render_template('index.html')

    return render_template('index.html')

# Página con enlaces de descarga
@app.route('/download')
def download():
    file1 = request.args.get('file1')
    file2 = request.args.get('file2')

    if not file1 or not file2:
        return "Error: Archivos no encontrados", 400

    return render_template('download.html', file1=file1, file2=file2)

# Endpoint para descargar archivos individuales como attachment
@app.route('/download/<filename>')
def download_file(filename):
    path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if not os.path.exists(path):
        return f"Archivo no encontrado: {filename}", 404
    return send_file(path, as_attachment=True)

# Nuevo endpoint para servir archivos PDF directamente para la previsualización
@app.route('/output/<path:filename>')
def output_files(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

@app.route('/about')
def about():
    return render_template('about.html')


# Limpia la carpeta de archivos subidos
def limpiar_carpeta(folder):
    os.makedirs(folder, exist_ok=True)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error eliminando {file_path}: {e}")

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/instrucciones')
def instrucciones():
    return render_template('instrucciones.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/objetivo')
def objetivo():
    return render_template('objetivo.html')

@app.route('/index')
def home():
    return render_template('index.html')
    
if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
    app.run(debug=True)
