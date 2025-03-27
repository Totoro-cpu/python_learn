# 打开并读取txt文件
with open('Polyfix.txt', 'r', encoding='gb2312') as file:
    lines = file.readlines()

# 定义一个空列表，用于存储转换后的对象
data_list = []
current_data = {}

# 遍历文件的每一行
for line in lines:
    line = line.strip()  # 去除首尾的空白字符
    if not line:
        continue  # 跳过空行

    # 假设每条记录以特定模式开始，例如以方括号开头
    if line.startswith('[') and line.endswith(']'):
        # 如果已经有一个记录在解析中，将其添加到列表
        if current_data:
            data_list.append(current_data)
            current_data = {}
        # 提取记录的标识符
        record_id = line[1:-1]
        current_data['record_id'] = record_id
    else:
        # 假设每行是一个键值对，用等号分隔
        if '=' in line:
            key, value = line.split('=', 1)
            current_data[key.strip()] = value.strip()

# 添加最后一个记录
if current_data:
    data_list.append(current_data)

# 将 PhotoVolt 没有值的 StationName 保存到文件中
output_file = 'output.txt'
with open(output_file, 'w', encoding='gb2312') as f:
    for data in data_list:
        if data.get('PhotoVolt') in ('', '无', 'None', 'null'):
            f.write(data.get('StationName', '') + '\n')

print(f"结果已保存到 {output_file} 文件中")