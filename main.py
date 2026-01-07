import sys
import uvicorn
from fastapi import FastAPI
from src.api.embedRouter.handleMapping import router as embed_router

app = FastAPI(title="Word2Vec Embedding Server")

app.include_router(embed_router)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port argument!")
            sys.exit(1)
    else:
        print("No port provided!")
        sys.exit(1)

    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
