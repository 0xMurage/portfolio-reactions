## PORTFOLIO PROJECTS REACTIONS

---

### 1. Docker Project Setup
#### Prerequisites
- Git
- Docker cli
- MySQL or MariaDB
#### Steps
- Clone the repo `git clone https://github.com/mimidotsuser/portfolio-reactions.git``
- Change directory ``cd portfolio-reactions`
- Copy and rename `.env-example` to `.env`.
- Setup MySQL/MariaDB database
- Update the `.env` config values especially the database config
- Build the image `docker build -t demo/reactions .`
- Run the image `docker run -p 8000:8000 --env-file .env --name abc demo/reactions`
  or `docker run -p 8000:8000 --env-file .env --name abc --network=host demo/reactions` to share the host network namespace
- Run `docker exec -it abc  alembic upgrade head` to execute migrations
- The endpoints are now ready and accessible at `http://localhost:8000/`

### 2. Manual Project Setup

#### Prerequisites
- Git
- Python 3.8+
- MySQL or MariaDB
#### Steps
- Clone the repo `git clone https://github.com/mimidotsuser/portfolio-reactions.git`
- Change directory `cd portfolio-reactions`
- Copy and rename `.env-example` to `.env`.
- Setup MySQL/MariaDB database
- Update the `.env` config values especially the database config
- Install project requirements with PIP `pip install -r requirements.txt`
- Run the Flask app `flask run`
- The endpoints are now ready and accessible at `http://localhost:8000/`

### RESTful Endpoints

**GET** `/api/reactions/{device_id}`
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

**POST** `/api/reactions/{project_id}`
increment reactions and return current reactions

Request

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

**DELETE** `/api/reactions/{device_id}`
decrement reactions and return current reactions

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
