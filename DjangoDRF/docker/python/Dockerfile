FROM python:3.6
MAINTAINER p.valeraka@gmail.com
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt

#COPY ./docker/python/entrypoint.sh  /entrypoint.sh
#RUN chmod +x /entrypoint.sh
#ENTRYPOINT "/entrypoint.sh"
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8888"]
