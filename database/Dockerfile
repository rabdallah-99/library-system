FROM mysql:8
ENV MYSQL_ROOT_PASSWORD=root  MYSQL_DATABASE=library
COPY library.sql test.sql  /docker-entrypoint-initdb.d/
