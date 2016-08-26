FROM python:2.7-slim
ADD . /src
WORKDIR /src
RUN wget http://download.savannah.gnu.org/releases/freetype/freetype-2.5.3.tar.gz
RUN tar xzf freetype-2.5.3.tar.gz
RUN cd freetype-2.5.3
RUN ./configure --prefix=/myhome/local --without-png
RUN make && make install
RUN export PKG_CONFIG_PATH=/myhome/local/lib/pkgconfig
RUN cd ..
RUN pip install -r requirements.txt
CMD python ./bot/app.py
