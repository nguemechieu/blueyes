FROM ubuntu:latest as build
WORKDIR /Blueyes
RUN echo "Welcome to Blueyes"
RUN echo "--------------------------------"
RUN echo "Now Installing Blueyes"
RUN apt-get   update
RUN apt-get install -y mysql
COPY pyproject.toml pyproject.toml
RUN echo "--------------------------------"
FROM python:latest 
RUN cd /Bueyes
CMD ["python", "Main.py"]