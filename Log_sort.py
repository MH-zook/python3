# encoding: utf-8
file = open('access.txt', 'rt')
log_file = open('log.txt', 'wt')
tittle = '|{:<10s}|{:<20s}|{:<5s}|{:<5s}|'.format('ip', 'url', 'code', 'count')
print(tittle)
dict_log = {}
for line in file:
    l_line = line.split()
    tp_line = (l_line[0], l_line[6], l_line[8])
    dict_log[tp_line] = dict_log.setdefault(tp_line, 0) + 1
dict_list = list(dict_log.items())
for i in range(10):
    for j in range(len(dict_list) - 1):
        if dict_list[j][1] > dict_list[j+1][1]:
            dict_list[j], dict_list[j+1] = dict_list[j+1], dict_list[j]
for key, value in dict_list[-1:-11:-1]:
    line_get = '|{:<10s}|{:<20s}|{:<5s}|{:<5d}|'.format(key[0], key[1], key[2], value)
    log_file.write('|{:<10s}|{:<20s}|{:<5s}|{:<5d}|\n'.format(key[0], key[1], key[2], value))
    print(line_get)
log_file.close()
file.close()
