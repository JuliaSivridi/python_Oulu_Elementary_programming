def filter_errors(filter_list, level):
    for el in filter_list[:]:
        if el > level:
            filter_list.remove(el)

measurements = [12.2, 54.2, 42345.2, 23534.1, 55.7, 8982.4]
filter_errors(measurements, 8000)
print(measurements)
