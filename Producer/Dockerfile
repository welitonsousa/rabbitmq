FROM python:3


COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ARG P
ENV PRODUCER_QUANTITY_PORTS $P
CMD python -m server ${PRODUCER_QUANTITY_PORTS};
