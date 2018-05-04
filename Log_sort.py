# encoding: utf-8
file = open('access.txt', 'rt')
log_file = open('log.txt', 'wt')
tittle = '|{:<10s}|{:<20s}|{:<5s}|{:<5s}|'.format('ip', 'error_num', 'error', 'count')
print(tittle)
dict_log = {}
for line in file:
    l_line = line.split()
    tp_line = (l_line[0], l_line[6], l_line[8])
    dict_log[tp_line] = dict_log.setdefault(tp_line, 0) + 1
dict_list = list(dict_log.items())
for i in range(len(dict_list) - 1):
    for j in range(len(dict_list) - 1 - i):
        if dict_list[j][1] > dict_list[j+1][1]:
            dict_list[j], dict_list[j+1] = dict_list[j+1], dict_list[j]
for i in range(-1, -11, -1):
    line_get = '|{:<10s}|{:<20s}|{:<5s}|{:<5d}|'.format(dict_list[i][0][0], dict_list[i][0][1], dict_list[i][0][2], dict_list[i][1])
    log_file.write('|{:<10s}|{:<20s}|{:<5s}|{:<5d}|\n'.format(dict_list[i][0][0], dict_list[i][0][1], dict_list[i][0][2], dict_list[i][1]))
    print(line_get)
log_file.close()
file.close()


