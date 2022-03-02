from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

import img_change
app = FastAPI()

class ImgRequest(BaseModel):
    img:str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/transform")
async def api_endpoint(transform:ImgRequest):
    transformed_img = img_change.img_encode(img_change.imgToGray(img_change.img_decode(transform.img)))
    return {"img":transformed_img}

