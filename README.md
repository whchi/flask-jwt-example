# flask-jwt-example

## run
1. enable mongo
```sh
docker-compose up -d
```
2. start flask
```sh
FLASK_ENV=development flask run
```
## create user
```sh
flask create create <account>
```

## get jwt token
[POST] /get-token
```json
{
	"account": "<account>",
	"password": "<generated password>"
}
```
