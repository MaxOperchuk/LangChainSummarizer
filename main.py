from fastapi import FastAPI
from schemas import TextInput
from transformers import pipeline
from services import exception_handler


app = FastAPI()

summarization_pipeline = pipeline(
    "summarization", model="sshleifer/distilbart-cnn-12-6"
)


@app.post("/summarize")
@exception_handler
async def summarize_text(text_input: TextInput):
    summary = summarization_pipeline(
        text_input.text, max_length=150, min_length=50, do_sample=False
    )
    return {"summary": summary[0]["summary_text"]}
