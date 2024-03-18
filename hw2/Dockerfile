FROM python:3.11

RUN apt-get update -y --fix-missing
RUN apt-get install -y texlive

WORKDIR /hw2

COPY . /hw2
RUN pip install -r requirements.txt

CMD ["python", "src/main21.py"]