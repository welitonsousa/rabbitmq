FROM python:3


COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ARG I
ENV INITIAL_PORT $I
CMD python -m client ${INITIAL_PORT};
