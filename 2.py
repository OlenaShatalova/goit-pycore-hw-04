from pprint import pprint

def get_cats_info(path: str) -> list :
    cats_list = []

    try:
        with open(path, 'r', encoding="utf-8") as f:
            for line in f:
                cat_id, name, age = line.strip().split(",")

                cats_list.append({
                    'id': cat_id,
                    'name': name,
                    'age': age
                })

        return cats_list

    except FileNotFoundError:
        print("File not found")
        return []


cats_info = get_cats_info("data/cats_file.txt")
pprint(cats_info)
