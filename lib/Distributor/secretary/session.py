from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from pathlib import Path

# 📌 현재 session.py와 같은 폴더의 .env를 정확히 지정
env_path = Path(__file__).resolve().parent / ".env"
# print("🧭 Looking for .env at:", env_path)

# ✅ 명시적으로 로딩
loaded = load_dotenv(dotenv_path=env_path)
# print("📦 dotenv loaded:", loaded)

# ✅ 환경변수 읽기
db_url = os.getenv("DB_URL")
# print("📌 Loaded DB_URL:", db_url)

engine = create_engine(db_url, echo=False, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)