from fastapi import APIRouter
from pydantic import BaseModel, Field
from src.embeddings.embedText import embedTextInstance

router = APIRouter()

class EmbedRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to embed")

class EmbedResponse(BaseModel):
    status: str
    embedding: list | None

@router.post("/embed", response_model=EmbedResponse)
def embed_text_endpoint(request: EmbedRequest):
    embedding = embedTextInstance.get_embedding(request.text)

    if embedding is None:
        return {"status": "Failure", "embedding": None}
    if not embedding:
        return {"status": "Failure", "embedding": []}

    return {"status": "Success", "embedding": embedding}
