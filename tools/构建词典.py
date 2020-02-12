import json
import codecs,sys


target = codecs.open('dict.txt', 'w', encoding = 'utf8')
# 批量添加关键词
f='/mnt/data/dev/github/Terry-toolkit/Terry-toolkit/Terry_toolkit/resources/THUOCL.json'
with open(f, 'r') as f:
    data = json.load(f)
    # print(data['动物'])
    all_data=[]
    for key in data.keys():
        all_data=all_data+data[key]
    target.writelines("\n".join(all_data))

        
        # for it in data[key]:
        #     try:
        #         # print('添加关键词',it)
        #         target.writelines(it)
        #     except :
        #         pass
print("well done")
f.close()
target.close()
