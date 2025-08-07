# bookspgs
Django Rest Framework with PGSQL
- The data will be loaded from csvs to PostgreSQL database inside the Docker conatiner.
- Django Rest Framework will connect to the PostgreSQL database.

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

Now open another terminal, go inside the same repo to run python commands inside the docker container - django_web
```bash
docker exec -it django_web bash
```
Run make migrations and migrate inside the docker container
```bash
python manage.py makemigrations
python manage.py migrate
exit
```
Now run this command to get pgsql shell
```bash
docker-compose exec db psql -U postgres
```
Connect to database
```bash
\c book
```
View the number of tables
```bash
\dt 
```
<img width="763" height="392" alt="image" src="https://github.com/user-attachments/assets/a2b27e00-f54b-4a2a-9704-e484735311a9" />

View table info for the particular table. Other tables can be checked similarly.
```bash
\d booktable
```
Once we see all tables are present, exit the pgsql shell using the command
```bash
\q
```
Now run the load_data.py file to populate the database. zit will load the 3 csvs into the database.
```bash
docker exec -it django_web python load_data.py
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
