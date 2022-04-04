import json


class Serializer:
    def serialize(self, file_name, serializable_object):
        dump = json.dumps(deep_serialize(serializable_object))
        f = open(file_name, "wb+")
        f.write(bytes(dump, "utf-8"))
        f.close()

    def deserialize(self, file_name): #, classx=Object
        f = open(file_name, "rb")
        text = f.read()
        js = json.loads(text)
        f.close()
        # obj = classx()
        # obj.__dict__ = js
        return js


def isobject(obj):
    return not type(obj).__module__ == "builtins"


def deep_serialize(obj):
    if isobject(obj):
        obj = vars(obj)
    if isinstance(obj, dict):
        for k, value in obj.items():
            obj[k] = deep_serialize(value)
    if isinstance(obj, list):
        for i in range(0, len(obj)):
            obj[i] = deep_serialize(obj[i])
    return obj
