data = "총매출 : 10000원\n순매출 : 10000원\n객수 : 30"
parsed_data = {}
for line in data.split('\n'):
    key, value = line.split(':')
    parsed_data[key.strip()] = int(value.strip()[:-1])

print(parsed_data)