web: daphne oxowlbot.asgi:application --port $PORT --bind 0.0.0.0 -v2
release: ./python -c 'import stanza; stanza.download("en")'
release: ./python manage.py migrate
