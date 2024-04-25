FROM python:3.12

WORKDIR /app

COPY main.py  /app
COPY paragraphs.txt /app
RUN pip install nltk
RUN python -m nltk.downloader punkt stopwords

CMD ["python", "main.py"]
