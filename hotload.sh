#!/bin/bash

ppid=$$

function watch_file {
    inotifywait -qm -r */ -e close_write --exclude ".*.pyc|.coverage|.pytest_cache|.mypy_cache" | while read -r path event filename;
    do
        echo -e "\033[1;7;37m$path$filename was $event\033[0;1;0m"
        kill -s SIGUSR1 $ppid
    done
}
watch_file & notify_pid="$!"

trap "{ kill --verbose -s SIGKILL -- $notify_pid $ppid; exit 255; }" SIGINT SIGTERM
trap "{ ./execute.sh; }" SIGUSR1

while :;
do
    echo -n "."
    sleep 1
done
