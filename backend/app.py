from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pdf_reader import read_pdf
from rag_pipeline import build_vector
from llm import generate_testcases
from exporter_pdf import save_pdf
from exporter_json import save_json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "RAG Backend is running!"}
@app.post("/generate")
async def generate(file: UploadFile):
    try:
        text = read_pdf(file.file)

        vector = build_vector(text)

        context = text[:4000]

        result = generate_testcases(context)

        save_pdf(result)

        save_json(result)

        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}