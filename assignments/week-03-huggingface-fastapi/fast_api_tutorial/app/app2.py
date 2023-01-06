from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from transformers import pipeline

pipeline = pipeline('translation_en_to_fr',model ='model/translation_model')
pipeline = pipeline('translation_en_to_fr',model ='t5-small')


class TextToTranslate(BaseModel):
    input_texts:List(str)

app = FastAPI()


@app.post("/translate")
def echo(text_to_translate: TextToTranslate):
    return {"message": pipeline(text_to_translate.input_texts)}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app2", host="0.0.0.0", port=8000, reload=True)