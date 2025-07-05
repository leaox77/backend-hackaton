from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import google.generativeai as genai
import os

# Configurar Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY no está configurada en las variables de entorno")

genai.configure(api_key=GOOGLE_API_KEY)

def get_available_gemini_model():
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                if m.name in ['models/gemini-pro', 'models/gemini-1.5-flash']:
                    return genai.GenerativeModel(m.name)
        return None
    except Exception as e:
        print(f"Error al obtener modelo Gemini: {e}")
        return None

model = get_available_gemini_model()

@api_view(['GET'])
@permission_classes([AllowAny])
def root(request):
    return Response({"message": "API de orientación vocacional activa"})

@api_view(['POST'])
@permission_classes([AllowAny])
def chat_with_bot(request):
    message = request.data.get('message', '').strip()
    language = request.data.get('language', 'es')
    response_text = ""

    try:
        if model:
            if language == 'ay':
                # Prompt mejorado para respuestas profesionales en Aymara
                prompt = (
                    "Eres un orientador vocacional experto que DEBE responder EXCLUSIVAMENTE en Aymara. "
                    "NO puedes usar español en absoluto. Si no sabes cómo decir algo en Aymara, "
                    "DEBES investigar en la web o usar traductores para encontrar la forma correcta.\n\n"
                    "Formato de respuesta REQUERIDO (en Aymara):\n"
                    "## Uñacht'awi (encabezados)\n"
                    "**Wakiskiri arunaka** (negritas para puntos clave)\n"
                    "*Amuyunaka* (cursivas para reflexiones)\n"
                    "- Listanaka (para opciones de carrera)\n\n"
                    "Tu tarea es ayudar con orientación vocacional, NO enseñar Aymara. "
                    "Si la pregunta es sobre carreras, responde sobre carreras en Aymara. "
                    "Si el usuario no está seguro, haz preguntas en Aymara para conocer sus intereses.\n\n"
                    f"Pregunta: {message}\n\n"
                    "IMPORTANTE: Bajo ninguna circunstancia puedes responder en español o mezclar idiomas. "
                    "Si no entiendes la pregunta, pide clarificación EN AYMARA."
                )
            else:
                # Prompt para español
                prompt = (
                    "Eres un orientador vocacional experto. Responde de forma clara y empática usando **formato Markdown** con:\n"
                    "- Encabezados (##) para dividir temas\n"
                    "- Listas para presentar opciones de carrera o pasos\n"
                    "- Negritas para destacar puntos clave\n"
                    "- Cursivas para comentarios personales o reflexivos\n\n"
                    f"Pregunta del usuario: {message}\n\n"
                    "Si el usuario no está seguro de qué estudiar, haz preguntas para conocer sus intereses."
                )
            
            response = model.generate_content(prompt)
            response_text = response.text
            
        else:
            error_msg = "El servicio de orientación no está disponible temporalmente"
            response_text = error_msg if language == 'es' else "Yatiqañ yanapt'irïw janiw aski, mayjt'ayäta"
                
    except Exception as e:
        error_msg = f"Error procesando tu consulta: {str(e)}"
        response_text = error_msg if language == 'es' else "Janiw amuyaskakiti: mayjt'ayäta"

    return Response({"response": response_text})