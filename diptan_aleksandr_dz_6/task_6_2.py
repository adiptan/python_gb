with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    max_ip_repeat = 0
    ip = ''
    all_ip = [i.split()[0] for i in f]  # Читаю построчно файл, беру тольк ip и добавляю их в список
    unique_ip = set(all_ip)  # делаю из списка множество из уникальных ip
    for el in unique_ip:  #
        if all_ip.count(el) > max_ip_repeat:
            max_ip_repeat = all_ip.count(el)
            ip = el

print(f'{ip} count is : {max_ip_repeat}')
