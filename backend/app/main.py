from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import members, consumptions, categories, products, materials, material_records

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Business Management System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(members.router)
app.include_router(consumptions.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(materials.router)
app.include_router(material_records.router)


@app.get("/")
def root():
    return {"message": "Business Management System API"}


@app.get("/api/health")
def health_check():
    return {"status": "ok"}
