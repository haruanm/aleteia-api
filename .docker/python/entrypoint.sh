#!/bin/sh
if [ -z ${DONT_WAIT_FOR_DB+1} ]; then
	until nc -z -v -w30 $DB_HOSTNAME $DB_PORT
	do
		echo "Waiting for database connection..."
		# wait for 5 seconds before check again
		sleep 2
	done
fi

[ -f __deploy_info.txt ] && mv __deploy_info.txt ./static
[ -d /usr/src/app/static-shared ] && cp -r ./static/* /usr/src/app/static-shared

python manage.py migrate

uwsgi --socket 0.0.0.0:8000 --buffer-size 8192 --protocol uwsgi --module aleteia.wsgi:application
