# from fastapi import FastAPI, HTTPException, Depends
# from sqlalchemy import create_engine, Column, Integer, Float, Date, Time
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from pydantic import BaseModel
# from datetime import datetime

# # # Database setup
# DATABASE_URL = "sqlite:///./test.db"  # Using SQLite for simplicity

# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # SQLAlchemy model
# class Data(Base):
#     __tablename__ = "data"
#     id = Column(Integer, primary_key=True, index=True)
#     current_date = Column(Date, nullable=False)
#     current_time = Column(Time, nullable=False)
#     x = Column(Float, nullable=False)
#     y = Column(Float, nullable=False)
#     z = Column(Float, nullable=False)

# # Create the database table(s)
# Base.metadata.create_all(bind=engine)

# # Pydantic models
# class DataCreate(BaseModel):
#     x: float
#     y: float
#     z: float

# class DataResponse(BaseModel):
#     id: int
#     current_date: datetime
#     current_time: datetime
#     x: float
#     y: float
#     z: float

#     class Config:
#         orm_mode = True

# # FastAPI app instance
# app = FastAPI()

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # # POST endpoint to create a new record with current date and time
# # @app.post("/data/", response_model=DataResponse)
# # def create_data(item: DataCreate, db: Session = Depends(get_db)):
# #     now = datetime.now()
# #     db_item = Data(
# #         current_date=now.date(),
# #         current_time=now.time(),
# #         x=item.x,
# #         y=item.y,
# #         z=item.z
# #     )
# #     db.add(db_item)
# #     db.commit()
# #     db.refresh(db_item)
# #     return db_item

# # GET endpoint to retrieve all records
# @app.get("/data/", response_model=list[DataResponse])
# def read_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = db.query(Data).offset(skip).limit(limit).all()
#     return items

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

# # # To run the app, use: uvicorn main:app --reload
# # # if __name__ == "__main__":
# # #     import uvicorn
# # #     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
# #     # Note: In a production environment, you would not use reload=True.
# #     # This is just for development purposes to auto-reload the server on code changes.
# # # Test the API with curl or Postman


# # from fastapi import FastAPI

# # app = FastAPI()

# # @app.get("/")
# # def read_root():
# #     return {"message": "Hello, World!"}



from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, Float, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from datetime import date, time

# Replace with your PostgreSQL connection details
DATABASE_URL = "postgresql://espuser:lcmQ50EMkDy3KfGmbIRzKuMLnKFpUDy2@dpg-cvoam3hr0fns739j680g-a.singapore-postgres.render.com/espapiep?sslmode=require"

engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy model
class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    current_date = Column(Date, nullable=False)
    current_time = Column(Time, nullable=False)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, nullable=False)

# Create the database table(s)
Base.metadata.create_all(bind=engine)

# Pydantic models
class DataCreate(BaseModel):
    x: float
    y: float
    z: float

class DataResponse(BaseModel):
    id: int
    current_date: date
    current_time: time
    x: float
    y: float
    z: float

    class Config:
        orm_mode = True

# FastAPI app instance
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST endpoint to create a new record with current date and time
@app.post("/data/", response_model=DataResponse)
def create_data(item: DataCreate, db: Session = Depends(get_db)):
    now = datetime.now()
    db_item = Data(
        current_date=now.date(),
        current_time=now.time(),
        x=item.x,
        y=item.y,
        z=item.z
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# GET endpoint to retrieve all records
@app.get("/data/", response_model=list[DataResponse])
def read_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(Data).offset(skip).limit(limit).all()
    return items

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
