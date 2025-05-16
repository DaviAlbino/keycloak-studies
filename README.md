# keycloak-studies
Para estudar keycloak


## Para usar keycloak com docker:

```console
(base)lumen@dev:~$ docker run -p 8070:8080 -e KC_BOOTSTRAP_ADMIN_USERNAME=admin -e KC_BOOTSTRAP_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:26.2.3 start-dev
```
# Set Enviroment

```console
(base)lumen@dev:~$ conda create --name keycloak-uma python=3.11
(base)lumen@dev:~$ conda activate keycloak-uma
(keycloak-uma)lumen@dev:~$ pip install -r requirements.txt
```


## Execução do código

```console
(tracker-ai)lumen@dev:~$ uvicorn main:app --port 8111 --reload
```
