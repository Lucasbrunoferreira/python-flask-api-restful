def object_id(data):
    if type(data) is list:
        for i, x in enumerate(data):
            data[i]['id'] = data[i]['_id']['$oid']
            del data[i]['_id']
        return data
    elif type(data) is dict:
        if '$oid' in data['_id']:
            data['id'] = data['_id']['$oid']
            del data['_id']
            return data
        else:
            raise ValueError
    else:
        raise TypeError
