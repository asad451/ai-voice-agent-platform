from fastapi import FastAPI

app = FastAPI(
    title="AI Voice Agent Platform",
    description="AI-powered lead communication platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "message": "AI Voice Agent Platform API",
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }