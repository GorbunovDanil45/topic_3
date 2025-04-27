distance = int(input('Введите расстояние до пункта назначения в км:'))
average_speed = int(input('Введите среднюю скорость в км/ч:'))
hours: int = distance // average_speed
minutes: int = hours * 60 % 60

print('При расстоянии', distance, 'км. и скорости', average_speed,
      'км\ч. время в пути:', hours, 'часа', minutes, 'минут.')
