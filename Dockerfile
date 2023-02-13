FROM ubuntu:latest

MAINTAINER :"nguemechieu@ive.com"

WORKDIR /Blueyes

RUN echo "Welcome to Blueyes"
RUN echo "--------------------------------"
RUN echo "Now Installing Blueyes"

COPY Main.py Main.py

CMD ["echo", "Main.py"]