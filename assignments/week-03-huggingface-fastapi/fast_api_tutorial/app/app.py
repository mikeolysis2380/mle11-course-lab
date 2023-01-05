from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from transformers import pipeline
pipeline = pipeline('translation_en_to_fr',model ='model/translation_model')
pipeline = pipeline('translation_en_to_fr',model ='t5-small')

app = FastAPI()

class TextToTranslate(BaseModel):
    input_texts:List(str)

class TextToTranslate(BaseModel):
    input_texts:List(str)

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}

@app.post("/translate")
def echo(text_to_translate: TextToTranslate):
    return {"message": pipeline(text_to_translate.input_text)}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)