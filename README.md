# gns3
gns3 서버 설정 파일들

종류
버전
웹 서버
nginx 1.15.8 
웹앱(WAS)
Django(Python 3.8.20 / Gunicorn)
DB
mysql 9.2.0

1. [디렉터리 구조]
.
├── anaconda-ks.cfg
├── django
│   ├── admin
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   ├── settings.cpython-38.pyc
│   │   │   ├── urls.cpython-38.pyc
│   │   │   └── wsgi.cpython-38.pyc
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── Dockerfile
│   ├── manage.py
│   ├── requirements.txt
│   └── wait-for-it.sh
├── docker-compose.yml
├── mysql
│   ├── data.sql
│   └── Dockerfile
├── nginx
    ├── Dockerfile
    ├── nginx.conf
    └── project.conf


2. 필요한 Dockerfile, docker-compose.yml 설정 
3. 실행
docker compose build 
docker compose up 
 