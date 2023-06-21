import requests
from response.main import *
# result = requests.get('https://api.monobank.ua/bank/currency')
# data = result.json()

# print(data)
# voice_input = 'какой курс евро и доллара'
currency_dict = {
        'доллара': 0,
        "евро": 1,
        "польской злоты": 82,
        "фунта": 3,
        "франка": 5
    }
# for i in currency_dict.keys():
#     if i in voice_input:
#         data[currency_dict[i]]['rateByu']
  

data = [{'currencyCodeA': 840, 'currencyCodeB': 980, 'date': 1685743273, 'rateBuy': 36.65, 'rateCross': 0, 'rateSell': 37.4406}, {'currencyCodeA': 978, 'currencyCodeB': 980, 'date': 1685771773, 'rateBuy': 39.25, 'rateCross': 0, 'rateSell': 40.5006}, {'currencyCodeA': 978, 'currencyCodeB': 840, 'date': 1685743273, 'rateBuy': 1.064, 'rateCross': 0, 'rateSell': 1.078}, {'currencyCodeA': 826, 'currencyCodeB': 980, 'date': 1685783721, 'rateBuy': 0, 'rateCross': 47.0016, 'rateSell': 0}, {'currencyCodeA': 392, 'currencyCodeB': 980, 'date': 1685783644, 'rateBuy': 0, 'rateCross': 0.2701, 'rateSell': 0}, {'currencyCodeA': 756, 'currencyCodeB': 980, 'date': 1685783715, 'rateBuy': 0, 'rateCross': 41.4519, 'rateSell': 0}, {'currencyCodeA': 156, 'currencyCodeB': 980, 'date': 1685783726, 'rateBuy': 0, 'rateCross': 5.2965, 'rateSell': 0}, {'currencyCodeA': 784, 'currencyCodeB': 980, 'date': 1685783733, 'rateBuy': 0, 'rateCross': 10.1918, 'rateSell': 0}, {'currencyCodeA': 971, 'currencyCodeB': 980, 'date': 1663425223, 'rateBuy': 0, 'rateCross': 0.4252, 'rateSell': 0}, {'currencyCodeA': 8, 'currencyCodeB': 980, 'date': 1685783286, 'rateBuy': 0, 'rateCross': 0.3694, 'rateSell': 0}, {'currencyCodeA': 51, 'currencyCodeB': 980, 'date': 1685783353, 'rateBuy': 0, 'rateCross': 0.097, 'rateSell': 0}, {'currencyCodeA': 973, 'currencyCodeB': 980, 'date': 1685373606, 'rateBuy': 0, 'rateCross': 0.0668, 'rateSell': 0}, {'currencyCodeA': 32, 'currencyCodeB': 980, 'date': 1685783657, 'rateBuy': 0, 'rateCross': 0.1553, 'rateSell': 0}, {'currencyCodeA': 36, 'currencyCodeB': 980, 'date': 1685783726, 'rateBuy': 0, 'rateCross': 24.8658, 'rateSell': 0}, {'currencyCodeA': 944, 'currencyCodeB': 980, 'date': 1685783721, 'rateBuy': 0, 'rateCross': 22.0861, 'rateSell': 0}, {'currencyCodeA': 50, 'currencyCodeB': 980, 'date': 1685782124, 'rateBuy': 0, 'rateCross': 0.3485, 'rateSell': 0}, {'currencyCodeA': 975, 'currencyCodeB': 980, 'date': 1685783739, 'rateBuy': 0, 'rateCross': 20.5246, 'rateSell': 0}, {'currencyCodeA': 48, 'currencyCodeB': 980, 'date': 1685782875, 'rateBuy': 0, 'rateCross': 99.3133, 'rateSell': 0}, {'currencyCodeA': 108, 'currencyCodeB': 980, 'date': 1538606522, 'rateBuy': 0, 'rateCross': 0.0158, 'rateSell': 0}, {'currencyCodeA': 96, 'currencyCodeB': 980, 'date': 1684824236, 'rateBuy': 0, 'rateCross': 27.8968, 'rateSell': 0}, {'currencyCodeA': 68, 'currencyCodeB': 980, 'date': 1685730089, 'rateBuy': 0, 'rateCross': 5.4629, 'rateSell': 0}, {'currencyCodeA': 986, 'currencyCodeB': 980, 'date': 1685777688, 'rateBuy': 0, 'rateCross': 7.5674, 'rateSell': 0}, {'currencyCodeA': 72, 'currencyCodeB': 980, 'date': 1681978995, 'rateBuy': 0, 'rateCross': 2.8521, 'rateSell': 0}, {'currencyCodeA': 933, 'currencyCodeB': 980, 'date': 1685783331, 'rateBuy': 0, 'rateCross': 12.8176, 'rateSell': 0}, {'currencyCodeA': 124, 'currencyCodeB': 980, 'date': 1685783594, 'rateBuy': 0, 'rateCross': 27.9381, 'rateSell': 0}, {'currencyCodeA': 976, 'currencyCodeB': 980, 'date': 1655462332, 'rateBuy': 0, 'rateCross': 0.0163, 'rateSell': 0}, {'currencyCodeA': 152, 'currencyCodeB': 980, 'date': 1685764915, 'rateBuy': 0, 'rateCross': 0.047, 'rateSell': 0}, {'currencyCodeA': 170, 'currencyCodeB': 980, 'date': 1685781664, 'rateBuy': 0, 'rateCross': 0.0084, 'rateSell': 0}, {'currencyCodeA': 188, 'currencyCodeB': 980, 'date': 1685763711, 'rateBuy': 0, 'rateCross': 0.0693, 'rateSell': 0}, {'currencyCodeA': 192, 'currencyCodeB': 980, 'date': 1685743205, 'rateBuy': 0, 'rateCross': 1.5237, 'rateSell': 0}, {'currencyCodeA': 203, 'currencyCodeB': 980, 'date': 1685783737, 'rateBuy': 0, 'rateCross': 1.7066, 'rateSell': 0}, {'currencyCodeA': 262, 'currencyCodeB': 980, 'date': 1678810696, 'rateBuy': 0, 'rateCross': 0.2108, 'rateSell': 0}, {'currencyCodeA': 208, 'currencyCodeB': 980, 'date': 1685783622, 'rateBuy': 0, 'rateCross': 5.4188, 'rateSell': 0}, {'currencyCodeA': 12, 'currencyCodeB': 980, 'date': 1685783198, 'rateBuy': 0, 'rateCross': 0.2747, 'rateSell': 0}, {'currencyCodeA': 818, 'currencyCodeB': 980, 'date': 1685783409, 'rateBuy': 0, 'rateCross': 1.2141, 'rateSell': 0}, {'currencyCodeA': 230, 'currencyCodeB': 980, 'date': 1684036036, 'rateBuy': 0, 'rateCross': 0.6906, 'rateSell': 0}, {'currencyCodeA': 981, 'currencyCodeB': 980, 'date': 1685783738, 'rateBuy': 0, 'rateCross': 14.5, 'rateSell': 0}, {'currencyCodeA': 936, 'currencyCodeB': 980, 'date': 1685783706, 'rateBuy': 0, 'rateCross': 3.4664, 'rateSell': 0}, {'currencyCodeA': 270, 'currencyCodeB': 980, 'date': 1685748930, 'rateBuy': 0, 'rateCross': 0.6439, 'rateSell': 0}, {'currencyCodeA': 324, 'currencyCodeB': 980, 'date': 1685702709, 'rateBuy': 0, 'rateCross': 0.0044, 'rateSell': 0}, {'currencyCodeA': 344, 'currencyCodeB': 980, 'date': 1685782661, 'rateBuy': 0, 'rateCross': 4.784, 'rateSell': 0}, {'currencyCodeA': 191, 'currencyCodeB': 980, 'date': 1680625280, 'rateBuy': 0, 'rateCross': 5.4258, 'rateSell': 0}, {'currencyCodeA': 348, 'currencyCodeB': 980, 'date': 1685783731, 'rateBuy': 0, 'rateCross': 0.1089, 'rateSell': 0}, {'currencyCodeA': 360, 'currencyCodeB': 980, 'date': 1685783727, 'rateBuy': 0, 'rateCross': 0.0024, 'rateSell': 0}, {'currencyCodeA': 376, 'currencyCodeB': 980, 'date': 1685783661, 'rateBuy': 0, 'rateCross': 10.0271, 'rateSell': 0}, {'currencyCodeA': 356, 'currencyCodeB': 980, 'date': 1685783544, 'rateBuy': 0, 'rateCross': 0.4555, 'rateSell': 0}, {'currencyCodeA': 368, 'currencyCodeB': 980, 'date': 1685775875, 'rateBuy': 0, 'rateCross': 0.0286, 'rateSell': 0}, {'currencyCodeA': 364, 'currencyCodeB': 980, 'date': 1685743205, 'rateBuy': 0, 'rateCross': 0.0009, 'rateSell': 0}, {'currencyCodeA': 352, 'currencyCodeB': 980, 'date': 1685777657, 'rateBuy': 0, 'rateCross': 0.2676, 'rateSell': 0}, {'currencyCodeA': 400, 'currencyCodeB': 980, 'date': 1685775284, 'rateBuy': 0, 'rateCross': 52.79, 'rateSell': 0}, {'currencyCodeA': 404, 'currencyCodeB': 980, 'date': 1685782381, 'rateBuy': 0, 'rateCross': 0.2697, 'rateSell': 0}, {'currencyCodeA': 417, 'currencyCodeB': 980, 'date': 1685781980, 'rateBuy': 0, 'rateCross': 0.4276, 'rateSell': 0}, {'currencyCodeA': 116, 'currencyCodeB': 980, 'date': 1685527854, 'rateBuy': 0, 'rateCross': 0.0091, 'rateSell': 0}, {'currencyCodeA': 408, 'currencyCodeB': 980, 'date': 1685743205, 'rateBuy': 0, 'rateCross': 16.6221, 'rateSell': 0}, {'currencyCodeA': 410, 'currencyCodeB': 980, 'date': 1685783710, 'rateBuy': 0, 'rateCross': 0.0288, 'rateSell': 0}, {'currencyCodeA': 414, 'currencyCodeB': 980, 'date': 1685780714, 'rateBuy': 0, 'rateCross': 121.897, 'rateSell': 0}, {'currencyCodeA': 398, 'currencyCodeB': 980, 'date': 1685783528, 'rateBuy': 0, 'rateCross': 0.0836, 'rateSell': 0}, {'currencyCodeA': 418, 'currencyCodeB': 980, 'date': 1685770511, 'rateBuy': 0, 'rateCross': 0.002, 'rateSell': 0}, {'currencyCodeA': 422, 'currencyCodeB': 980, 'date': 1685265301, 'rateBuy': 0, 'rateCross': 0.0004, 'rateSell': 0}, {'currencyCodeA': 144, 'currencyCodeB': 980, 'date': 1685783643, 'rateBuy': 0, 'rateCross': 0.129, 'rateSell': 0}, {'currencyCodeA': 434, 'currencyCodeB': 980, 'date': 1674670757, 'rateBuy': 0, 'rateCross': 7.8783, 'rateSell': 0}, {'currencyCodeA': 504, 'currencyCodeB': 980, 'date': 1685772874, 'rateBuy': 0, 'rateCross': 3.6902, 'rateSell': 0}, {'currencyCodeA': 498, 'currencyCodeB': 980, 'date': 1685783730, 'rateBuy': 0, 'rateCross': 2.1159, 'rateSell': 0}, {'currencyCodeA': 969, 'currencyCodeB': 980, 'date': 1685082195, 'rateBuy': 0, 'rateCross': 0.0085, 'rateSell': 0}, {'currencyCodeA': 807, 'currencyCodeB': 980, 'date': 1685783612, 'rateBuy': 0, 'rateCross': 0.6514, 'rateSell': 0}, {'currencyCodeA': 496, 'currencyCodeB': 980, 'date': 1685712190, 'rateBuy': 0, 'rateCross': 0.0107, 'rateSell': 0}, {'currencyCodeA': 478, 'currencyCodeB': 980, 'date': 1685743205, 'rateBuy': 0, 'rateCross': 0.1067, 'rateSell': 0}, {'currencyCodeA': 480, 'currencyCodeB': 980, 'date': 1685782148, 'rateBuy': 0, 'rateCross': 0.8195, 'rateSell': 0}, {'currencyCodeA': 454, 'currencyCodeB': 980, 'date': 1678369785, 'rateBuy': 0, 'rateCross': 0.0368, 'rateSell': 0}, {'currencyCodeA': 484, 'currencyCodeB': 980, 'date': 1685782490, 'rateBuy': 0, 'rateCross': 2.1499, 'rateSell': 0}, {'currencyCodeA': 458, 'currencyCodeB': 980, 'date': 1685783620, 'rateBuy': 0, 'rateCross': 8.185, 'rateSell': 0}, {'currencyCodeA': 943, 'currencyCodeB': 980, 'date': 1685609027, 'rateBuy': 0, 'rateCross': 0.5911, 'rateSell': 0}, {'currencyCodeA': 516, 'currencyCodeB': 980, 'date': 1685722191, 'rateBuy': 0, 'rateCross': 1.9133, 'rateSell': 0}, {'currencyCodeA': 566, 'currencyCodeB': 980, 'date': 1685777476, 'rateBuy': 0, 'rateCross': 0.0804, 'rateSell': 0}, {'currencyCodeA': 558, 'currencyCodeB': 980, 'date': 1685645313, 'rateBuy': 0, 'rateCross': 1.0362, 'rateSell': 0}, {'currencyCodeA': 578, 'currencyCodeB': 980, 'date': 1685783734, 'rateBuy': 0, 'rateCross': 3.4173, 'rateSell': 0}, {'currencyCodeA': 524, 'currencyCodeB': 980, 'date': 1685782300, 'rateBuy': 0, 'rateCross': 0.2844, 'rateSell': 0}, {'currencyCodeA': 554, 'currencyCodeB': 980, 'date': 1685771428, 'rateBuy': 0, 'rateCross': 22.885, 'rateSell': 0}, {'currencyCodeA': 512, 'currencyCodeB': 980, 'date': 1685780823, 'rateBuy': 0, 'rateCross': 97.4824, 'rateSell': 0}, {'currencyCodeA': 604, 'currencyCodeB': 980, 'date': 1685763421, 'rateBuy': 0, 'rateCross': 10.209, 'rateSell': 0}, {'currencyCodeA': 608, 'currencyCodeB': 980, 'date': 1685781804, 'rateBuy': 0, 'rateCross': 0.6721, 'rateSell': 0}, {'currencyCodeA': 586, 'currencyCodeB': 980, 'date': 1685783223, 'rateBuy': 0, 'rateCross': 0.1312, 'rateSell': 0}, {'currencyCodeA': 985, 'currencyCodeB': 980, 'date': 1685783741, 'rateBuy': 0, 'rateCross': 8.9919, 'rateSell': 0}, {'currencyCodeA': 600, 'currencyCodeB': 980, 'date': 1685782678, 'rateBuy': 0, 'rateCross': 0.0051, 'rateSell': 0}, {'currencyCodeA': 634, 'currencyCodeB': 980, 'date': 1685781266, 'rateBuy': 0, 'rateCross': 10.2836, 'rateSell': 0}, {'currencyCodeA': 946, 'currencyCodeB': 980, 'date': 1685783741, 'rateBuy': 0, 'rateCross': 8.1507, 'rateSell': 0}, {'currencyCodeA': 941, 'currencyCodeB': 980, 'date': 1685783578, 'rateBuy': 0, 'rateCross': 0.3424, 'rateSell': 0}, {'currencyCodeA': 682, 'currencyCodeB': 980, 'date': 1685781862, 'rateBuy': 0, 'rateCross': 9.9918, 'rateSell': 0}, {'currencyCodeA': 690, 'currencyCodeB': 980, 'date': 1685729756, 'rateBuy': 0, 'rateCross': 2.752, 'rateSell': 0}, {'currencyCodeA': 938, 'currencyCodeB': 980, 'date': 1680961561, 'rateBuy': 0, 'rateCross': 0.0627, 'rateSell': 0}, {'currencyCodeA': 752, 'currencyCodeB': 980, 'date': 1685783741, 'rateBuy': 0, 'rateCross': 3.5045, 'rateSell': 0}, {'currencyCodeA': 702, 'currencyCodeB': 980, 'date': 1685782925, 'rateBuy': 0, 'rateCross': 27.8833, 'rateSell': 0}, {'currencyCodeA': 694, 'currencyCodeB': 980, 'date': 1664217991, 'rateBuy': 0, 'rateCross': 0.0024, 'rateSell': 0}, {'currencyCodeA': 706, 'currencyCodeB': 980, 'date': 1683386099, 'rateBuy': 0, 'rateCross': 0.0659, 'rateSell': 0}, {'currencyCodeA': 968, 'currencyCodeB': 980, 'date': 1680879569, 'rateBuy': 0, 'rateCross': 1.0284, 'rateSell': 0}, {'currencyCodeA': 760, 'currencyCodeB': 980, 'date': 1685743205, 'rateBuy': 0, 'rateCross': 0.0056, 'rateSell': 0}, {'currencyCodeA': 748, 'currencyCodeB': 980, 'date': 1668614714, 'rateBuy': 0, 'rateCross': 2.1898, 'rateSell': 0}, {'currencyCodeA': 764, 'currencyCodeB': 980, 'date': 1685783714, 'rateBuy': 0, 'rateCross': 1.0862, 'rateSell': 0}, {'currencyCodeA': 972, 'currencyCodeB': 980, 'date': 1685783644, 'rateBuy': 0, 'rateCross': 3.4311, 'rateSell': 0}, {'currencyCodeA': 795, 'currencyCodeB': 980, 'date': 1685743205, 'rateBuy': 0, 'rateCross': 0.0021, 'rateSell': 0}, {'currencyCodeA': 788, 'currencyCodeB': 980, 'date': 1685733798, 'rateBuy': 0, 'rateCross': 12.1062, 'rateSell': 0}, {'currencyCodeA': 949, 'currencyCodeB': 980, 'date': 1685783734, 'rateBuy': 0, 'rateCross': 1.8016, 'rateSell': 0}, {'currencyCodeA': 901, 'currencyCodeB': 980, 'date': 1685783517, 'rateBuy': 0, 'rateCross': 1.2209, 'rateSell': 0}, {'currencyCodeA': 834, 'currencyCodeB': 980, 'date': 1685783260, 'rateBuy': 0, 'rateCross': 0.0162, 'rateSell': 0}, {'currencyCodeA': 800, 'currencyCodeB': 980, 'date': 1685718649, 'rateBuy': 0, 'rateCross': 0.0099, 'rateSell': 0}, {'currencyCodeA': 858, 'currencyCodeB': 980, 'date': 1685717176, 'rateBuy': 0, 'rateCross': 0.9664, 'rateSell': 0}, {'currencyCodeA': 860, 'currencyCodeB': 980, 'date': 1685783548, 'rateBuy': 0, 'rateCross': 0.0032, 'rateSell': 0}, {'currencyCodeA': 937, 'currencyCodeB': 980, 'date': 1685743205, 'rateBuy': 0, 'rateCross': 1.3784, 'rateSell': 0}, {'currencyCodeA': 704, 'currencyCodeB': 980, 'date': 1685782967, 'rateBuy': 0, 'rateCross': 0.0015, 'rateSell': 0}, {'currencyCodeA': 950, 'currencyCodeB': 980, 'date': 1685710790, 'rateBuy': 0, 'rateCross': 0.0609, 'rateSell': 0}, {'currencyCodeA': 952, 'currencyCodeB': 980, 'date': 1685739517, 'rateBuy': 0, 'rateCross': 0.0614, 'rateSell': 0}, {'currencyCodeA': 886, 'currencyCodeB': 980, 'date': 1543715495, 'rateBuy': 0, 'rateCross': 0.112, 'rateSell': 0}, {'currencyCodeA': 710, 'currencyCodeB': 980, 'date': 1685783273, 'rateBuy': 0, 'rateCross': 1.931, 'rateSell': 0}, {'currencyCodeA': 894, 'currencyCodeB': 980, 'date': 1685743205, 'rateBuy': 0, 'rateCross': 0.0019, 'rateSell': 0}]

def currency(voice_input):
    global data
    result = requests.get('https://api.monobank.ua/bank/currency')
    if result.status_code == 200:
        data = result.json()
    for i in currency_dict.keys():
        if i in voice_input:
            buy = data[currency_dict[i]]['rateBuy']
            sell = data[currency_dict[i]]['rateSell']
            cross = data[currency_dict[i]]['rateCross']
            if sell == 0 and buy == 0:
                tts_engine.say(f"Сейчас курс {i} в продаже и покупке {round(cross,2)}")
            else:
                tts_engine.say(f"Сейчас курс {i} в продаже {round(buy,2)}, а в покупке {round(sell,2)}")
                
list_tolking.append(Tolking(
    ['какой курс'], currency
))