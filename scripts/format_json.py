
from google import genai
import json

def formatear_datos(raw_data):

    
    prompt = """
Convierte el siguiente currículum al formato JSON. Los único campos obligatorios son "Nombre", "Contacto" (si hay más de un contacto que sea lista) y "Titulo" (encuentra su titulo). El resto de la información enfrascala en 4 Secciones 
Ejemplo: "Seccion1: El sumario del curriculum", "Seccion2: Experiencia del curriculum subseccion2:experiencia 2, subseccion3:experiencia3", "Seccion4: Sumario del usuario", "Seccion5: Pasatiempos", si encuentras más secciones enumeralas y crealas pero mantén la nomenclaruta de SeccionN 
y si esta seccion tiene más subsecciones hace una lista dentro de esta sección. Currículum a convertir:
""" + raw_data

    client = genai.Client(api_key="AIzaSyAX-Z4PrvJ8iBZtkYWPrbaPzv3ylX-qepQ") 

    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
        config={
        'response_mime_type': 'application/json'
    },

        
    )
    print(response.text)
    try:
        json_data = json.loads(response.text)
        print("JSON success")
        print(json_data)
        return json_data
    except json.JSONDecodeError:
        print("⚠️ El modelo no devolvió un JSON válido.")
        return None

if __name__ == "__main__":
    datos = formatear_datos()
    # Opcional: guardar en un archivo para usar después
    with open('datos_generados.json', 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)
