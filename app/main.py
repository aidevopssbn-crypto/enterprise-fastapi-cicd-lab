from fastapi import FastAPI

app = FastAPI(title="Enterprise CI/CD FastAPI Lab", version="1.0.0")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Enterprise CI/CD lab is running"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
