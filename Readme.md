1. 압축 해제 후 폴더 열기

2. (선택) 가상환경 생성 및 활성화  
   - python -m venv venv  
   - venv\\Scripts\\activate (Windows)

3. 터미널에서 패키지 설치  
   - pip install -r requirements.txt

4. MySQL Workbench 등에서 SQL 파일(create-table-template) 열고 실행  
   - CREATE DATABASE myproject; ← 사전에 만들어둬야 함  
   - 테이블 생성, 데이터 삽입 SQL 모두 Run
   - DB구축.ipynb 실행!

5. main.py 실행  
   - python main.py  
   - 실행 후 http://127.0.0.1:8000/docs 접속해 확인 가능

6. index.html 또는 heatwave_map_clustered.html 실행  
   - "Live Server"로 열기 (VSCode 추천)  
   - 주소 검색 없이도 쉼터 리스트와 마커 자동 표시
