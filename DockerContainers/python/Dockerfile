## Image + workdir set 
FROM python:3
WORKDIR /app

# Copying files from container
COPY . /app
# Runing apt commands
RUN apt-get update && \
    apt-get install -y nano
# Runing python packages commands
RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt
# Running terminal commands
RUN alias ls='ls --color -a'

CMD [ "python", "main.py"]