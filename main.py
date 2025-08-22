from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from models import Base, WeatherForecast, HeatShelter
import subprocess
import sys
import importlib.util
import os

# ✅ FastAPI 객체는 한 번만 생성!!
app = FastAPI()

# ✅ CORS 허용 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 또는 ["http://localhost:5500"] 등으로 제한 가능
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 테이블 자동 생성
Base.metadata.create_all(bind=engine)

# ✅ DB 세션 DI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ API: 최신 기온
@app.get("/weather/latest")
def get_latest_weather(db: Session = Depends(get_db)):
    return db.query(WeatherForecast).filter(WeatherForecast.category == "TMP")\
             .order_by(WeatherForecast.fcst_date.desc(), WeatherForecast.fcst_time.desc()).first()

# ✅ API: 쉼터 목록
@app.get("/shelters")
def get_shelters(db: Session = Depends(get_db)):
    return db.query(HeatShelter).all()

# ✅ API: 폭염 알림
@app.get("/alert")
def heatwave_alert(db: Session = Depends(get_db)):
    latest = db.query(WeatherForecast).filter(WeatherForecast.category == "TMP")\
        .order_by(WeatherForecast.fcst_date.desc(), WeatherForecast.fcst_time.desc()).first()

    if not latest:
        raise HTTPException(status_code=404, detail="기온 데이터 없음")

    if float(latest.value) >= 33.0:
        return {"alert": True, "message": "🔥 폭염주의보! 무더위쉼터를 확인하세요!"}
    else:
        return {"alert": False, "message": "☀️ 현재 기온은 정상입니다."}

# ✅ 필요한 패키지 자동 설치
def install(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

packages = ["fastapi", "uvicorn", "sqlalchemy", "pymysql"]
for pkg in packages:
    if importlib.util.find_spec(pkg) is None:
        print(f"📦 '{pkg}' 설치 중...")
        install(pkg)
    else:
        print(f"✅ '{pkg}' 이미 설치됨!")

# ✅ FastAPI 서버 실행
print("🚀 FastAPI 서버 실행 중...")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
