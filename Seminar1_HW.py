#!/usr/bin/env python
# coding: utf-8

# ## Домашнее задание 1

# ### Оформляйте ноутбук, используя эти советы:
# -  Номер задачи - заголовок 2
# -  Номер подзадачи - заголовок 3 <br>
# Предоставленные наборы данных оформляйте, как код

# ## Домашнее задание 2
# 

# На складе лежат разные фрукты в разном количестве. Нужно написать функцию, которая на вход принимает любое
# количество названий фруктов и их количество, а возвращает общее количество фруктов на складе

# In[19]:


def stock(**kwargs):
    total = 0
    for value in kwargs.values():
        total += value
    print(f'Total stock = {total} ')


# In[20]:


stock(яблоки = 50, груши = 40, бананы = 60, апельсины = 30, киви = 60, ананасы = 20)


# In[5]:


def total_fruts(**kwargs): # вариант 2
    return sum(kwargs.values())
print(f'Total stock = {total_fruts(яблоки = 50, груши = 40, бананы = 60, апельсины = 30, киви = 60, ананасы = 20)} ')


# ## Домашнее задание 3

# Дан список с затратами на рекламу. Но в данных есть ошибки, некоторые затраты имеют отрицательную величину. Удалите
# такие значения из списка и посчитайте суммарные затраты 
# 

# In[22]:


[100, 125, -90, 345, 655, -1, 0, 200]


# Используйте list comprehensions

# In[7]:


advertising_costs = [100, 125, -90, 345, 655, -1, 0, 200]


# In[8]:


total_costs = 0 # решение через цикл
for i in advertising_costs:
    if i > 0:
        total_costs += i
print(f'Total costs = {total_costs} ')


# In[9]:


total_costs = sum(i for i in advertising_costs if i > 0) # решение через list comprehensions
print('Total costs = {:,.0f} руб.'.format(total_costs))


# In[20]:


sum(num for num in advertising_costs if num >= 0) # вариант 2


# ## Домашнее задание 4

# ### Даны два списка.<br>
# Дата покупки

# In[13]:


data_list = ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29',
             '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23', '2021-09-27','2021-10-02',
             '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09',
             '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']


# Суммы покупок по датам

# In[14]:


sum_list = [1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 7037, 4274, 6275, 4988, 6930, 2971, 6592,
            2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 6333, 5700, 2887]


# ### 4.1 Найдите, какая выручка у компании в ноябре

# Используйте list comprehensions

# In[15]:


november = '-11-' # решение через цикл
# matched_indexes = [] 
revenue_november = 0
i = 0 
length = len(data_list)
while i < length: 
    if november in data_list[i]:
#         matched_indexes.append(i)
        revenue_november+= sum_list[i]
    i += 1
# print(matched_indexes)
print('Revenue in November = {:,.0f} руб.'.format(revenue_november)) 


# In[16]:


revenue_november = sum([sum_list[i] for i in range(len(data_list)) if '-11-' in data_list[i]]) # решение через list comprehensions
print('Revenue in November = {:,.0f} руб.'.format(revenue_november)) 


# 
# ### 4.2 Найдите выручку компании в зависимости от месяца

# Для этого напишите функцию, которая на вход принимает список с датами и список с выручкой, а на выходе словарь, где
# ключи - это месяцы, а значения - это выручка.<br>
# Используйте аннотирование типов.

# In[17]:


def revenue_month(dat_l: list, sum_l: list)-> dict:  # решение для всех месяцев года
    revenue_sum_month = {}
    january = '-01-'
    sum_j = 0
    february = '-02-'
    sum_f = 0
    march = '-03-'
    sum_m = 0
    april = '-04-'
    sum_a = 0
    may = '-05-'
    sum_may = 0
    june = '-06-'
    sum_jun = 0
    july = '-07-'
    sum_jul = 0
    august = '-08-'
    sum_aug = 0
    september = '-09-'
    sum_sep = 0
    october = '-10-'
    sum_oct = 0
    november = '-11-'
    sum_nov = 0
    december = '-12-'
    sum_dec = 0
    i = 0
    length = len(data_list)
    while i < length:
        if january in dat_l[i]:
            sum_j += sum_l[i]
        elif february in dat_l[i]:
            sum_f += sum_l[i]
        elif march in dat_l[i]:
            sum_m += sum_l[i]
            sum_a += sum_l[i]
        elif may in dat_l[i]:
            sum_may += sum_l[i]
        elif june in dat_l[i]:
            sum_jun += sum_l[i]
        elif july in dat_l[i]:
            sum_jul += sum_l[i]
        elif august in dat_l[i]:
            sum_aug += sum_l[i]
        elif september in dat_l[i]:
            sum_sep += sum_l[i]
        elif october in dat_l[i]:
            sum_oct += sum_l[i]
        elif november in dat_l[i]:
            sum_nov += sum_l[i]
        elif december in dat_l[i]:
            sum_dec += sum_l[i]
        i += 1
    revenue_sum_month["january"] = sum_j
    revenue_sum_month["february"] = sum_f
    revenue_sum_month["march"] = sum_m
    revenue_sum_month["april"] = sum_a
    revenue_sum_month["may"] = sum_may
    revenue_sum_month["june"] = sum_jun
    revenue_sum_month["july"] = sum_jul
    revenue_sum_month["august"] = sum_aug
    revenue_sum_month["september"] = sum_sep
    revenue_sum_month["october"] = sum_oct
    revenue_sum_month["november"] = sum_nov
    revenue_sum_month["december"] = sum_dec
    for key,value in list(revenue_sum_month.items()):        
        if revenue_sum_month[key] == 0:
            del revenue_sum_month[key]
    return revenue_sum_month

revenue_month(data_list, sum_list)


# In[21]:


def months_purchases(keys: list, values: list)-> dict:    # вариант 2
    dict_res = {}
    for i in range(len(keys)):
        month = keys[i][5:7]
        if month not in dict_res:
            dict_res[month] = values[i]
        else:
            dict_res[month] += values[i]
    return dict_res
                


# In[19]:


print(months_purchases(data_list,sum_list))

