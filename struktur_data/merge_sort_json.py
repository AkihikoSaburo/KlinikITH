
import json

def merge_sort_dict_items(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort_dict_items(items[:mid])
    right = merge_sort_dict_items(items[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_items = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            sorted_items.append(left[i])
            i += 1
        else:
            sorted_items.append(right[j])
            j += 1

    sorted_items.extend(left[i:])
    sorted_items.extend(right[j:])
    return sorted_items

def save_sorted_json_with_merge_sort(filepath, hashtable_data):
    items = list(hashtable_data.items())
    sorted_items = merge_sort_dict_items(items)
    sorted_dict = dict(sorted_items)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(sorted_dict, f, ensure_ascii=False, indent=2)

# Contoh penggunaan:
if __name__ == "__main__":
    sample_data = {
        "241011008": {"nama": "Budi", "prodi": "Ilmu Komputer"},
        "231011003": {"nama": "Ayu", "prodi": "Sistem Informasi"},
        "241011002": {"nama": "Gita", "prodi": "Sains Data"}
    }

    save_sorted_json_with_merge_sort("sorted_pasien_merge.json", sample_data)
