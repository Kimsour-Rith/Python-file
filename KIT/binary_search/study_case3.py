# def top_words(text):
#     a ="!@#$%^&*():'{}<>[]"
#
#     lists = []
#     count = {}
#     if len(text) < 1:
#         return []
#     else:
#         for i in text:
#             if i not in a:
#                 split = list.append(i)
#                 if split not in lists:
#                     count[split] += 1
#                     lists.append(split)
#                 else:
#                     count[split] = 1
#                 return lists
#
#     common_word = sorted(count,key=count.get,reverse=False)
#     top3 = common_word[3:]
#     return top3
#
#
#
# top_words("Hello! Hi@ Good$ Hi Go! @# Go Hello Hi Hi^^ Hi%")
# top_words('hi hello hi wow wow hello good good')
# def top_words(text):
#     counter = 0
#     num = text[0]
#
#     for i in text:
#         curr_frequency = text.count(i)
#         if curr_frequency > counter:
#             counter = curr_frequency
#             num = i
#
#     return num


# text = ["Hello!","Hi@", "Good$","Hi!","Go!@#","Go@%","Hello!","Hi","Hi^^","Hi%"]
# print(top_words(text))

# from collections import Counter
#
# data_set = "Welcome to the world of Geeks " \
#             "This portal has been created to provide well written well" \
#             "thought and well explained solutions for selected questions " \
#             "If you like Geeks for Geeks and would like to contribute " \
#             "here is your chance You can write article and mail your article " \
#             " to contribute at geeksforgeeks org See your article appearing on " \
#             "the Geeks for Geeks main page and help thousands of other Geeks. " \
#
#     # split() returns list of all the words in the string
# split_it = data_set.split()
#
# # Pass the split_it list to instance of Counter class.
# Counter = Counter(split_it)
#
# # most_common() produces k frequently encountered
# # input values and their respective counts.
# most_occur = Counter.most_common(4)
#
# print(most_occur)

# def top_words(text):
#     text_spit=text.split()
#     list=[]
#     for i in text_spit:
#         if i not in list:
#             word=''
#             for element in i:
#                 if element.isalnum():
#                     word += element
#             list.append(i.lower())
#         elif len(list) == 3:
#             break
#     return list


#print(top_words('hi hello hi wow wow hello good good'))

# from collections import Counter
# a = "!@#$%^&*():'{}<>[]"
# text = 'hi! hello# hi! wow!! wow!! hello!! good good'
# lists =[]
# list1 = []
# for i in text:
#     if i in a:
#         lists.append(i)
    # else:
    #     words= text.lower().split()
    #     most_common_words = [word for word, word_count in Counter(words).most_common(3)]
    #     print(most_common_words)


# from collections import Counter
# text = 'hi! hello# hi! wow!! wow!! hello hello!! good good'
# words= text.lower().split()
# most_common_words = [word for word, word_count in Counter(words).most_common(3)]
# list=[]
# list_new=[]
# for i in most_common_words:
#     word=""
#     for j in i:
#         if j.isalnum():
#             word+=j
#     list.append(word)
# for x in list:
#     if x not in list_new:
#         list_new.append(x)
# print(list_new)



#correct anwer are the above two answers
import re
# from collections import Counter
#
# def top_word(text):
#     text = text.lower().split()
#     new = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in text]
#     last_list=[]
#     if len(new) > 3:
#         most_common_words = [word for word, word_count in Counter(new).most_common(3)]
#         return most_common_words
#     for x in new:
#         if x not in last_list:
#             last_list.append(x)
#     return last_list
#
# print(top_word('hi! hello# hi! wow!! wow!! hello hello!! good good'))




import re
from collections import Counter

def top_word(text):
    text = text.lower().split()
    new = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in text]
    if len(new) > 3:
        most_common_words = [word for word, word_count in Counter(new).most_common(3)]
        return most_common_words
    return list(set(new))

print(top_word('hi! hello# hi! wow!! wow!! hello hello!! good good'))