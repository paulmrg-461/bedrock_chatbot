import boto3
import json

class BedrockClient:
    def __init__(self, region_name='us-west-2'):
        """
        Inicializa el cliente de Amazon Bedrock Runtime en la región especificada.
        :param region_name: La región donde está disponible Amazon Bedrock (us-west-2 en este caso).
        """
        self.client = boto3.client('bedrock-runtime', region_name=region_name)
    
    def invoke_model(self, model_id, prompt, max_tokens_to_sample=100):
        """
        Invoca el modelo de Amazon Bedrock con un prompt dado.
        
        :param model_id: El ID del modelo (ej. 'anthropic.claude-v2:1').
        :param prompt: El texto de entrada que deseas enviar al modelo.
        :param max_tokens_to_sample: El número máximo de tokens que debe generar la respuesta.
        :return: La respuesta generada por el modelo.
        """
        try:
            # Formato correcto para Claude v2.1 con "Human:" como se requiere
            body = json.dumps({
                "prompt": f'Human: {prompt}\nAssistant:',
                "max_tokens_to_sample": max_tokens_to_sample
            })

            response = self.client.invoke_model_with_response_stream(
                modelId=model_id,
                contentType="application/json",
                accept="application/json",
                body=body
            )

            # Leer el evento desde el stream
            result = ""
            for event in response['body']:
                try:
                    # Acceder al campo 'bytes' dentro de 'chunk' y decodificarlo
                    chunk = event.get('chunk', {})
                    if 'bytes' in chunk:
                        event_data = chunk['bytes'].decode('utf-8')
                        event_json = json.loads(event_data)  # Convertir de nuevo a JSON
                        
                        # Verificar si el fragmento contiene texto de completación
                        if 'completion' in event_json:
                            result += event_json['completion']
                except Exception as decode_error:
                    print(f"Error al procesar el evento: {str(decode_error)}")
                    continue

            return result
        except Exception as e:
            print(f"Error al invocar el modelo: {str(e)}")
            return None

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia del cliente Bedrock Runtime
    bedrock_client = BedrockClient()

    # Especificar el ID del modelo Claude y el prompt
    model_id = 'anthropic.claude-v2:1'
    prompt = "Como recorrer en python una lista de strings e imprimir cada elemento?" 

    # Invocar el modelo
    result = bedrock_client.invoke_model(model_id, prompt)

    if result:
        print("Respuesta del modelo:")
        print(result)
    else:
        print("No se pudo obtener la respuesta del modelo.")
