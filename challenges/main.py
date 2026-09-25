def find_phone_number(contacts, name):
    # TODO: build a dict from `contacts` (list of (name, phone) tuples),
    # then return the phone number for `name`, or "Not found"
    
    phone_book = {}

    for contact_name, phone in contacts:
        phone_book[contact_name] = phone
    
    if name in phone_book:
        return phone_book[name]
    else:
        return 'Not found'

print(find_phone_number([('Ada', '0801'), ('Bola', '0802')], 'Ada'))