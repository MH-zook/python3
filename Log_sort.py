#coding: utf-8
file = open('access.txt', 'rt')
log_file = open('log.txt', 'wt')
tittle = '|{:<20s}|{:<50s}|{:<8s}|{:<8s}|'.format('ip', 'url', 'code', 'count')
print(tittle)
dict_log = {}
for line in file:
    l_line = line.split()
    tp_line = (l_line[0], l_line[6], l_line[8])
    dict_log[tp_line] = dict_log.setdefault(tp_line, 0) + 1
dict_list = list(dict_log.items())
dict_list.sort(key=lambda x: x[1])
'''
#排序和匿名函数混合双打
def sort_list(l, key):
    for i in range(10):
        for j in range(len(l) - 1 - i):
            if key(l[j]) > key(l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
sort_list(dict_list, lambda x: x[1])
'''
for key, value in dict_list[-1:-10:-1]:
    line_get = '|{:<20s}|{:<50s}|{:<8s}|{:<8d}|'.format(key[0], key[1], key[2], value)
    log_file.write('|{:<20s}|{:<50s}|{:<8s}|{:<8d}|\n'.format(key[0], key[1], key[2], value))
    print(line_get)
log_file.close()
file.close()
