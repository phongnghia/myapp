# MY RESUME
```text
Python (Django framework)
Docker
YAML
Shell scripting
``` 

### COMMAND TO PULL MY RESUME IMAGE FROM DOCKER HUB

---
```commandline
docker pull phongnghia/myresume:<tagname>
```
_or_
``` command
docker pull phongnghia.jfrog.io/default-docker-local/myresume:<tagname>
```

### COMMAND TO PUSH IMAGE TO REPOSITORY

---

_To docker hub_
```markdown
docker push phongnghia/<imagename>:<tagname>
```
_To Jfrog artifactory_
```commandline
jf docker tag <image>:<tag> phongnghia.jfrog.io/default-docker-virtual/<image>:<tag>
jf docker push phongnghia.jfrog.io/default-docker-virtual/<image>:<tag>
jf docker pull phongnghia.jfrog.io/default-docker-virtual/<image>:<tag>
```
### HOW TO RUN THE RESUME IMAGE

---

#### Pull resume image from docker hub or Jfrog artifactory
```commandline
docker pull phongnghia/myresume:<tagname>
```
_or_
``` command
docker pull phongnghia.jfrog.io/default-docker-local/myresume:<tagname>
```
#### Run container using the image pull above
```commandline
docker run -p <host_port>:<container_port> -it phongnghia/myresume:<tagname>
```
_example:_
```commandline
docker run -p 8000:8000 -it phongnghia/myresume:0.3
```

#### Run container using compose setup
```yaml
version: '3.9'
services:
  web:
    image: <docker_url>/<imagename>:<tagname> # phongnghia/myresume:0.2
    container_name: {image.name} # myresume
    tty: true
    ports:
      - "<port>:<port>" #8080:8080
```
_run command:_
```commandline
docker compose up
```
#### Run application using kubernetes YAML
```commandline
kubectl apply -f <pathfile>
```
_example:_
```commandline
kubectl apply -f myapp\myresume.yml
```