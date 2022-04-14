def words_to_object(s):
    return "[" + ', '.join("{" + f"name : \'{d['name']}\', id : \'{d['id']}\'" + "}" for d in [{"name": ele[0], "id": ele[1]} for ele in list(zip(*(iter(s.split()),) *2))]) + "]"
