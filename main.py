from fastapi import FastAPI
from transformers import pipeline


app = FastAPI()

summarization_pipeline = pipeline("summarization")
