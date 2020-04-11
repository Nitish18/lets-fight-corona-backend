
import json

def transform_response(data, group_by_field):
    if not data:
        return []
    for item in data:
        item['value'] = item.pop('id__count')
        item['name'] = item.pop(group_by_field)
    return data

