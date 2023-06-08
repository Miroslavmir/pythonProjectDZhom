# 9.82. Дано предложение, в котором нет символа "-". Определить количество букв о
# # в первом слове. Учесть, что в начале предложения могут быть пробелы.
# string = input('vvod\n')
# lenstring = len(string)
# x = 0
# a = 0
# while True:
#     str = (string.index(' ', x, lenstring))
#     if str == 0:
#         x += 1
#     elif str != 0:
#         a = string.count('o', 0 , str)
#         if a == 0:
#             print('no')
#             break
#     if a != 0:
#         break
# print(a)



# 9.141. Дан текст, в котором имеются цифры.
# а) Найти их сумму.
# б) Найти максимальную цифру.
# ответ А
# string = input("vvod dann") # 3 5 6 7 789
# a = 0
# for summ in string:
#     if summ.isdigit():
#         a += int(summ) + 1
#         print(summ)
# print('a = ',a)
# ответ Б
# s = [int(n) for (n) in string.split()]
# print(max(s))

# 9.161. Даны три слова. Напечатать только те буквы слов, которые есть лишь в одном из слов.
# Рассмотреть два варианта:
# 1) повторяющиеся буквы каждого слова рассматриваются;
# 2) повторяющиеся буквы каждого слова не рассматриваются
# text = input('vvod\n').lower().split()
# str = []
# result = []
# for el in text:
#     for char in el:
#         if char in str:
#             try: result.remove(char)
#             except ValueError: pass
#         else:
#             str.append(char)
#             result.append(char)
# print(* result)

#
# 9.166. Дано предложение. Поменять местами его первое и последнее слово.
# s = input('vvod\n')
# s = s.split(' ')
# print('s.split(' ') - ', end='')
# print(s)
# s = s[::-1]
# print('s[::-1]- ', end='')
# print(s)
# s = ' '.join(s)
# print("' '.join(s) - ", end='')
# print(s)
# вариант2
# string = ' '.join(input().split(' ')[::-1])
# print(string)


# 9.178. Дано предложение. Напечатать все его слова, предварительно преобразовав
# каждое из них по следующему правилу:
# а) заменить первую встреченную букву a на о;
# б) удалить из слова все вхождения последней буквы (кроме нее самой);
# в) оставить в слове только первые вхождения каждой буквы;
# г) в самом длинном слове удалить среднюю (средние) буквы. Принять, что
# такое слово — единственное.
# а)
# string = input('vvod\n')
# result = string.replace('а','о', 1)
# print(result)
# b)
# string = input('vvod\n')
# summ = string[:-1].split()
# lens = len(summ)
# s = []
# for i in summ:
#     if i != summ[lens -1]:
#         s.append(i)
#     print(summ)
#     print(s)
# res = []
# for i in s:
#     n = i[-1]
#     res.append(i.replace(n, '')+ n)
# print(res)
# В
# if __name__ == '__main__':
#     s =input('vvod\n')
#
#     n = s.count('')
# print(n)

