# NESTRO_CHALLENGE_hackaton
Решение задачи хакатона NESTRO CHALLENGE

Код на Python / Django. Визуализация и интерактив на Streamlit. Умные парсеры.

Чтобы запустить это приложение локально:

1. Клонируйте репозиторий.
```git clone https://github.com/AGoldian/who-the-oil ```
2. Перейдите в директорию с проектом.
```cd who-the-oil```
3. Убедитесь, что у вас установлен Python 3.6+ и остальные зависимости.
```pip install --upgrade```
```pip install -r requirements.txt```
4. Запустите приложение локально
```streamlit run dashboard/dashboard_one.py```

## Введение

Этот проект был создан для решения нескольких ключевых проблем, связанных с анализом данных. Проект включает в себя реализацию механизмов сбора, анализа и визуализации данных с целью повышения эффективности и качества принимаемых решений.

## Проблемы и цели

Проект решает следующие проблемы:

1. **Отсутствие механизмов анализа данных:** В организации отсутствовали эффективные механизмы для анализа данных, что мешало принимать обоснованные решения на основе имеющихся данных.

2. **Необходимость снижения трудозатрат при рассмотрении большого объема данных с одновременным повышением качества их анализа:** Сотрудники были перегружены ручным анализом больших объемов данных, что снижало качество их работы и требовало больших временных затрат.

3. **Объем данных не позволяет оперативно и с необходимой точностью вручную анализировать эффективность принятых решений:** Объем данных был настолько большим, что вручную анализировать его было практически невозможно в оперативном режиме.

Цели проекта включают в себя:

- Создание механизмов для автоматического сбора данных.
- Разработка алгоритмов анализа данных.
- Визуализация данных для удобства интерпретации результатов.
- Уменьшение трудозатрат и повышение качества анализа данных.

## Техническая реализация

### 1. Анализ данных с использованием библиотеки `requests`

Для получения актуальных данных о курсах валют с внешних источников, мы использовали библиотеку `requests` для отправки HTTP-запросов и получения данных.

### 2. Разработка парсера данных из Excel, дальнейшее преобразование файла и выгрузка нового, изменённого файла в формате .xlsx

Для извлечения нужной информации из файлов Excel мы использовали библиотеку openpyxl, которая позволяет работать с файлами Excel в формате xlsx.

### 3. Визуализация данных с использованием фреймворка Streamlit.

Данные фреймворк обладает большой документацией https://docs.streamlit.io/ имеет огромный функционал, масштабируется и к нему достаточно просто прикрутить взаимодействие с бэкендомЮ для дальнейшей загрузки файла уже нее локально, а загрузив его на сайте.


# Разработчики
| Имя                  | Роль           | Контакт               |
|----------------------|----------------|-----------------------|
| Константин Балцат    | Data Analyse | [t.me/baltsat](https://t.me/baltsat)       |
| ---                  | ---            | ---                   |
| Александр Серов      | Machine Learning | [t.me/thegoldian](https://t.me/thegoldian) |
| ---                  | ---            | ---                   |
| Артём Тарасов        | Full stack | [t.me/tarasovxx](https://t.me/tarasovxx)   |
| ---                  | ---            | ---                   |
