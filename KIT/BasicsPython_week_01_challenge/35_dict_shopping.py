# def dict_shopping(dic):
#
#
# print(dict_shopping([{"price": 123.49, "quantity": 3}]))  # ('$370.47', 3)
# print(dict_shopping([{"price": 19.99, "quantity": 3}, {"price": 99.99, "quantity": 6}]))  # ('$659.91', 9)
# print(dict_shopping([{"price": 0.01, "quantity": 999}]))  # ('$9.99', 999)
# print(dict_shopping([{"price": 123.49, "quantity": 0}]))  # ('Invalid JSON', 0)
# print(dict_shopping([{"price": -23.49, "quantity": 2}]))  # ('Invalid JSON', 0)
# print(dict_shopping([{"quantity": 2}]))  # ('Invalid JSON', 0)
# print(dict_shopping([{"price": 99.99}]))  # ('Invalid JSON', 0)

# def dict_shopping(ent):
#     error = 0
#     l = []
#     t = []
#
#
#     if len(ent) == 2:        # ent = [{}, {}]
#         for dc in ent:       # dc = {}
#             for i in dc:     # i = key
#                 x = dc[i]    # dc[i] = value
#                 l.append(x)
#         a = l[0]*l[1] + l[2]*l[3]
#         # total = str('$'+str(a))   # $XXX
#         total = '$'+str(a)   # $XXX
#         sum = l[1] + l[3]
#         t.extend([total, sum])
#         print(tuple(t))
#
#
#     elif len(ent) == 1:
#         for dc in ent:   # dc = {}
#             for i in dc:
#                 x = dc[i]
#                 l.append(x)
#
#         if len(l) == 1:
#             print('Invalid JSON', error)
#         elif l[0] >= 0.01 and l[1] >= 1 :
#             a = l[0]*l[1]
#             total = '$'+ str(a)
#             sum = l[1]
#             t.extend([total, sum])
#             print(tuple(t))
#         elif l[0] < 0.01 or l[1] < 1 :
#             print('Invalid JSON', error)
#
#
#
# dict_shopping([{"price" : 123.49, "quantity" : 3}])
# dict_shopping([{"price" : 19.99, "quantity" : 3},{"price" : 99.99, "quantity" : 6}])
# dict_shopping([{"price" : 0.01, "quantity" : 999}])
# dict_shopping([{"price" : 123.49, "quantity" : 0}])
# dict_shopping([{"price" : -23.49, "quantity" : 2}])
# dict_shopping([{"quantity" : 2}])
# dict_shopping([{"price" : 99.99}])