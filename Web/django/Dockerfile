FROM python:3.8

# 컨테이너 내부 기준 디렉토리 생성
WORKDIR /app 

# django/requirements.txt를 컨테이너 app/requirements.txt로 복사
COPY /django/requirements.txt requirements.txt

# 기반 세팅
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# django 내부 모든 파일을 app/ 이하로 복사
COPY . .