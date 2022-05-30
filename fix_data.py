import json

with open("./data.json") as f:
    data = json.load(f)

should_add_list = ['add1', 'add2', 'add3', 'add4']

has_check_name_list = []

last_list = []

for one_data in data:
    name = one_data['name_id']  # should not repeat

    if (name not in has_check_name_list):
        has_check_name_list.append(name)
        for key in should_add_list:
            one_data[key] = (
                int(one_data[key]) if str(one_data[key]).strip() else 0
            )

        last_list.append(one_data)
    else:
        try:
            index = has_check_name_list.index(name)
            for key_name in should_add_list:
                if not str(one_data[key_name]).strip():
                    num = 0
                else:
                    num = int(one_data[key_name])
                    last_list[index][key_name] += num
        except Exception as e:
            print(one_data)


print(len(data))
print(len(last_list))


with open("./data_fix.json", "w") as f:
    json.dump(last_list, f)
    print("finished...")
