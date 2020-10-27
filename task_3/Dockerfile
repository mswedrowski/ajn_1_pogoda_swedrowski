FROM ubuntu:xenial

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install libboost-all-dev libicu-dev git-core wget cmake libantlr-dev libloki-dev python-dev swig libxml2-dev libsigc++-2.0-dev libglibmm-2.4-dev libxml++2.6-dev

RUN mkdir /build
WORKDIR /build
RUN git clone http://nlp.pwr.wroc.pl/corpus2.git
RUN git clone http://nlp.pwr.edu.pl/wccl.git
RUN wget -O morfeusz2-2.0.0-Linux-amd64.deb https://nextcloud.clarin-pl.eu/index.php/s/VVIvx4w20azcWbp/download
RUN dpkg -i morfeusz2-2.0.0-Linux-amd64.deb

RUN cd corpus2
RUN mkdir bin
WORKDIR /build/corpus2/bin
RUN cmake ..
RUN make -j
RUN make -j
RUN make install
RUN ldconfig
