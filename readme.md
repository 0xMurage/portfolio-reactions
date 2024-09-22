## PORTFOLIO PROJECTS REACTIONS

---

### 1. Development setup using Docker
#### Prerequisites
- Git v2+
- Docker cli v27+
- Docker compose v2.29+
#### Steps
- Fork/Clone the repo
```shell
git clone git@github.com:0xmurage/portfolio-reactions.git
````
- Navigate to the project directory 
```shell
cd portfolio-reactions
```
- Copy and update the app config 
```shell
cp .env-example .env
```

- Run the docker compose 
```shell
docker compose up
```
Above will run both compose.yaml and compose.override.yaml.

- The API endpoints are now ready and accessible at `http://localhost:8000/`

### 2. Manual Project Setup

#### Prerequisites
- Git
- Python 3.8+
- MySQL or MariaDB
#### Steps
- Fork/Clone the repo
```shell
git clone git@github.com:0xmurage/portfolio-reactions.git
````
- Navigate to the project directory
```shell
cd portfolio-reactions
```
- Copy and update the app config
```shell
cp .env-example .env
```
- Create virtual env if not exists

```shell
python3 -m venv ./venv
```
- Activate the virtualenv
```shell
source ./venv/bin/activate
```

- Install the project requirements

```shell
pip install -r requirements.txt
```

- Run the Flask app 
```shell 
flask run
```

- The endpoints are now ready and accessible at `http://localhost:8000/`

### RESTful Endpoints

**GET** `/api/v1/reactions/{device_id}`
Return all reactions and if I have reacted

```json
{
  "reactions": [
    {
      "project_id": "xxx",
      "reactions": 100000,
      "reacted": false
    }
  ]
}
```

**POST** `/api/v1/reactions/{project_id}`
increment reactions and return current reactions

Request body

```json
{
  "device_id": 100000
}
```

Response

```json
{
  "reactions": [
    {
      "project_id": "xxx",
      "reactions": 100000,
      "reacted": true
    }
  ]
}
```

**DELETE** `/api/v1/reactions/{project_id}`
decrement reactions and return current reactions

Request body

```json
{
  "device_id": 100000
}
```

Response

```json
{
  "reactions": [
    {
      "project_id": "xxx",
      "reactions": 100000,
      "reacted": false
    }
  ]
}
```
