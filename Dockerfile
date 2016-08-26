FROM tailordev/pandas
ADD . /src
WORKDIR /src
RUN pip install -r requirements.txt
CMD python ./bot/app.py
