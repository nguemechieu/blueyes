FROM python:latest as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PATH=/home/buser/.local/bin:$PATH
ENV FT_APP_ENV="docker"

# Prepare environment
RUN mkdir /blueyes \
  && apt-get update \
  && apt-get -y install sudo libatlas3-base curl sqlite3 libhdf5-serial-dev libgomp1 \
  && apt-get clean \
  && useradd -u 1000 -G sudo -U -m -s /bin/bash btuser \
  && apt-get install -y mysql  \
  && chown buser:buser /blueyes \
  # Allow sudoers
  && echo "btuser ALL=(ALL) NOPASSWD: /bin/chown" >> /etc/sudoers

WORKDIR /blueyes

# Install dependencies
FROM base as python-deps
RUN  apt-get update \
  && apt-get -y install build-essential libssl-dev git libffi-dev libgfortran5 pkg-config cmake gcc \
  && apt-get clean \
  && pip install --upgrade pip

# Install TA-lib
COPY build_helpers/* /tmp/
RUN cd /tmp && /tmp/install_ta-lib.sh && rm -r /tmp/*ta-lib*
ENV LD_LIBRARY_PATH /usr/local/lib

# Install dependencies
COPY --chown=buser:buser requirements.txt requirements-hyperopt.txt /blueyes/
USER ftuser
RUN  pip install --user --no-cache-dir numpy \
  && pip install --user --no-cache-dir -r requirements-hyperopt.txt

# Copy dependencies to runtime-image
FROM base as runtime-image
COPY --from=python-deps /usr/local/lib /usr/local/lib
ENV LD_LIBRARY_PATH /usr/local/lib

COPY --from=python-deps --chown=buser:buser /home/buser/.local /home/buser/.local

USER buser
# Install and execute
COPY --chown=buser:buser . /blueyes/

RUN pip install -e . --user --no-cache-dir --no-build-isolation \
  && mkdir /blueyes/user_data/ \
  && freqtrade install-ui

ENTRYPOINT ["main"]
# Default to trade mode
CMD [ "run" ]
