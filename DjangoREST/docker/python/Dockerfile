FROM python:3.6
MAINTAINER p.valeraka@gmail.com
COPY ./src /src
WORKDIR /src
RUN pip install -r requirements.txt
COPY ./docker/python/entrypoint.sh  /entrypoint.sh
ENTRYPOINT "/entrypoint.sh"
RUN chmod +x /entrypoint.sh
#CMD ["python3", "app/manage.py", "runserver", "0.0.0.0:8080"]
