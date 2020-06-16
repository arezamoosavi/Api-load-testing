#!/bin/bash
#!/bin/sh

set -o errexit
set -o nounset



n=8

while [ $n -gt 0 ]
do
	echo "Wait for kafka and redis $n more times."
	n=$(( n-1 ))
    sleep 2
done

pytest tests/test_health_check.py -s

echo ". . . . . Health Check Is Done! . . . . ."
sleep 5

while python check_faust.py; do echo 'faust is running...'; sleep 2; done;

echo ". . . . . Faust Is Done! . . . . ."


faust -A app.tools.faust_:faust_app worker -l info -p 6066

exec "$@"