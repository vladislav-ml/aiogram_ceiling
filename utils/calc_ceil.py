from settings import logger

from .common import CommonClass


class CalcCeil:

    types_ceilings = [
        {
            'name': 'пвх',
            'price': 500
        },
        {
            'name': 'матовый',
            'price': 750
        },
        {
            'name': 'глянцевый',
            'price': 850
        },
        {
            'name': 'с рисунком',
            'price': 900
        },
        {
            'name': 'звездное небо',
            'price': 1400
        },
        {
            'name': 'тканевый',
            'price': 800
        },
        {
            'name': 'двухуровневый',
            'price': 1100
        },
        {
            'name': 'многоуровневый',
            'price': 1200
        },
    ]

    lights = [
        {
            'name': 'светильники',
            'price': 4000
        },
        {
            'name': 'люстры',
            'price': 7000
        },
        {
            'name': 'светодиоды',
            'price': 10000
        },
        {
            'name': 'подсветка',
            'price': 15000
        },
    ]

    towns = [
        {
            'name': 'Москва',
            'price': 5000
        },
        {
            'name': 'Пушкино',
            'price': 0
        },
        {
            'name': 'Сергиев Посад',
            'price': 2000
        },
        {
            'name': 'Дмитров',
            'price': 3000
        },
        {
            'name': 'Щелково',
            'price': 4000
        },
        {
            'name': 'Лобня',
            'price': 4000
        },
        {
            'name': 'Мытищи',
            'price': 4000
        },
        {
            'name': 'Другой город МО',
            'price': 5000
        },
    ]

    leveling = [
        {
            'name': 'да',
            'price': 1.2
        },
        {
            'name': 'нет',
            'price': 1
        }
    ]

    @classmethod
    def calc_sum(cls, town: str, type_ceiling: str, size: str, perimetr: str, leveiling: bool, light: str) -> str:
        sum = 'Ошибка'
        try:
            town_int = CommonClass.get_data(town, cls.towns)
            type_ceil_int = CommonClass.get_data(type_ceiling, cls.types_ceilings)
            size_int = int(size)
            perimetr_int = int(perimetr)
            light_int = CommonClass.get_data(light, cls.lights)
            leveiling_int = CommonClass.get_data(leveiling, cls.leveling)
            all_sum = int(round((type_ceil_int * size_int + 200 * perimetr_int + light_int + town_int) * leveiling_int, -2))
            sum = cls.formatter(all_sum)
        except Exception as e:
            logger.error(f'Ошибка в калькуляторе - {type(e)}\n{e}')

        return sum

    @classmethod
    def formatter(cls, sum: int) -> str:
        str_format = '{0:,}'.format(sum).replace(',', ' ')
        return str_format + ' р.'
