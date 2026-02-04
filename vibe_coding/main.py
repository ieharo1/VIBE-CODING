from fastapi import FastAPI

app = FastAPI(
    title="VIBE-CODING API",
    description="Enterprise inventory system with AI-powered features.",
    version="0.1.0",
)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the VIBE-CODING API"}


@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "ok"}
