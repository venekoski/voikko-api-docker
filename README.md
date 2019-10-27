# Voikko API Docker

This container runs a custom fork of Voikko as an API (flask-gunicorn-nginx) in a Docker container.

All endpoints take one argument, `?text=YOUR+QUERY+HERE`.

## Setup

First, make sure you have installed Docker. cd yourself here, build and run the docker with e.g.:
1. `docker build . -t <tag>`
2. `docker run -d -p 127.0.0.1:<port>:80 <tag>`

And voilà; you have an instance running at port `<port>`.

To test that the services are working, run e.g.

`curl -X GET 'http://localhost:<port>/lemmatize/?text=testaan+tätä'`

### (1) /analyze/

Get Voikko's basic linguistic analysis. Contains word class, inflection, etc. Both analysis and lemmatization services quality (vocabulary, inflection rules) depend on the built Voikko solution.

Returns Voikko's analysis object as json.

### (2) /lemmatize/

Get lemmatized text using Voikko.

### (3) /tokenize/

Get tokenized text using Voikko's tokenization.

The endpoint should be used if using Voikko's lemmatization and lemmatized data alongside non-lemmatized data. In other cases, there are probably better tokenization methods (e.g. nltk's various tokenizers).

### (4) /health/

Health check endpoint.