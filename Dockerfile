FROM python:alpine

WORKDIR /app

# Install APK dependencies
# RUN apk update &&  apk add xxx

# Install PIP dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose App directory
# COPY . .
VOLUME /app

# Expose App port
EXPOSE 5000

CMD [ "python", "./run.py" ]