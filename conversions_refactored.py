__author__ = 'wilsonincs'


def converter(fromUnit, toUnit, value):


    convert_distance = {
        'miles': 0.000621371,
        'yards': 1.09361,
        'meters': 1.0}


    convert_temp = {
        'celsius': (1.0, 0),
        'fahrenheit': (1.8, 32),
        'kelvin': (1.0, 273.15)}

    value = float(value)#turn value into float
    fromUnit = str(fromUnit.lower())
    toUnit = str(toUnit.lower())



    if fromUnit in convert_distance and toUnit in convert_distance:
        first_ops = convert_distance[fromUnit]
        sec_ops = convert_distance[toUnit]

        return value * (1/first_ops) * sec_ops

    elif fromUnit in convert_temp and toUnit in convert_temp:
        first_ops = convert_temp[fromUnit][0]
        sec_ops = convert_temp[fromUnit][1]
        third_ops = convert_temp[toUnit][0]
        fourth_ops = convert_temp[toUnit][1]

        return (value - sec_ops) * third_ops / first_ops + fourth_ops

    checking = ((fromUnit in convert_distance) and (toUnit in convert_distance)) \
    or ((fromUnit in convert_temp) and (toUnit in convert_temp))

