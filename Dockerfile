FROM python:3.9-slim

WORKDIR /app

COPY cloudassigment.ipynb .
COPY paragraphs.txt .

RUN pip install nltk
RUN python -m nltk.downloader punkt stopwords

CMD ["python", "cloudassigment.ipynb"]
