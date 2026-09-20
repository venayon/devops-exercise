```sh

docker build -t devops-exercise:1.1 .

```

```sh

docker run --rm -p 8080:5050 devops-exercise:1.1

```

```bash

curl http://localhost:8080/health

```