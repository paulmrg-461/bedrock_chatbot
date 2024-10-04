from fastapi import APIRouter, UploadFile, File
from core.bedrock_client import BedrockClient
from services.pdf_extractor import PdfExtractor
from api.schemas import PromptRequest, PromptResponse

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

@router.post("/extract-pdf")
async def extract_pdf(file: UploadFile = File(...)):
    # Guardar el archivo temporalmente
    file_location = f"/tmp/{file.filename}"
    with open(file_location, "wb+") as f:
        f.write(file.file.read())
    
    # Usar PdfExtractor para extraer texto
    pdf_extractor = PdfExtractor(file_location)
    extracted_text = pdf_extractor.extract_text()

    return {"text": extracted_text}