# bookspgs
Django Rest Framework with PGSQL

## Folder structure


## Installation

```bash
  cd ph_drf
  python venv myvenv
  myvenv\Scripts\activate
```

Run the docker-compose file inside the terminal.
```bash
docker-compose up --build
```

Now open another terminal and go inside the same repo
```bash
docker exec -it django_web bash
```
Run make migrations and migrate inside the docker container
```bash
python manage.py makemigrations
python manage.py migrate
```

```bash
  python manage.py runserver
```
The server runs on http://localhost:8000

## API Reference

#### Get all items

```http
  GET /books/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None |  | Fetches JSON containing all articles from MongoDB |
<img width="1212" height="696" alt="image" src="https://github.com/user-attachments/assets/ea5013cd-e418-46df-a450-87ad9a834c5e" />
