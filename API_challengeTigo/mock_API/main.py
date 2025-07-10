from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, Response, PlainTextResponse
from uuid import uuid4
from models import MockConfig, MatchRule
from storage import storage
from utils import match_request, render_template

app = FastAPI()

@app.post("/configure-mock")
def configure_mock(mock: MockConfig):
    mock.id = str(uuid4())
    storage.append(mock)
    return {"id": mock.id, "message": "Mock configurado exitosamente"}

@app.get("/configure-mock")
def list_mocks():
    return storage

@app.delete("/configure-mock/{mock_id}")
def delete_mock(mock_id: str):
    for i, mock in enumerate(storage):
        if mock.id == mock_id:
            del storage[i]
            return {"message": "Mock eliminado"}
    raise HTTPException(status_code=404, detail="Mock no encontrado")

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
async def catch_all(request: Request, path: str):
    body = await request.body()
    incoming = {
        "method": request.method,
        "path": f"/{path}",
        "query": dict(request.query_params),
        "headers": dict(request.headers),
        "body": body.decode("utf-8") if body else ""
    }

    for mock in storage:
        if match_request(incoming, mock):
            content = render_template(mock.response_content, incoming)
            response_class = JSONResponse if mock.content_type == "application/json" else PlainTextResponse
            return response_class(content=content, status_code=mock.status_code, media_type=mock.content_type)

    raise HTTPException(status_code=404, detail="Mock no encontrado")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)

