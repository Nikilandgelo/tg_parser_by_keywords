FROM python:3.13-alpine
WORKDIR /app

RUN pip install pip-tools
COPY requirements.in .
RUN pip-compile && pip-sync

COPY . .
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["sh", "-c", "./entrypoint.sh \"$@\"", "--"]