"""MOdule that defines a Student class"""
import json
class Student:
    """"defines a Student class"""
    def __init__(self, first_name, last_name, age):
        """initialization of class instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representaion of Student instance"""
        curr_dict = json.loads(json.dumps((self.__dict__)))
        if isinstance(attrs, list) and len(attrs) > 0:
            dict_keys = [key for key in curr_dict.keys()]
            keys_to_del = [item if item not in attrs else\
                    None for item in dict_keys]
            for item in keys_to_del:
                try:
                    del curr_dict[item]
                except:
                    pass
        return curr_dict

    def reload_from_json(self, json):
        """replaces all attributes of class instance

        Args:
            json: input dictionary to replace current attribute with
        """
        for x in json:
            self.__dict__.update({x: json[x]})
