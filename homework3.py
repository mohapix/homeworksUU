"""
1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).

  {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
"""

import inspect
from pprint import pprint


class MyClass:

    def __init__(self):
        self.attr1 = 13

    def myclass_multi(self):
        self.attr1 = self.attr1 * 2


myclass_object = MyClass()


def introspection_info(obj):
    attrs_dict = {}
    attrs_dict['type'] = str(type(obj)).split("'")[1]
    attrs_list = []
    attrs_methods = []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if isinstance(attr, int) or isinstance(attr, str) or isinstance(attr, bool):
            attrs_list.append(attr_name)
        else:
            attrs_methods.append(attr_name)
    attrs_dict['attributes'] = attrs_list
    attrs_dict['methods'] = attrs_methods
    obj_module = str(inspect.getmodule(myclass_object)).split("'")
    if obj_module[0] != "None":
        attrs_dict['module'] = obj_module[1]
    else:
        attrs_dict['module'] = obj_module[0]
    return attrs_dict


number_info = introspection_info(42)
pprint(number_info)
myclass_info = introspection_info(myclass_object)
pprint(myclass_info)
