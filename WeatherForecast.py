from pyowm import OWM
from pyowm.utils.config import get_default_config
owm =OWM('d7b48cb7dd4703fb34b7626572b70b81')

place = input(' В каком городе/стране?:')
mgr = owm.weather_manager()
observation= mgr.weather_at_place(place)
w = observation.weather
config_dict = get_default_config()
config_dict['language']= 'ru'

t = w.temperature("celsius")
# температура
t1= t['temp']
t2= t ['feels_like']
t3= t['temp_max']
t4= t['temp_min']
# ветер
wind = w.wind()['speed']
#влажность
humidity = w.humidity
# облачность
cloudy = w.clouds
# статус
st = w.status
# детализированный статус
dt = w.detailed_status
# время
ti = w.reference_time('iso')
# давление
pr = w.pressure['press']
# видимость
vd= w.visibility_distance

print(f'В городе {place} температура {t1} °С, ощушается как {t2} °С, максимальная {t3} °С, минимальная {t4} °С\nСкорость ветра {wind}м/с, влажность {humidity}%, облачность {cloudy}%, статус {st}, детальный статус {dt},\n справочное время {ti}, давление {pr}мм. ртутного столба, видимость {vd} метр')
