FROM python:3.6-alpine

ENV FLASK_APP run.py
ENV FLASK_CONFIG production

WORKDIR /greenbox-server

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY run.py config.py boot.sh ./
ENTRYPOINT ["python"]
CMD ["run.py"]
