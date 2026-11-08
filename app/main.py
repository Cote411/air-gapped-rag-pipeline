from fastapi import FastAPI

app = FastAPI(title="Airgap RAG", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


# /ingest, /query, /metrics are added in phase 2 of the build.
