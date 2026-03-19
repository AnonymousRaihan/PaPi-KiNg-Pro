from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Active", "message": "PaPi BG Remover API is running!"}

@app.post("/remove-bg/")
async def remove_background(file: UploadFile = File(...)):
    try:
        input_image = await file.read()
        output_image = remove(input_image)
        return Response(content=output_image, media_type="image/png")
    
    except Exception as e:
        return {"error": str(e)}
