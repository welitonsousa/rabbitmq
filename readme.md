<h1 style="color: red">Rabbitmq</h1>
<!-- python3 -m Pyro4.naming -->

### Producer
##### build the image
```bash
docker build -t producer --build-arg Q=QUANTITY_PORTS I=INITIAL_PORT .
```
##### run the image
```bash
docker run producer
```

<hr>

### Consumer
##### build the image
```bash
docker build -t consumer --build-arg Q=QUANTITY_PORTS I=INITIAL_PORT .
```

<br>
<p align="center">
   Feito com ❤️ by <b>weliton sousa</b>
</p>
