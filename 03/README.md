# Домашнее задание к занятию «Средство визуализации Grafana»

## Задание 1

* В docker-compose.yml для prometheus добавляю 

```
ports:
  - 9090:9090
```

* Запускаю docker-compose.yml файл из папки help 

docker-compose up -d

![grafana is up](https://github.com/A-Tagir/monitoring/blob/main/03/CICD_Grafana_up.png)

* Добавляю и тестирую prometheus, как источник данных:

![source_test_ok](https://github.com/A-Tagir/monitoring/blob/main/03/CICD_Grafana_data_sources_test_ok.png)

![data_sources](https://github.com/A-Tagir/monitoring/blob/main/03/CICD_Grafana_data_sources_prometheus.png)

## Задание 2

* Создаю Dashboard и панели

- CPU Usage Total: 100 - ((irate(node_cpu_seconds_total{job="nodeexporter",mode="idle"}[5m])) * 100)

- Средняя загрузка CPU за 1 минуту: node_load1 * 100

- Средняя загрузка CPU за 5 минут:  node_load5 * 100

- Средняя загрузка CPU за 15 минут: node_load15 * 100

- Свободное место на диске: node_filesystem_avail_bytes

- Свободно памяти оперативной: node_memory_MemFree_bytes

* Чтобы убедится, что все корректно отображается, заходим в контейнер с nodeexporter и загружаем процессор:

```
tiger@VM1:~/monitoring/03/help$ docker exec -it 5be036a9431f sh
/ $ cat /dev/random > /dev/null
^C
/ $ exit
```

* Видим, что график отреагировал правильно.

![Dashboard](https://github.com/A-Tagir/monitoring/blob/main/03/CICD_Grafana_dashboard.png)

## Задание 3

