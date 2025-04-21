vacancy_name = input('Название вакансии:')
salary = int(input('Размер заработной платы:'))
num_of_working_hours_per_week = int(
    input('Количество рабочих часов в неделю:'))

hourly_rate: float = salary / num_of_working_hours_per_week

print('По вакансии "' + vacancy_name + '" вы будете получать '
      + str(hourly_rate), 'руб в час')
