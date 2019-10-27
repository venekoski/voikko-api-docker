FROM tensorflow/tensorflow:latest-py3
# Using a base image which can be used for much more complciated things than just running Voikko

# Install Voikko packages 
RUN DEBIAN_FRONTEND=noninteractive \
	&& apt-get update \
	&& apt-get install -y voikko-fi python-libvoikko build-essential wget git unzip nginx supervisor locales \
  && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen "en_US.UTF-8" && localedef -f UTF-8 -i en_US en_US.UTF-8 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copy voikko transducers to appropriate locations
COPY ./app/mor.vfst /usr/lib/voikko/5/mor-standard/

# Copy requirements for running the API with Python and install them
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the app
COPY ./app /app

WORKDIR /app

# Copy libvoikko.py to app directory from install dir to make it available for the app.
RUN cp /usr/lib/python3/dist-packages/libvoikko.py /app/libvoikko.py

# Nginx configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
COPY ./conf/nginx.conf /etc/nginx/conf.d/nginx.conf

# Gunicorn and Supervisord configuration
COPY ./conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./conf/gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf
COPY ./conf/gunicorn.config.py /app/gunicorn.config.py

EXPOSE 80 443

# Run the app via supervisor
CMD ["/usr/bin/supervisord"]