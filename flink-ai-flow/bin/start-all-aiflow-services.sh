#!/usr/bin/env bash
##
## Licensed to the Apache Software Foundation (ASF) under one
## or more contributor license agreements.  See the NOTICE file
## distributed with this work for additional information
## regarding copyright ownership.  The ASF licenses this file
## to you under the Apache License, Version 2.0 (the
## "License"); you may not use this file except in compliance
## with the License.  You may obtain a copy of the License at
##
##   http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing,
## software distributed under the License is distributed on an
## "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
## KIND, either express or implied.  See the License for the
## specific language governing permissions and limitations
## under the License.
##
set -e
usage="Usage: start-all-aiflow-service.sh [notification-database-conn] [airflow-mysql-conn]"

if [ $# -ne 2 ]; then
  echo $usage
  exit 1
fi

NOTIFICATION_DATABASE_CONN=$1
AIRFLOW_MYSQL_CONN=$2
BIN=`dirname "${BASH_SOURCE-$0}"`
BIN=`cd "$BIN"; pwd`

# start notification service
${BIN}/start-notification.sh ${NOTIFICATION_DATABASE_CONN}

# start airflow scheduler and web server
${BIN}/start-airflow.sh ${AIRFLOW_MYSQL_CONN}

# start AIFlow
${BIN}/start-aiflow.sh

echo "Visit http://127.0.0.1:8080/ to access the airflow web server."
