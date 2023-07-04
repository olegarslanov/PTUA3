# Docker ////

# Pagrindinis skirtumas tarp konteinerio ir vaizdo yra tai, kad vaizdas yra pasyvus, nevykdomas failų rinkinys,
# o konteineris yra aktyvus procesas, veikiantis pagal vaizdo aprašymą. 
# Galima manyti, kad vaizdas yra programos arba paslaugos šablonas, o konteineris yra paleistas atvejis,
# naudojantis šiuo šablonu. 

### Работа с изображениями ////

# Откройте терминал или командную строку и введите следующую команду, чтобы загрузить образ Docker:
docker pull <image_name>

# Как только образ загружен, вы можете запустить из него контейнер, набрав:
docker run <image_name>

# Чтобы просмотреть все изображения, которые вы уже скачали:
docker image list
docker image ls

# Чтобы удалить изображение из списка:
docker rmi <image_id>


### Работа с контейнерами ////

# Запустите контейнер Docker:
docker run <image_name>

# Список всех запущенных контейнеров:
docker ps

# Остановить работающий контейнер:
docker stop <container_id>

# Удаление остановленного контейнера:
docker rmi <container_id>

# Просмотр логов из контейнера:
docker logs <container_id>

# Запустите остановленный контейнер:
docker start <container_id>