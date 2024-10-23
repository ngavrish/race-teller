

### race-teller
arkadiy kirsanov inspired tool to analyse racing data 

### installation
```brew update
brew install telegraf
brew install git
brew install go
brew install node@20
brew install corepack
brew install influxdb
brew install influxdb-cli
brew install ffmpeg
corepack enable
brew install postgres

-- insrall go2rtc
cd go2rtc
go build


```
### influx db setup
To start influxdb@1 now and restart at login:
  ```brew services start influxdb@1```
Or, if you don't want/need a background service you can just run:
  ```/opt/homebrew/opt/influxdb@1/bin/influxd -config /opt/homebrew/etc/influxdb.conf```

Create datasource
> CREATE DATABASE twentyniner 
> 
> SHOW DATABASES


### env
PATH=/opt/homebrew/opt/influxdb@1/bin/:${PATH}
INFLUX_TOKEN=gVHBPAhBd4qgWJuN3bHhJ5YpEiUdaBRKzE0Y1YqG_DVQ5nnXCxkGMtdb3Um_ONHPPTCTA_pcQ5eO3S4PERIKzw==
export INFLUX_TOKEN

open http://localhost:8086
root token AtkVxYRj4UrZ7m67MTpYvLf0N5UsWCK987OkMtKlr41fjYoYFex6RnWXtvnW2jL4vrfNTzctgRR-2Xq-iIIcmw==
all access token gVHBPAhBd4qgWJuN3bHhJ5YpEiUdaBRKzE0Y1YqG_DVQ5nnXCxkGMtdb3Um_ONHPPTCTA_pcQ5eO3S4PERIKzw==

### influx authorization

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

### Python env

python -m venv envs/virtual-env && . ./envs/virtual-env/bin/activate
pip install influxdb3-python pandas tabulate pip3 install influxdb-client


## Install local grafana
```
make lefthook-install
yarn install --immutable # to build the frontend assets, you need to install the related dependencies:
yarn start # start building the source code
make run # in the grafana folder
yarn test
go test -v ./pkg/...
```

By default, you can access the web server at http://localhost:3000/.

Log in using the default credentials:

username	password
admin	admin

### Configuration
The default configuration, defaults.ini, is located in the conf directory.

To override the default configuration, create a custom.ini file in the conf directory. You only need to add the options you wish to override.

Enable the development mode by adding the following line in your custom.ini:
```
app_mode = development
```


### PostgreSQL

```
brew services start postgresql@17
rm /opt/homebrew/var/postgres@17/postmaster.pid

```


https://docs.influxdata.com/telegraf/v1/get-started/
https://www.influxdata.com/time-series-platform/
https://docs.influxdata.com/influxdb/v1/


### how to switch between projects in github
assuming you have several projects with different id_rsa keys. you need to work with your ssh agent to switch between using those
```
ssh-add -D # clean id_rsa
ssh-add ~/.ssh/<id_rsa_filename> # add new id_rsa 
```

[//]: # (geomap know how)
[//]: # (https://community.grafana.com/t/grafana-geomap-route/106009/6)

[//]: # (https://community.grafana.com/t/synchronizing-cursor-movement-in-grafanas-time-series-panel-with-custom-panel-events/116891)
[//]: # (https://grafana.com/developers/plugin-tools/tutorials/build-a-panel-plugin)