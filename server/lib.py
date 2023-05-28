 #!/usr/bin/python3

import re
import datetime
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def pars_txt_file(data:str):
    columns = ["Station", "Satellite", "Access", "Start Time (UTCG)", "Stop Time (UTCG)", "Duration (sec)"]
    data = data.split('\n')[4:]
    data = [i for i in data if i != '']
    data = [i for i in data if '-----' not in i]
    data = [i for i in data if 'Duration' not in i]
    data = [i for i in data if 'Global' not in i]
    data_temp = list()
    satellite_name = ''
    for row in data:
        if row[0] != ' ':
            satellite_name = row
        else:
            temp_string = satellite_name + row
            temp_string = re.sub(r"(\s{5,})", "    ", temp_string)
            temp_string = temp_string.replace("-To-", ";")
            temp_string = temp_string.replace("    ", ";")
            temp_dict = dict(zip(columns, temp_string.split(";")))
            temp_dict["Start Time (UTCG)"] = datetime.datetime.strptime(temp_dict["Start Time (UTCG)"], "%d %b %Y %H:%M:%S.%f").strftime("%Y-%m-%d %H:%M:%S")
            temp_dict["Stop Time (UTCG)"] = datetime.datetime.strptime(temp_dict["Stop Time (UTCG)"], "%d %b %Y %H:%M:%S.%f").strftime("%Y-%m-%d %H:%M:%S")
            temp_dict["Duration (sec)"] = int(float(temp_dict["Duration (sec)"]))
            data_temp.append(temp_dict)
    return data_temp

def main_magic(Facility_df, Russia_df):
    gbit_to_tb = 1 / 8192 # константа перевода Gbit в Tbyte

    list_date = []
    def date_file(delta_date, max_date):
        #list_date.append(delta_date)
        if delta_date != max_date:
            date_1 = datetime.datetime(delta_date.year, delta_date.month, delta_date.day, 9, 0, 0)
            delta_date = delta_date + datetime.timedelta(days=1)
            date_2 = datetime.datetime(delta_date.year, delta_date.month, delta_date.day, 9, 0, 0)
        else:
            date_1 = datetime.datetime(delta_date.year, delta_date.month, delta_date.day, 9, 0, 0)
            date_2 = datetime.datetime(delta_date.year, delta_date.month, delta_date.day, 23, 59, 59)
        facility_day = Facility_df.loc[np.logical_and(Facility_df['Start Time (UTCG)'] >= date_1,
                                                      Facility_df['Start Time (UTCG)'] < date_2)]
        russia_day = Russia_df.loc[np.logical_and(Russia_df['Start Time (UTCG)'] >= date_1,
                                                   Russia_df['Start Time (UTCG)'] < date_2)]
         return {"delta_date": delta_date, f"Facility_{date_1.date()}": facility_day, f"Russia_{date_1.date()}": russia_day}
 
    def intersection(date_on, date_off, start_date, stop_date):
        """
        Функция поиска пересечения временных периодов
        :param date_on: дата начала первого периода включения
        :param date_off: дата окончания первого периода включения
        :param start_date: дата начала второго периода включения
        :param stop_date: дата окончания второго периода включения
        :return:
        - дата начала и дата окончания общей части периодов
        """
        if date_off < date_on or stop_date < start_date:
            # вот тут надо вывести исключение
            print('Ошибка! Дата начала периода не может быть больше даты окончания')
        else:
            if start_date <= date_on:
                start_date_period = date_on
            else:
                start_date_period = start_date
            if stop_date <= date_off:
                stop_date_period = stop_date
            else:
                stop_date_period = date_off
            if start_date_period >= stop_date_period:
                return date_on, date_on
            else:
                return start_date_period, stop_date_period

    for col in ['Start Time (UTCG)', 'Stop Time (UTCG)']:
        Facility_df[col] = Facility_df[col].apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S'))
        Russia_df[col] = Russia_df[col].apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S'))

    min_date = min(Facility_df['Start Time (UTCG)']).date()
    max_date = max(Facility_df['Start Time (UTCG)']).date()

    result = dict()

    delta_date = min_date
    while max_date != delta_date:
        list_date.append(delta_date)
        temp_dict = date_file(delta_date, max_date)
        delta_date = temp_dict["delta_date"]
        del temp_dict["delta_date"]
        result.update(temp_dict)
    date_file(delta_date, max_date)

    print(*list(result.keys()), sep='\n', end='\n\n')
