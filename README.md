# Решение задачи №12 от команды Энди-Олли
## Оглавление
- [Постановка задачи](https://github.com/Che3108/LTC_2023/blob/main/README.md#постановка-задачи)
- [Описание решения](https://github.com/Che3108/LTC_2023/blob/main/README.md#описание-решения)
- [Как начать](https://github.com/Che3108/LTC_2023/blob/main/README.md#как-начать)

## Постановка задачи
Необходимо предложить и реализовать алгоритм составления расписания фотосъемки поверхности земли на территории РФ группировкой спутников типа CubeSat в количестве 200-а штук.
Для реализации поставленной задачи предосталены данные о временных интервалах нахождения спутников над территорий РФ, а так же интервалы времени видимости спутников наземными станцими. Так же предоставлены данные о орбитах и характеристика всех 200-а спутников. Результатом решения задачи является расписание передачи данных со спутников на наземные станции, с условием минимизации бездействия спутников, вызванного невозможностью продолжать фотосъемку изза отсутвия свободного места на запоминающим устройстве спутника.

## Описание решения
Решение выполнено в нескольких этапов. Основной код решения находится в файле lib.py в директории сервера и разделен на две основные части: 
- pars_txt_file (чтение данных из исходных текстовых файлов и преобразование исходных данных в табличный вид).
- main_magic (основной блок со всеми необходимыми решениями).
### Этап 1 - получение данных от клиента и реализация взаимодействия с клиентом
Наше решение реализовано в виде микросервиса на базе библиотеки fastAPI языка программирования python3. Взаимодействие с клиентом осуществляется посредством передачи rest-запроса на сервер на рукоятку /upload. Rest-запросом на сервер должен быть передан архив, содержащий исходную информацию для формирования расписания (временные интервалы нахождения спутников над территорией РФ и временные интервалы видимости спутников наземными станциями).
### Этап 2 - преобразование входящей информации
Полученный от клиента архив распаковывается во временную папку, затем итеративно выполняется обработка распакованных текстовых файлов с помощью функции pars_txt_file. Вся собранная информация помещается в две таблицы Facility_df и Russia_df (класс DataFrame библиотеки pandas) и отправляются на дальнейшую обработку.
### Этап 3 - обработка входящей информации
- Полученные на втором этапе данные поступают в таблицу Full_date, содержащую все интервалы видимости для каждой станции каждого спутника и таблицу For_foto - интервалы съемки для каждого спутника с учетом ограничения.
- Затем выполняется рассчет пересечения интервалов между Full_date и For_foto, итог расчета пересечения интервалов помещается в таблицу Full.
- Далее резервируем временные интервалы на съемку, исключая их из интервалов видимости спутников наземными станциями, результат  записываем в таблицу Full_without_foto.
- Вычисляем длительности временных интервадов и помещаем их в таблицу Duration.
- Дополняем Duration расчетами объемов возможной передачи данных с заданными интервалами видимости, результат помещаем в таблицу
Duration_added.
- Рассчитываем непосредственно расписание и помещаем его в таблицу 
final_schdule.<br>
Для упрощения обработки и наглядности результатов все таблицы составляются посуточно. Т.к. в процессе расчета возможно изменение количества спутников, их характеристик, есть промежуточные расчеты суммарных объемов.
### Этап 4 - вывод результатов
Все таблицы с расчетами собираются в единый объект в json-формате и отправляются клиенту. Результирующий json содержит ключи, соответствующие рассчитанным на этапе выше таблицам:
- Full_date
- For_foto
- Full
- Full_without_foto
- Duration
- Duration_added
- final_schdule
### Решение по текущим данным
Результаты расчетов по текущим исходным данным выполнены и находятся в корне репозитория в [excel-таблице](https://github.com/Che3108/LTC_2023/blob/main/%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5_k_0.15.xlsx)
Загруженность наземных станций показана на графиках и находится в папке "загруженность станций".


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

### Как работает
Сервис находится на рукоядке /upload сервера. <br>
Для получения ответа от сервиса необходимо отправить файл методом POST на рукоядку /upload и дожаться ответа от сервиса. <br>
Сервис в ответ отправит данные в формате json, с итоговым расписанием (ключ final_schdule), а так же со всеми необходыми для расчетов промеуточными результатами для последуещей валиадции полученного расписания. Время вычислений может занять 8 минут.

### Клиентская часть
В нашем решении так же предусмотрена клиентская часть.
Для запуска клиентской части потрбуется интерпритор python3 версии 3.8 и выше, а также установленная библиотека [requests](https://pypi.org/project/requests/).<br>
Исполняемый файл находится в корне репозитория и назывется [client.py](https://github.com/Che3108/LTC_2023/blob/main/client.py). <br>
Для настройки клиентской части необходимо в исполняемом файле в переменной ARHIVE_name указать путь к архиву с исходными данными, а так же в переменной URL указать адрем до серверной части. <br>Результатом работы клиентской части будет выведенный в консоль ответ от сервера в формате json 
