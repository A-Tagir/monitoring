# Домашнее задание к занятию «Система сбора логов Elastic Stack»

## Задание 1

* Копируем папку help

* выполняем команду sudo sysctl -w vm.max_map_count=262144 иначе elasticsearch падает с ошибкой

* Запускаем 

docker-compose up -d

* Проверяем docker ps

![docker ps](https://github.com/A-Tagir/monitoring/blob/main/04/CICD_ELK_up.png)

* Заходим в интерфей Kibana

![Kibana Welcome](https://github.com/A-Tagir/monitoring/blob/main/04/CICD_Kibana_Welcome.png)

* Проверяем индексы и видим что статус Yellow. Правим конфигурацию replicas=0 и теперь статус Green:

![Indices Green](https://github.com/A-Tagir/monitoring/blob/main/04/CICD_Kibana_Indices.png)

## Задание 2

* Создаю Data-view из имеющихся индексов logstash-*

![DataView](https://github.com/A-Tagir/monitoring/blob/main/04/CICD_Kibana_DataView.png)

* Просматриваю логи

![Discover](https://github.com/A-Tagir/monitoring/blob/main/04/CICD_Kibana_Discover.png)

