import keyboard as keyb

keyb.add_hotkey('alt + 1', lambda: keyb.write('Здравствуйте \n Что вы хотите продать?\n'))
keyb.add_hotkey('alt + 2', lambda: keyb.write('Отправьте фото ноутбука в открытом виде'))
keyb.add_hotkey('alt + 3', lambda: keyb.write('Отправьте фото с передней и задней стороны'))
keyb.add_hotkey('alt + 4', lambda: keyb.write('напишите характеристики или отправьте фото с передней и задней стороны'))
keyb.add_hotkey('alt + 5', lambda: keyb.write('Микрорайон №2 дом 18б работаем с понедельника по пятницу с 9.00 до 18.00'))
keyb.add_hotkey('alt + 6', lambda: keyb.write('слишком старый такие идут на лом'))
keyb.add_hotkey('alt + 7', lambda: keyb.write('отправьте фото с передней стороны и фото наклейки с задней стороны монитора'))
keyb.add_hotkey('alt + 8', lambda: keyb.write('точнее без знания полных характеристик смогу сказать только после осмотра'))
#keyb.add_hotkey('alt + 9', lambda: keyb.write('Здравствуйте \n Что вы хотите продать?\n'))
#keyb.add_hotkey('alt + 0', lambda: keyb.write('Здравствуйте \n Что вы хотите продать?\n'))

keyb.wait()