# Домашнее задание к занятию «Системы мониторинга»

## Задание 1

* Вас пригласили настроить мониторинг на проект. На онбординге вам рассказали, что проект представляет из себя платформу для вычислений с выдачей текстовых отчетов, которые      сохраняются на диск. Взаимодействие с платформой осуществляется по протоколу http. Также вам отметили, что вычисления загружают ЦПУ. Какой минимальный набор метрик вы выведите в мониторинг и почему?

* Ответ:
  
  Здесь нужны будут следующие метрики:

  - Свободное место на диске:   если диск заполнится отчетами или логами то система перестанет быть доступной.
  
  - Число запросов/ответов http (успешных 2-- /с ошибкой (коды ошибок 4--, 5--))  -  Если число ответов с ошибкой выше заданного в SLA значит нужно вмешательство

  - Загрузка CPU   -   Слишком высокая загрузка CPU может указывать на медленную работу и проблемы с ПО (необходима вмешательство - оптимизировать ПО или масштабировать платформу)
  
  - Загрузка оперативной памяти - Слишком маленькое количество свободного RAM указывает на неоптимальную работу ПО. Необходимо либо увеличивать RAM либо оптимизировать ПО.

  - Inodes/Files number - хотя число возможных inodes обычно велико и достаточно для большинства задач, однако некоторые системы виртуализации позволяют ставить лимиты
    Поэтому, особенно, если очеты сохраняются на диск (в БД или как отдельные файлы?) то эти параметры лучше отслеживать. Если превысят предел то система перестанет 
    быть доступной с признаками нехватки места на диске.
  
## Задание 2

* 



