# modbus-server

minimal docker container with python env and a TCP modbus server listening on port 502

## Build

```shell
docker build -t "modbus-server" .
```

## Run

```shell
docker run --rm -it -p 502:502 --name "modbus-server" modbus-server
```
