# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл
# логов web-сервера nginx_logs.txt
#
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
# Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.


import json

def convert():
     with open("nginx_logs.txt", "r", encoding="utf-8" ) as f:
         content = f.read()
         splitcontent = content.splitlines()

         for line in splitcontent:
             pipesplit = line.split(' ')
             my_list = (pipesplit[0], pipesplit[5].replace('"',' '), pipesplit[6])
             print(my_list)

         # в этой части записываем логи в json файл для сокращения
         # объемов памяти, чтобы вновь к нему обратиться


         with open("json_log.json", 'a') as fout:
             json.dump(pipesplit, fout)

convert()

# в этой части я пыталась поработать в лоб, с форматированием строки, но обрабатывалась, только первая строчка,
# удлинение цикла приводило к ошибке



# with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
#
#      splitcontent = f.read().splitlines()
#      # print(splitcontent)
#      for line in splitcontent:
#          my_list = []
#          part1 = line.split(' - - ')
#          part2 = line.split('"')
#          part2_2 = part2[1].replace('HTTP/1.1', ' ')
#          part2_3 = part2_2.split(' ')
#          b = part2_3[0:2]
#          my_list.append(part1[0])
#          my_list.extend(b)
#
#
#
# print(my_list)
