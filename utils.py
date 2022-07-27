def remove_repeated_dicts_from_list(target_list):
    seen_dicts = set()
    new_list = []
    for dict_item in target_list:
        t = tuple(sorted(dict_item.items()))
        if t not in seen_dicts:
            seen_dicts.add(t)
            new_list.append(dict_item)
    return new_list


def format_datetime_obj(datetime_obj):
    query_date_format = "%Y-%m-%dT%H:%M:%S"
    return datetime_obj.strftime(query_date_format)
