#!/bin/bash

# Установите название базы данных и пользователя
DB_NAME="postgres"
DB_USER="postgres"

# Удалите существующую базу данных
dropdb --if-exists -U $DB_USER $DB_NAME
