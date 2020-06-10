# px-locust

## Run px-locust
```
docker run -e FRONTEND_ADDR='<addres to front end>' --rm --name test -p 5000:5000 javier1/px-locust:0.0.2
```
For example
```
docker run -e FRONTEND_ADDR='http://35.225.95.162' --rm --name test -p 5000:5000 javier1/px-locust:0.0.2
```

## Get locust status
```
curl localhost:5000/invokust/get
```

## Start locust
```
curl -X POST -d "{\"users\": \"1\", \"hrate\": \"1\"}"  -H 'Content-Type: application/json' localhost:5000/invokust
```

## Stop locust
```
curl localhost:5000/invokust/stop
```
