import io
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, JSONResponse
app = FastAPI()

@app.post("/generate-image-dalle")
def generate_image_dalle(prompt:str):
    
    try:
        image = stable_diffusion_predictor.call(prompt=prompt)
        stream = io.BytesIO()
        image.save(stream, format="PNG")
        stream.seek(0)
        return StreamingResponse(stream, media_type="image/png")
    except ValueError():
        return JSONResponse(
        status_code=418,
        content={"message": f"Oops! the prompt is empty. Please try again"},
    )
