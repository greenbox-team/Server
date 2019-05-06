FROM python:3.6-alpine

ENV FLASK_APP run.py
ENV FLASK_CONFIG production

RUN mkdir /greenbox-server

WORKDIR /greenbox-server

ADD . .

RUN pip install -r ./requirements.txt

EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["run.py"]
