
from google import genai
import json

def formatear_datos(raw_data):

    
    prompt = """
Quiero que tomes generes un diccionario JSON con el siguiente curriculum, campos obligatorios siendo Nombre, profesion y contacto(si tiene más de uno contactoN).

El resto tiene que ser seccion1, seccion2, seccion3 y seccion4 máximo 4 macrosecciones. Si encuentras experiencia laboral o educación, la priorizas en seccion 1 y 2, priorizar sumario en seccion 3.

Si dentro de cada seccion encuentras mas de un item entonces separalo como seccion1, seccion1_n y así sucesivamente. ejemplo de estructura

{

"Nombre": "María Fernanda Rodríguez Gómez",

"profesion": "Ingeniera de Sistemas",

"contacto": null,


"seccion1":"Experiencia laboral ",

"seccion1_1": "Arquitecta de Software en Soluciones Fintech Avanzadas S.A. (2021-actualidad) Encargada del diseño y la evolución de la arquitectura de una plataforma de pagos digitales con más de 100 mil usuarios activos. Coordinación de equipo de 10 desarrolladores. Migración de monolito a microservicios utilizando Spring Boot, Docker, Kubernetes y RabbitMQ. Implementación de políticas de seguridad con OAuth2 y autenticación multifactor. Desarrollo de pruebas automatizadas y CI/CD con Jenkins y GitLab. Logros: reducción del 40% en tiempos de respuesta de la API y mejora del 99.9% en disponibilidad.",

"seccion1_2": "Desarrolladora Senior Backend en Grupo Educativo GlobalNet (2018-2021) Participación en el desarrollo de una plataforma de gestión académica para universidades. Lenguajes usados: Java, Python, PostgreSQL, Redis. Integración de servicios externos como PayPal y Google Drive. Mejora del rendimiento de consultas complejas mediante reestructuración de índices. Apoyo en definición de requerimientos con stakeholders y mejora de procesos mediante metodologías ágiles Scrum y Kanban.",

"seccion1_3": "Desarrolladora Full Stack Junior en MedData Solutions (2015-2018) Desarrollo de funcionalidades nuevas para un sistema hospitalario basado en Django y Angular. Automatización de reportes estadísticos en Excel y PDF. Soporte a usuarios y resolución de bugs.",

"seccion2": "Formación",

"seccion2_1": "Ingeniería de Sistemas, Universidad de los Andes, Colombia (2010-2015). Promedio: 4.5/5. Trabajo de grado sobre análisis de datos clínicos con machine learning.",

"seccion3": "Sumario",

"seccion3_1": "Profesional en Ingeniería de Sistemas con más de 8 años de experiencia en análisis, diseño, desarrollo e implementación de soluciones tecnológicas en sectores financiero, educativo y de salud. Especializada en desarrollo backend con Java y Python, arquitectura de microservicios y bases de datos relacionales y no relacionales.",

"seccion4": "Certificaciones",

"seccion4_1": "Oracle Certified Professional Java SE 11, AWS Certified Solutions Architect Associate, Curso Avanzado de Arquitectura de Software en Platzi, Certificado Scrum Master (Scrum.org).",

"seccion4_2": "Java, Python, Spring Boot, Django, PostgreSQL, MongoDB, Redis, Kafka, Git, Docker, Kubernetes, Jenkins, REST, GraphQL, TDD, Clean Architecture.",

"seccion4_3": "Español (nativo), Inglés (avanzado - TOEFL 107), Francés (intermedio).",

"seccion4_4": "liderazgo técnico, pensamiento analítico, comunicación efectiva, trabajo bajo presión, documentación técnica, diseño de soluciones escalables.",

"seccion4_5": "API REST para control de tareas con Django y JWT, sistema de recomendaciones de películas con ML, participación en hackatones de innovación financiera.",

"seccion4_6": "inteligencia artificial, educación tecnológica, viajes, voluntariado digital."

}



Curriculum a convertir:


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
