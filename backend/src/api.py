import io
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, JSONResponse
from .models.dalle_predictor import DallePredictor

app = FastAPI()

dalle_predictor = DallePredictor()


@app.post("/generate-image-dalle")
async def generate_image_dalle(prompt: str):

    try:
        image = await dalle_predictor.predict(prompt)
        stream = io.BytesIO()
        image.save(stream, format="PNG")
        stream.seek(0)
        return StreamingResponse(stream, media_type="image/png")
    except Exception():
        return JSONResponse(
            status_code=418,
            content={"message": f"Oops! Some error happened. Please try again"},
        )
