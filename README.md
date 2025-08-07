# [λ] AWS Lambda Demo amb Docker

Aquest projecte és una **demo mínima** d'una funció AWS Lambda escrita en **Python**, executada en **local** dins un contenidor Docker, utilitzant la imatge oficial `amazon/aws-lambda-python`.

---

## Què són les funcions Lambda?

Les **funcions Lambda** d'AWS són xicotetes peces de codi que s'executen **sense necessitat de servidors propis**. Només s'executen quan són invocades per algun "esdeveniment" (ex: petició HTTP, pujada a S3, missatge en una cua, etc.).

### Característiques:
- Sense servidors: no cal gestionar màquines ni desplegaments manuals.
- Escalabilitat automàtica: Lambda escala segons la demanda.
- Pagament per ús: només pagues pel temps d'execució real.
- Integració nativa amb serveis AWS (S3, API Gateway, DynamoDB, etc.)

---

## Contingut del projecte

```
lambda-demo/
├── lambda_function.py     # Codi de la funció Lambda
├── Dockerfile             # Imatge Docker basada en amazon/aws-lambda-python
└── event.json             # Exemple d'esdeveniment per provar la funció
```

---

## Utilitat de fer proves en local

Fer proves locals amb Docker et permet:
- Validar el comportament de la funció **sense accedir a AWS**
- Fer debugging més ràpid i econòmic
- Simular invocacions reals com les que faria API Gateway o altres serveis

---

## Instruccions d'ús

### 1. Construir la imatge

```bash
git clone https://github.com/iesbillenguatges/lambda-demo.git
cd lambda-demo
docker build -t lambda-python-demo .
```
### Dockerfile

``
FROM public.ecr.aws/lambda/python:3.12

COPY lambda_function.py ${LAMBDA_TASK_ROOT}

CMD ["lambda_function.handler"]
```

### Explicat línia per línia

- FROM public.ecr.aws/lambda/python:3.12 Indica quina imatge base s’ha d’utilitzar per crear el contenidor Docker. Utilitza una imatge oficial de Lambda amb Python 3.12. Aquesta imatge simula l'entorn real d'AWS Lambda (paths, permisos, API, etc.)
- COPY lambda_function.py ${LAMBDA_TASK_ROOT} Copia el fitxer lambda_function.py (del teu projecte local) dins del contenidor. El fitxer es copia al directori especial ${LAMBDA_TASK_ROOT}. Aquest és un path predefinit dins la imatge Lambda on ha d’estar el codi per a que Lambda el trobe. És com dir: *Posa aquest fitxer allà on Lambda espera trobar el codi.*
- CMD ["lambda_function.handler"] Indica quin és el punt d’entrada de la funció Lambda quan s’invoca. ["nom_del_fitxer.nom_de_la_funció"] en aquest cas: *lambda_function* = nom del fitxer (sense .py) *handler* = nom de la funció dins el fitxer

### 2. Executar el contenidor

```bash
docker run -p 9000:8080 lambda-python-demo
```

Això alça un servidor local que simula AWS Lambda.

---

## Invocar la funció Lambda

Assegura't que el fitxer event.json existeix al directori actual i executa:

```bash
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d @event.json
```

Això envia el contingut de `event.json` com a esdeveniment a la Lambda.

## Resposta esperada

```json
{
  "statusCode": 200,
  "body": "Hola, Classe iesbi_np 25/26!"
}
```

---

## Recursos útils

- [Documentació oficial Lambda + Docker](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html)
- [Imatge oficial a Docker Hub](https://hub.docker.com/r/amazon/aws-lambda-python)

---

## Propòsit

Creat per aprendre el funcionament de Lambda amb Docker. Ideal per entorns de desenvolupament locals, prototips i proves de concepte.
