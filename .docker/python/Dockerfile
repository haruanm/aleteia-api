FROM python:3.7

WORKDIR /usr/src/app

COPY . .

RUN apt update && apt install python3-mysqldb

RUN mkdir -p /usr/src/app/static
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir uwsgi

RUN python manage.py warmup
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python3 manage.py shell
RUN chmod +x /usr/src/app/.docker/python/entrypoint.sh

CMD ["/usr/src/app/.docker/python/entrypoint.sh"]
