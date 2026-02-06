from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Admin API Server")

# CORS 설정 - React와 통신하기 위해 필수
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # admin 페이지 개발 서버
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": 200, "message": "Admin API Server"}

@app.get("/api/test")
def test_endpoint():
    return {
        "status": 200,
        "message": "연동 테스트 성공!",
        "data": {
            "server": "admin",
            "timestamp": "2024-02-06"
        }
    }