from alpine:latest
RUN apk add --no-cache python3-dev
RUN apk add --no-cache py-pip

WORKDIR /app
COPY . /app

RUN pip
RUN pip --no-cache-dir install -r requirements.txt
RUN pip install flake8
RUN flake8
RUN python3 test.py

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["mainpage.py"]
