<h1 style="color: red">Rabbitmq</h1>
<hr>

### activate your environments
```bash
  python -m venv .
```

### enter in your venv environments
<img width="500" src="./assets/screenshots/use_venv.png">

example:<br>
windows: 
```bash
Scripts/activate.bat
```
Linux:
```bash
source bin/activate
```

### install all dependencies
```bash
pip install -r requirements.txt
```

### Define global URI in your pc
```bash
python -m Pyro4.naming
```

### run swapper
```bash
python ./Include/swapper/swapper.py
```

### run consumer
```bash
python ./Include/consumer/consumer.py rule=a
```
<div style="display: flex;">
   rule=&lt;character> <p style="color:red; padding-left: 20px">required parameter</p>
</div>

### run producer
```bash
python ./Include/producer/producer.py mpm=12 rule=a
```
<div style="display: flex;">
   mpm=&lt;integer> <p style="color:red; padding-left: 20px">required parameter</p>
</div>
<div style="display: flex;">
   rule=&lt;character> <p style="padding-left: 20px">optional parameter</p>
</div>


<br>
<p align="center">
   Feito com ❤️ by <b>weliton sousa</b>
</p>