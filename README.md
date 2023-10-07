# MY RESUME
```text
Python (Django framework)
Docker
YAML
Shell scripting
``` 

### 1. COMMAND TO PULL MY RESUME IMAGE FROM DOCKER HUB
```commandline
docker pull phongnghia/myresume:<tagname>
```
###### or
``` command
docker pull phongnghia.jfrog.io/default-docker-local/myresume:<tagname>
```

### 2. COMMAND TO PUSH IMAGE TO REPOSITORY

##### To docker hub
```markdown
docker push phongnghia/<imagename>:<tagname>
```
##### To Jfrog artifactory
```commandline
jf docker tag <image>:<tag> phongnghia.jfrog.io/default-docker-virtual/<image>:<tag>
jf docker push phongnghia.jfrog.io/default-docker-virtual/<image>:<tag>
jf docker pull phongnghia.jfrog.io/default-docker-virtual/<image>:<tag>
```
### 3. HOW TO RUN THE RESUME IMAGE

##### 3.1 Pull resume image from docker hub or Jfrog artifactory
```commandline
docker pull phongnghia/myresume:<tagname>
```
###### or
``` command
docker pull phongnghia.jfrog.io/default-docker-local/myresume:<tagname>
```
##### 3.2 Run container using the image pull above
```commandline
docker run -p <host_port>:<container_port> -it phongnghia/myresume:<tagname>
```
###### example:
```commandline
docker run -p 8000:8000 -it phongnghia/myresume:0.3
```

##### 3.3 Run container using compose setup
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
###### run command
```commandline
docker compose up
```
##### 3.4 Run application using kubernetes YAML
```commandline
kubectl apply -f <pathfile>
```
###### example
```commandline
kubectl apply -f myapp\myresume.yml
```