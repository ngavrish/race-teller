# race-teller
arkadiy kirsanov inspired tool to analyse racing data 

# installation
brew update
brew install telegraf
brew install git
brew install go
brew install node@20
brew install corepack
brew install influxdb
brew install influxdb-cli
corepack enable

git clone https://github.com/grafana/grafana.git

# influx db setup
open http://localhost:8086
root token AtkVxYRj4UrZ7m67MTpYvLf0N5UsWCK987OkMtKlr41fjYoYFex6RnWXtvnW2jL4vrfNTzctgRR-2Xq-iIIcmw==
all access token gVHBPAhBd4qgWJuN3bHhJ5YpEiUdaBRKzE0Y1YqG_DVQ5nnXCxkGMtdb3Um_ONHPPTCTA_pcQ5eO3S4PERIKzw==

# authorization

```angular2html
influx config create  --config-name race-teller-config --host-url http://localhost:8086  --org race-teller --token gVHBPAhBd4qgWJuN3bHhJ5YpEiUdaBRKzE0Y1YqG_DVQ5nnXCxkGMtdb3Um_ONHPPTCTA_pcQ5eO3S4PERIKzw== --active
```


from cli
```influx setup```
or
```angular2html
influx setup \
  --username USERNAME \
  --password PASSWORD \
  --token TOKEN \
  --org ORG_NAME \
  --bucket BUCKET_NAME \
  --force
```

run telegraph

```angular2html
telegraf -config ./telegraf.conf #create config
telegraf -config /opt/homebrew/etc/telegraf.conf
```

# Python env

python -m venv envs/virtual-env && . ./envs/virtual-env/bin/activate
pip install influxdb3-python pandas tabulate pip3 install influxdb-client
