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
- установленный интерпритатор python3 версии 3.8 и выше
- установленный список зависимостей, указанные в файле [requirements.txt](https://github.com/Che3108/LTC_2023/blob/main/requirements.txt)
- Созданная и с необходымыми правами временная папка для хранения полученных от клиентов файлов.<br><br>

Установка и настройка серверной части:
- Клонируем репозиторий git clone https://github.com/Che3108/LTC_2023.git.
- Серверная часть находится в папке server.
- Открываем исполняемый файл server.py и изменяем в нем HOST, PORT, TEMP_FOLDER на собственные ip-адресс сервера (внешний, белый), порт работы приложения, путь ко временной папке соответственно.
- запускаем файл server.py на исполнение.<br><br>

## Как работает
Сервис находится на рукоядке /upload сервера. <br>
Для получения ответа от сервиса необходимо отправить файл методом POST на рукоядку /upload и дожаться ответа от сервиса. <br>
Сервис в ответ отправить данные в формате json, с итоговым расписанием, а так же со всеми необходыми для расчетов промеуточными результатами для последуещей валиадции полученного расписания.

### Клиентская часть
В нашем решении так же предусмотрена клиентская часть.
Для запуска клиентской части потрбуется интерпритор python3 версии 3.8 и выше, а также установленная библиотека [requests](https://pypi.org/project/requests/).<br>
Исполняемый файл находится в корне репозитория и назывется [client.py](https://github.com/Che3108/LTC_2023/blob/main/client.py). <br>
Для настройки клиентской части необходимо в исполняемом файле в переменной ARHIVE_name указать путь к архиву с исходными данными, а так же в переменной URL указать адрем до серверной части. <br>Результатом работы клиентской части будет выведенный в консоль ответ от сервера в формате json 
