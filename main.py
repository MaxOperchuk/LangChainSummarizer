from fastapi import FastAPI
from schemas import TextInput
from transformers import pipeline
from services import exception_handler
from langchain_huggingface import HuggingFacePipeline


app = FastAPI()

# Initialize the summarization pipeline.
summarization_pipeline = pipeline(
    "summarization", model="sshleifer/distilbart-cnn-12-6"
)

# Wrap the pipeline in a LangChain model
summarizer = HuggingFacePipeline(pipeline=summarization_pipeline)


@app.post("/summarize")
@exception_handler
async def summarize_text(text_input: TextInput) -> dict:
    """
    Endpoint to summarize the input text using a pre-trained summarization model.
    """

    summary = summarizer(text_input.text)
    return {"summary": summary}
