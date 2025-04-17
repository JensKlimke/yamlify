
def process(data):
    # Create index of persons
    data['person_index'] = {}
    for person in data['children']['persons']['elements']:
        data['person_index'][person['key']] = person
    for car in data['children']['cars']['elements']:
        if 'owner' in car and data['person_index'][car['owner']]:
            car['owner'] = data['person_index'][car['owner']]
        else:
            car['owner'] = None
    return data