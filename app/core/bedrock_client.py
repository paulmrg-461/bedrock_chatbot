import boto3
import json

class BedrockClient:
    def __init__(self, region_name='us-west-2'):
        self.client = boto3.client('bedrock-runtime', region_name=region_name)

    def invoke_model(self, model_id, prompt, max_tokens_to_sample=100):
        try:
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

            result = ""
            for event in response['body']:
                chunk = event.get('chunk', {})
                if 'bytes' in chunk:
                    event_data = chunk['bytes'].decode('utf-8')
                    event_json = json.loads(event_data)
                    if 'completion' in event_json:
                        result += event_json['completion']
            return result
        except Exception as e:
            print(f"Error al invocar el modelo: {str(e)}")
            return None
