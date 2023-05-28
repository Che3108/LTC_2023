# Решение задачи №12 от команды Энди-Олли
## Оглавление
- [Постановка задачи](https://github.com/Che3108/LTC_2023/blob/main/README.md#постановка-задачи)
- [Описание решения]()
- [Как начать]()

## Постановка задачи
Необходимо предложить и реализовать алгоритм составления расписания фотосъемки поверхности земли на территории РФ группировкой спутников типа CubeSat в количестве 200-а штук.
Для реализации поставленной задачи предосталены данные о временных интервалах нахождения спутников над территорий РФ, а так же интервалы времени видимости спутников наземными станцими. Так же предоставлены данные о орбитах и характеристика всех 200-а спутников. Результатом решения задачи является расписание передачи данных со спутников на наземные станции, с условием минимизации бездействия спутников, вызванного невозможностью продолжать фотосъемку изза отсутвия свободного места на запоминающим устройстве спутника.



## Как начать
### Серверная часть
Для запуска серверной части потребуется:
- ПК с любой операционной системой 
- установленный интерпритатор python3 версии не ниже чем 3.8
- установленный список зависимостей, указанные в файле requirements.txt
