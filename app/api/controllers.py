from fastapi import APIRouter, Depends
from app.core.bedrock_client import BedrockClient
from app.api.schemas import PromptRequest, PromptResponse

router = APIRouter()

# Inicializamos el cliente de Bedrock
bedrock_client = BedrockClient()

@router.post("/generate-response", response_model=PromptResponse)
async def generate_response(request: PromptRequest):
    # Llamada a Bedrock con el prompt
    result = bedrock_client.invoke_model(
        model_id='anthropic.claude-v2:1',
        prompt=request.prompt
    )
    return PromptResponse(response=result)
