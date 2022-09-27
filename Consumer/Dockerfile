FROM python:3


COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ARG P
ENV CLIENT_QUANTITY_PORTS $P
CMD python -m client ${CLIENT_QUANTITY_PORTS};