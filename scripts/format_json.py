
from google import genai
import json

def formatear_datos(raw_data):

    
    prompt = """Formatea este curriculum a JSON con los siguientes campos obligatorios: nombre:, sumario:, experiencia:, competencias:, contacto:, formacion:."""+raw_data

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
