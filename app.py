from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/log-request")
async def log_request(request: Request):

    # Log request headers
    print("Request Headers:")
    for key, value in request.headers.items():
        print(f"{key}: {value}")
    
    # Log query parameters
    print("Query Parameters:")
    for key, value in request.query_params.items():
        print(f"{key}: {value}")

    # Log request body
    body = await request.body()
    print(f"Request Body: {body.decode()}")

    return {"message": "Request logged successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
