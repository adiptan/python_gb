file_content = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split()
        file_content.append((line[0], line[5].replace('"', ''), line[6]))

print(file_content)
