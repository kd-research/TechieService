# Use an official Ubuntu base image
FROM ubuntu:22.04 AS base

# Set environment variables
ENV RUBY_VERSION=3.3.3
ENV PYTHON_VERSION=3.12.4

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libssl-dev \
    libreadline-dev \
    zlib1g-dev \
    libbz2-dev \
    libsqlite3-dev \
    wget \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libffi-dev \
    liblzma-dev \
    uuid-dev \
    libdb-dev \
    libgmp-dev \
    libxml2-dev \
    libxslt-dev \
    libffi-dev \
    libyaml-dev

# Install Ruby
RUN wget http://cache.ruby-lang.org/pub/ruby/3.3/ruby-$RUBY_VERSION.tar.gz \
    && tar -xzvf ruby-$RUBY_VERSION.tar.gz \
    && cd ruby-$RUBY_VERSION \
    && ./configure \
    && make -j$(nproc)\
    && make install \
    && cd .. \
    && rm -rf ruby-$RUBY_VERSION ruby-$RUBY_VERSION.tar.gz

# Install Python
RUN wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz \
    && tar -xzf Python-$PYTHON_VERSION.tgz \
    && cd Python-$PYTHON_VERSION \
    && ./configure --enable-optimizations \
                   --enable-shared \
                   LDFLAGS="-Wl,-rpath /usr/local/lib" \
    && make -j$(nproc) \
    && make altinstall \
    && cd .. \
    && rm -rf Python-$PYTHON_VERSION Python-$PYTHON_VERSION.tgz

ENV RUBY=/usr/local/bin/ruby
ENV PYTHON=/usr/local/bin/python3.12

# Verify installations
RUN ruby -v && python3.12 --version

# Set up a working directory
WORKDIR /app

FROM base AS python_server

COPY requirements.lock /app

RUN $PYTHON -m pip install --upgrade pip \
    && $PYTHON -m pip install -r requirements.lock

# Perform a daily refresh on the latest techies pip package
RUN echo $(date) >/dev/null \
    && $PYTHON -m pip install techies@git+https://github.com/kd-research/Techies@main

COPY . /app

EXPOSE 9452
ENTRYPOINT ["bash", "-l", "-c"]
CMD ["./serve.sh"]
