from alpine:latest
RUN apk add --no-cache python3-dev
RUN apk add --no-cache py-pip

WORKDIR /app
COPY . /app

RUN pip
RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000
