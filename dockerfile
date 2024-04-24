FROM python:3

RUN pip3 --no-cache-dir install requests
RUN pip3 --no-cache-dir install gitpython

WORKDIR /app/
COPY /app/*.py /app/
COPY /data/* /app/data/
CMD ["python", "/app/main.py"]
