FROM python:2.7-slim
ADD . /src
WORKDIR /src
RUN sudo apt-get install pkg-config
RUN pip install -r requirements.txt
CMD python ./bot/app.py
