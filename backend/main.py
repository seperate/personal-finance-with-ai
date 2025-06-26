from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(
    title="Personal Finance AI API",
    description="AI-powered personal finance management with PDF bank statement processing",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint - API health check"""
    return JSONResponse(
        content={
            "message": "Personal Finance AI API",
            "status": "healthy",
            "version": "1.0.0",
        }
    )


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse(
        content={"status": "healthy", "service": "Personal Finance AI API"}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
