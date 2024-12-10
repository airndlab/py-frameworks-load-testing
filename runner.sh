#!/bin/bash

K6_DURATION="1m"

declare -A TYPE_FILENAME_MAP=(
  ["fastapi"]="myfastapi.py"
  ["blacksheep"]="myblacksheep.py"
  ["muffin"]="mymuffin.py"
  ["sanic"]="mysanic.py"
)


for TYPE in "${!TYPE_FILENAME_MAP[@]}"
do
  FILENAME=${TYPE_FILENAME_MAP[$TYPE]}

  python apps/$FILENAME &
  APP_PID=$!

  mkdir -p reports/$TYPE

  sleep 3
#1 10 30 60 90 120
  for K6_VUS in 150 300 600 1000
  do
    K6_DURATION=$K6_DURATION K6_VUS=$K6_VUS TYPE=$TYPE k6 run script.js
  done

  kill $APP_PID
done
