#!/bin/bash
#!/bin/sh


set -o errexit
set -o nounset



n=10

while [ $n -gt 0 ]
do
	echo "Wait for postgres $n more times."
	n=$(( n-1 ))
    sleep 5
done


while python check_create_db.py; do echo 'connecting to database...'; sleep 2; done;

echo ". . . . . Database Connection Is Done! . . . . ."


echo ". . . . . Web Boot Up In Progress! . . . . ."

uvicorn bootUp:app --host ${HOST} --port ${PORT} --reload --ws 'auto' --loop 'auto' --workers 8

# python bootUp.py

exec "$@"