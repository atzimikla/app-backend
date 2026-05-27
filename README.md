# app-backend

API Flask que expone si un entero es primo. PoC para validar Docker, Fury y GitOps/ArgoCD.

## Endpoints

| Método | Path | Descripción |
|---|---|---|
| `GET` | `/health` | liveness/readiness, devuelve `{"status":"ok"}` |
| `GET` | `/is-prime?n=<int>` | devuelve `{"n":<int>,"is_prime":<bool>}` |

## Correr local sin Docker

```
pip install -r requirements.txt
python app.py
curl 'http://localhost:8080/is-prime?n=17'
```

## Correr con Docker

```
docker build -t app-backend:dev .
docker run --rm -p 8080:8080 app-backend:dev
```

## En el contexto del PoC

Los manifests de Kubernetes y la definición ArgoCD viven en el repo `gitops-apps` (no acá). Para iterar local junto con el frontend usar el `docker-compose.yml` de la raíz del workspace.
