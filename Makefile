all:
	gunicorn3 app:app --daemon

kill:
	fuser -k 8000/tcp

clean:
	sudo -u postgres psql -d autopost -f pre_psql.sql
	rm -rf posts/*