FROM openalpr

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .
RUN pip3 install -r /app/requirements.txt

ENV FLASK_APP=/app/src/app.py
ENTRYPOINT [ "flask", "run" ]