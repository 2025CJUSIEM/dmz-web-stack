FROM mysql:latest

# root 패스워드 지정
ENV MYSQL_ROOT_PASSWORD=pass

COPY ./data.sql /docker-entrypoint-initdb.d/data.sql

