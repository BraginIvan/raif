# Raifhack DS 2021

## Команда OldStar

Решение приведено в формате Jupyter Notebook.

Внешние данные не использовались.

Краткое описание решения:

    Считывам данные
    Сразу находим ближайших соседей с объявлеными ценами
    Проводим преобразование данных (квантильное преобразование, минимакс, хотэнкод)
    Обучаем модели сразу на цену price_type == 1
    Для обучения используются XGB, CatBoost
    Используется поиск оптимальных весов для построения ансамбля моделей

Для воспроизведения решения необходимо положить данные в папку datasets и запустить все ячейки ноутбука Final fit-predict.ipynb.

В requirements.txt перечислены требумые пакеты.
