FROM python:3


COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ARG P
ARG I
ENV PRODUCER_QUANTITY_PORTS $P
ENV INITIAL_PORT $I
CMD python -m server ${PRODUCER_QUANTITY_PORTS} ${INITIAL_PORT};
