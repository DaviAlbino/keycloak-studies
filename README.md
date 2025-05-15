# keycloak-studies
Para estudar keycloak


## Para usar keycloak com docker:

```console
(base)lumen@dev:~$ docker run -p 8070:8080 -e KC_BOOTSTRAP_ADMIN_USERNAME=admin -e KC_BOOTSTRAP_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:26.2.3 start-dev
```
