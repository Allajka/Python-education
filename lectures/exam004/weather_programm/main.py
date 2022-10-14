# Модуль 5: главный модуль
import html_creater as hc
import xml_generator as xg
import data_provider as dp

# print(hc.create())
# print(xg.create())  # xml часто используют для передачи данных через сервер

hc.new_create(xg.new_create(dp.data_collection()))