#!/bin/bash

cd src

if [[ "${1}" == "celery" ]]; then
  celery -A celery_app:celery_app worker --loglevel=INFO
elif [[ "${1}" == "flower" ]]; then
  celery -A celery_app:celery_app flower
 fi
