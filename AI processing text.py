import openai

# Configurar tu clave de API de OpenAI
openai.api_key = 'tu_clave_de_api_aqui'

# Definir una función para generar texto
def generar_texto(prompt):
    respuesta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None
    )
    return respuesta.choices[0].text.strip()

# Solicitar un prompt al usuario
prompt_usuario = input("Ingresa un prompt: ")

# Generar texto utilizando el prompt proporcionado
texto_generado = generar_texto(prompt_usuario)

# Imprimir el texto generado
print(texto_generado)
