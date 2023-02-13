FROM python:latest
MAINTAINER :"nguemechieu@ive.com"

WORKDIR /Blueyes

RUN echo "Welcome to Blueyes"
RUN echo "--------------------------------"
RUN echo "Now Installing Blueyes"

COPY pyproject.toml pyproject.toml
RUN echo "--------------------------------"
RUN  python -m build

CMD ["echo", "Main.py"]