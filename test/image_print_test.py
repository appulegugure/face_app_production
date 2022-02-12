import json

with open('../image_dir/naikaku_list/g7_member_list.json') as f:
    jsn = json.load(f)

print(jsn)
