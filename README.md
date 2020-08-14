fastapi-sklearn-demo



###### Deployment with Docker

1.Build the Docker image

```
docker build -t fastapi:v0.1 .
```

2.Running the Docker image

```
docker run -p 8000:8000 fastapi:v0.1
```

3.Entering into the Docker image

```
docker run -it --entrypoint /bin/bash fastapi:v0.1
```

