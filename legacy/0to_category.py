import pandas as pd
import csv


def category(_input, _output):
    """
    Сортирует все строки из файла по категориям
    """
    cosmetic = ['косметолог', 'косметологпрага', 'косметологчехия', 'косметология', 'красота', 'увеличениегуб',
                'чисткалица', 'мезотерапия', 'ботокс', 'маникюр', 'массаж', 'салонкрасоты', 'здоровье', 'шугаринг',
                'контурнаяпластика', 'педикюр', 'биоревитализация', 'врачкосметолог', 'пилинг', 'косметика',
                'уколыкрасоты', 'уход', 'гельлак', 'губы', 'ламинированиересниц', 'акне', 'депиляция', 'plasmapen',
                'дерматолог']
    epilation = ['эпиляция', 'эпиляцияпрага', 'эпиляциячехия', 'шугаринг', 'депиляция', 'гладкаякожа',
                 'лазернаяэпиляция', 'косметология', 'косметолог', 'эпиляциявоск', 'депиляциявоск', 'сахарнаяпаста',
                 'здоровье', 'салонкрасоты', 'восковаядепиляция', 'удалениенежелательныхволос', 'нежелательныеволосы',
                 'шугаринг', 'нетвросшимволосам', 'электроэпиляция', 'сахарнаядепиляция', 'депиляциясахаром',
                 'сахарнаяэпиляция', 'эпиляциясахаром']
    brows_and_lashes = ['брови', 'макияж', 'ресницы', 'красота', 'brows', 'архитектурабровей', 'makeup',
                        'наращиваниересниц', 'маникюр', 'оформлениебровей', 'перманентныймакияж', 'beauty', 'бровист',
                        'хна', 'окрашиваниебровей', 'красивыеброви', 'ламинированиересниц', 'визажистпрага',
                        'визажистчехия', 'ламинированиебровей', 'коррекциябровей', 'реснички', 'brow', 'микроблейдинг',
                        'browhenna']
    makeup = ['визаж', 'визажистпрага', 'макияж', 'makeup', 'красотапрага', 'makeupartist', 'стилист', 'beauty',
              'свадебныймакияж', 'вечерниймакияж', 'fashion', 'визаж', 'макияжглаз', 'мейкап', 'брови', 'mua', 'модель',
              'прически', 'свадьба', 'косметика', 'стиль', 'hair', 'hairstyle', 'прическа', 'самсебевизажист']
    tattoo = ['тату', 'tattoo', 'татуировка', 'татуировки', 'tattoos', 'tattooed', 'tattooart', 'tattooartist',
              'татумастер', 'татумастерпрага', 'татуэскиз', 'tattoosketch', 'перманентныймакияж', 'sketch', 'tattooing',
              'tattoostyle', 'tattooink', 'instatattoo', 'татусалон', 'tattoogirl', 'пирсинг', 'piercing', 'проколушей',
              'пирсингязыка', 'татуаж', 'piercings', 'piercedgirl', 'татунаруке']
    haircut = ['Парикмахер', 'Стрижкамужская', 'Стрижкаженская', 'Стрижкадетская', 'Лечениеволос', 'стилист',
               'окрашивание', 'стрижка', 'волосы', 'hair', 'колорирование', 'укладка', 'уход', 'салонкрасоты',
               'haerdresser', 'карэ', 'бобкаре', 'haer', 'омбрэ', 'завивка', 'harrystyles', 'окрашиваниеволос',
               'прически', 'андеркат', 'балаяж', 'красота', 'hairstyle', 'блонд', 'стрижки', 'barbershop', 'колорист',
               'barber']
    nails = ['ногти', 'маникюр', 'гельлак', 'дизайнногтей', 'nails', 'nail', 'наращиваниеногтей', 'шеллак',
             'аппаратныйманикюр', 'педикюр', 'красивыеногти', 'nailart', 'френч', 'manicure', 'ногтидня', 'маникюрчик',
             'инстаманикюр', 'маникюрдизайн', 'ногтифото', 'маникюрныйинстаграм', 'инстаногти', 'ногтики', 'маникюрдня',
             'комбиманикюр', 'ногтилук']
    massage = ['массаж', 'массажлица', 'коррекцияфигуры', 'massage', 'естественноеомоложение', 'банночныймассаж',
               'самомассаж', 'мимика', 'исполнениежеланий', 'гимнастикадлялица', 'скульптурированиелица', 'осанка']
    stylist = ['стилист', 'парикмахер', 'окрашивание', 'стрижка', 'москва', 'макияж', 'стиль', 'красота', 'визажист',
               'прически', 'fashion', 'локоны', 'спб', 'мода', 'волосы', 'haerdresser', 'колорирование', 'уход',
               'style', 'карэ', 'бобкаре', 'haer', 'завивка', 'hair', 'женская', 'омбрэ', 'harrystyles', 'makeup',
               'свадьба', 'hairstyle']
    psychology = ['психолог', 'психология', 'психологияотношений', 'советыпсихолога', 'логопед', 'саморазвитие',
                  'помощь', 'family', 'psychology', 'психотерапевт', 'психологияличности']
    medicine = ['медсестра', 'медицина', 'поликлиника', 'врачи', 'любимыйдоктор', 'белыехалаты', 'яврач',
                'стоматологпрага', 'медицинскаяодежда', 'айболит']
    fitness = ['тренерпрага', 'тренерчехия', 'спорт', 'фитнес', 'sport', 'fitness', 'тренировка', 'зож', 'пп',
               'мотивация', 'motivation', 'gym', 'персональныйтренер', 'бодибилдинг', 'фитнестренер', 'тренировки',
               'bodybuilding', 'fitnessmotivation', 'спортзал', 'coach', 'тренажерныйзал', 'training', 'sportlife',
               'fitnessgirl', 'sportgirl']

    database = pd.DataFrame(columns=['userid', 'cosmetic', 'epilation', 'brows_and_lashes', 'makeup', 'tattoo',
                                     'haircut', 'nails', 'massage', 'stylist', 'psychology', 'medicine', 'fitness'])

    with open(_input, "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # first row is userid
            database.loc[row[0], 'userid'] = row[0]
            for word in row:
                if word in cosmetic:
                    database.loc[row[0], 'cosmetic'] = 1
                    print(word)
                if word in epilation:
                    database.loc[row[0], 'epilation'] = 1
                    print(word)
                if word in brows_and_lashes:
                    database.loc[row[0], 'brows_and_lashes'] = 1
                    print(word)
                if word in makeup:
                    database.loc[row[0], 'makeup'] = 1
                    print(word)
                if word in tattoo:
                    database.loc[row[0], 'tattoo'] = 1
                    print(word)
                if word in haircut:
                    database.loc[row[0], 'haircut'] = 1
                    print(word)
                if word in nails:
                    database.loc[row[0], 'nails'] = 1
                    print(word)
                if word in massage:
                    database.loc[row[0], 'massage'] = 1
                    print(word)
                if word in stylist:
                    database.loc[row[0], 'stylist'] = 1
                    print(word)
                if word in psychology:
                    database.loc[row[0], 'psychology'] = 1
                    print(word)
                if word in medicine:
                    database.loc[row[0], 'medicine'] = 1
                    print(word)
                if word in fitness:
                    database.loc[row[0], 'fitness'] = 1
                    print(word)

    database.to_csv(_output, index=False)


if __name__ == '__main__':
    category('to_tags.csv', 'final.csv')
