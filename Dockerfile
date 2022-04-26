FROM python:alpine

WORKDIR /app


# Install dependencies
COPY requirements.txt ./
RUN apk add --no-cache --update alpine-sdk &&\
    pip install --no-cache-dir gunicorn &&\
    pip install --no-cache-dir -r requirements.txt

# Expose App directory
# COPY . .
VOLUME /app

# Expose App port
EXPOSE 5000

#CMD [ "python", "./run.py" ]
CMD ["/bin/sh", "./run.sh"]
