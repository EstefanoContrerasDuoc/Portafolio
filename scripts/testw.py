from weasyprint import HTML, CSS
import os
def test():
    html = "<h1>Hola</h1>"
    css = CSS(string='h1 { color: red; }')
    HTML(string=html).write_pdf("test.pdf", stylesheets=[css])
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Sube a /proyecto
    css_path = os.path.join(BASE_DIR, 'static', 'css', 'estilos.css')

    print("Ruta absoluta esperada del CSS:")
    print(css_path)

    print("\n¿Existe el archivo?")
    print(os.path.isfile(css_path))
if __name__ == "__main__":
    test()