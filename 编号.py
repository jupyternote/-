import json

def add_hex_id_to_top(json_file_path):
    # 读取JSON文件
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 检查data是否是列表，假设JSON文件中的数据是一个数组
    if not isinstance(data, list):
        print("JSON文件的数据不是列表格式。")
        return

    # 初始化编号计数器
    counter = 0

    # 创建一个新的列表来存储修改后的条目
    new_data = []

    # 为每个条目添加编号属性，并确保编号位于最前面
    for item in data:
        counter += 1
        # 创建一个新字典，将编号作为第一个键值对
        new_item = {'编号': f"0x{counter:05x}"}
        # 将原始条目的内容添加到新字典中，保持原有顺序
        new_item.update(item)
        new_data.append(new_item)

    # 将修改后的数据写回JSON文件
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)

# 假设你已经有了一个JSON文件的路径
json_file_path = '总集合.json'
add_hex_id_to_top(json_file_path)