# # # # from fastapi import FastAPI, HTTPException, Depends
# # # # from sqlalchemy import create_engine, Column, Integer, Float, Date, Time
# # # # from sqlalchemy.ext.declarative import declarative_base
# # # # from sqlalchemy.orm import sessionmaker, Session
# # # # from pydantic import BaseModel
# # # # from datetime import datetime

# # # # # # Database setup
# # # # DATABASE_URL = "sqlite:///./test.db"  # Using SQLite for simplicity

# # # # engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# # # # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# # # # Base = declarative_base()

# # # # # SQLAlchemy model
# # # # class Data(Base):
# # # #     __tablename__ = "data"
# # # #     id = Column(Integer, primary_key=True, index=True)
# # # #     current_date = Column(Date, nullable=False)
# # # #     current_time = Column(Time, nullable=False)
# # # #     x = Column(Float, nullable=False)
# # # #     y = Column(Float, nullable=False)
# # # #     z = Column(Float, nullable=False)

# # # # # Create the database table(s)
# # # # Base.metadata.create_all(bind=engine)

# # # # # Pydantic models
# # # # class DataCreate(BaseModel):
# # # #     x: float
# # # #     y: float
# # # #     z: float

# # # # class DataResponse(BaseModel):
# # # #     id: int
# # # #     current_date: datetime
# # # #     current_time: datetime
# # # #     x: float
# # # #     y: float
# # # #     z: float

# # # #     class Config:
# # # #         orm_mode = True

# # # # # FastAPI app instance
# # # # app = FastAPI()

# # # # # Dependency to get DB session
# # # # def get_db():
# # # #     db = SessionLocal()
# # # #     try:
# # # #         yield db
# # # #     finally:
# # # #         db.close()

# # # # # # POST endpoint to create a new record with current date and time
# # # # # @app.post("/data/", response_model=DataResponse)
# # # # # def create_data(item: DataCreate, db: Session = Depends(get_db)):
# # # # #     now = datetime.now()
# # # # #     db_item = Data(
# # # # #         current_date=now.date(),
# # # # #         current_time=now.time(),
# # # # #         x=item.x,
# # # # #         y=item.y,
# # # # #         z=item.z
# # # # #     )
# # # # #     db.add(db_item)
# # # # #     db.commit()
# # # # #     db.refresh(db_item)
# # # # #     return db_item

# # # # # GET endpoint to retrieve all records
# # # # @app.get("/data/", response_model=list[DataResponse])
# # # # def read_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
# # # #     items = db.query(Data).offset(skip).limit(limit).all()
# # # #     return items

# # # # @app.get("/")
# # # # def read_root():
# # # #     return {"message": "Hello, World!"}

# # # # # # To run the app, use: uvicorn main:app --reload
# # # # # # if __name__ == "__main__":
# # # # # #     import uvicorn
# # # # # #     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
# # # # #     # Note: In a production environment, you would not use reload=True.
# # # # #     # This is just for development purposes to auto-reload the server on code changes.
# # # # # # Test the API with curl or Postman


# # # # # from fastapi import FastAPI

# # # # # app = FastAPI()

# # # # # @app.get("/")
# # # # # def read_root():
# # # # #     return {"message": "Hello, World!"}



# # # from fastapi import FastAPI, HTTPException, Depends
# # # from sqlalchemy import create_engine, Column, Integer, Float, Date, Time
# # # from sqlalchemy.ext.declarative import declarative_base
# # # from sqlalchemy.orm import sessionmaker, Session
# # # from pydantic import BaseModel
# # # from datetime import date, time

# # # # Replace with your PostgreSQL connection details
# # # DATABASE_URL = "postgresql://espuser:lcmQ50EMkDy3KfGmbIRzKuMLnKFpUDy2@dpg-cvoam3hr0fns739j680g-a.singapore-postgres.render.com/espapiep?sslmode=require"

# # # engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})
# # # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# # # Base = declarative_base()

# # # # SQLAlchemy model
# # # class Data(Base):
# # #     __tablename__ = "data"
# # #     id = Column(Integer, primary_key=True, index=True)
# # #     current_date = Column(Date, nullable=False)
# # #     current_time = Column(Time, nullable=False)
# # #     x = Column(Float, nullable=False)
# # #     y = Column(Float, nullable=False)
# # #     z = Column(Float, nullable=False)

# # # # Create the database table(s)
# # # Base.metadata.create_all(bind=engine)

# # # # Pydantic models
# # # class DataCreate(BaseModel):
# # #     x: float
# # #     y: float
# # #     z: float

# # # class DataResponse(BaseModel):
# # #     id: int
# # #     current_date: date
# # #     current_time: time
# # #     x: float
# # #     y: float
# # #     z: float

# # #     class Config:
# # #         orm_mode = True

# # # # FastAPI app instance
# # # app = FastAPI()

# # # # Dependency to get DB session
# # # def get_db():
# # #     db = SessionLocal()
# # #     try:
# # #         yield db
# # #     finally:
# # #         db.close()

# # # # POST endpoint to create a new record with current date and time
# # # @app.post("/data/", response_model=DataResponse)
# # # def create_data(item: DataCreate, db: Session = Depends(get_db)):
# # #     now = datetime.now()
# # #     db_item = Data(
# # #         current_date=now.date(),
# # #         current_time=now.time(),
# # #         x=item.x,
# # #         y=item.y,
# # #         z=item.z
# # #     )
# # #     db.add(db_item)
# # #     db.commit()
# # #     db.refresh(db_item)
# # #     return db_item

# # # # GET endpoint to retrieve all records
# # # @app.get("/data/", response_model=list[DataResponse])
# # # def read_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
# # #     items = db.query(Data).offset(skip).limit(limit).all()
# # #     return items

# # # @app.get("/")
# # # def read_root():
# # #     return {"message": "Hello, World!"}






# # from fastapi import FastAPI, HTTPException, Depends
# # from pydantic import BaseModel
# # from datetime import datetime, date, time
# # from sqlalchemy import create_engine, Column, Integer, Float, Date, Time
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy.orm import sessionmaker, Session
# # from typing import List

# # # Replace with your actual PostgreSQL connection string
# # DATABASE_URL = "postgresql://your_user:your_password@your_host:your_port/your_db?sslmode=require"

# # engine = create_engine(DATABASE_URL)
# # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# # Base = declarative_base()

# # # SQLAlchemy model for sensor data
# # class Data(Base):
# #     __tablename__ = "data"
# #     id = Column(Integer, primary_key=True, index=True)
# #     current_date = Column(Date, nullable=False)
# #     current_time = Column(Time, nullable=False)
# #     x = Column(Float, nullable=False)
# #     y = Column(Float, nullable=False)
# #     z = Column(Float, nullable=False)

# # # Uncomment if you want to create tables automatically
# # # Base.metadata.create_all(bind=engine)

# # # Pydantic model for incoming data
# # class DataCreate(BaseModel):
# #     x: float
# #     y: float
# #     z: float

# # # Pydantic model for outgoing response
# # class DataResponse(BaseModel):
# #     id: int
# #     current_date: date
# #     current_time: time
# #     x: float
# #     y: float
# #     z: float

# #     class Config:
# #         orm_mode = True

# # app = FastAPI()

# # # Dependency for getting DB session
# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()

# # # POST endpoint to store sensor data
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

# # # GET endpoint to retrieve all stored sensor data as a list of JSON objects
# # @app.get("/data/", response_model=List[DataResponse])
# # def read_data(db: Session = Depends(get_db)):
# #     items = db.query(Data).all()
# #     return items

# # # A simple GET endpoint to test if the API is running
# # @app.get("/")
# # def read_root():
# #     return {"message": "Hello, World!"}


# # ===========================================
# # Flask server to receive data from ESP32s and store it in memory


# # from flask import Flask, request, jsonify
# # from flask_sqlalchemy import SQLAlchemy
# # from datetime import datetime

# # app = Flask(__name__)

# # # 1) Tell Flask‑SQLAlchemy where to store the file
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# # db = SQLAlchemy(app)

# # # 2) Define a model for your batches
# # class Batch(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     ts = db.Column(db.String, nullable=False)
# #     devices = db.Column(db.JSON, nullable=False)  # Requires SQLAlchemy 1.4+

# # # 3) Create the table (run once at startup)
# # with app.app_context():
# #     db.create_all()

# # @app.route('/receive_data', methods=['POST'])
# # def receive_data():
# #     payload = request.get_json()
# #     if not payload:
# #         return jsonify({"status":"error", "reason":"no JSON"}), 400

# #     payload['received_ts'] = datetime.utcnow().isoformat() + 'Z'
# #     batch = Batch(ts=payload['ts'], devices=payload['devices'])
# #     db.session.add(batch)
# #     db.session.commit()

# #     return jsonify({"status":"success", "received_ts": payload['received_ts']}), 200

# # @app.route('/all_batches', methods=['GET'])
# # def all_batches():
# #     rows = Batch.query.all()
# #     return jsonify([{"ts":r.ts, "devices":r.devices} for r in rows]), 200

# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=80)


# # ===========================================


# #!/usr/bin/env python3
# from flask import Flask, request, jsonify
# from datetime import datetime

# app = Flask(__name__)

# # In‐memory store of all batches received
# batches = []

# def utc_now_iso():
#     """Return current UTC time in ISO‑8601 with Z."""
#     return datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'

# @app.route('/receive_data', methods=['POST'])
# def receive_data():
#     data = request.get_json()
#     if not data:
#         return jsonify({"status": "error", "reason": "no JSON payload"}), 400

#     # Attach server receipt timestamp
#     data['received_ts'] = utc_now_iso()
#     # Store it
#     batches.append(data)

#     return jsonify({
#         "status": "success",
#         "received_ts": data['received_ts']
#     }), 200

# @app.route('/all_batches', methods=['GET'])
# def all_batches():
#     return jsonify(batches), 200

# if __name__ == '__main__':
#     # Install dependencies: pip3 install flask
#     # Run with: sudo python3 server.py   (or on port 5000 without sudo)
#     app.run(host='0.0.0.0', port=80)

#!/usr/bin/env python3
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In‐memory store of all batches received
batches = []

def utc_now_iso():
    """Return current UTC time in ISO-8601 with Z."""
    return datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'

@app.route('/test', methods=['GET'])
def test():
    """
    Simple health check endpoint to verify that the backend is running.
    """
    return jsonify({"status": "running"}), 200

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "reason": "no JSON payload"}), 400

    # Attach server receipt timestamp
    data['received_ts'] = utc_now_iso()
    # Store it
    batches.append(data)

    return jsonify({
        "status": "success",
        "received_ts": data['received_ts']
    }), 200

@app.route('/all_batches', methods=['GET'])
def all_batches():
    """
    Return all batches in the order they were received (oldest first).
    """
    return jsonify(batches), 200

@app.route('/batches_desc', methods=['GET'])
def batches_desc():
    """
    Return all batches with the latest addition first (descending order by received_ts).
    """
    # Sort by 'received_ts' in reverse chronological order
    sorted_batches = sorted(batches, key=lambda x: x['received_ts'], reverse=True)
    return jsonify(sorted_batches), 200

if __name__ == '__main__':
    # Install dependencies: pip3 install flask
    # Run with: sudo python3 server.py   (or on port 5000 without sudo)
    app.run(host='0.0.0.0', port=80)
