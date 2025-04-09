FROM nginx:1.15.8

# 기존 conf 삭제하고, 사용자가 설정한 conf로 변경
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY project.conf /etc/nginx/conf.d/
