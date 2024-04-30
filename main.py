# main.py
from requests import RequestException
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from routers.image_router import router as image_router
from routers.command_router import router as command_router

app = FastAPI()

# Include the router
app.include_router(image_router)
app.include_router(command_router)

@app.get("/", response_class=HTMLResponse)
def form():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Upload Image</title>
    </head>
    <body>
        <h1>Upload Image to FastAPI</h1>
        <form action="/analyze-image/hello" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit">
        </form>
    </body>
    </html>
    """

@app.exception_handler(RequestException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"message": "An error occurred while executing the command", "details": str(exc)}
    )