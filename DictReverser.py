from functools import reduce


class DictReverser:
    """Rreverse the key-value order of a nested dict.
    
    source_dict: dict
        Each layer has only a pair of key-value.
    """
    def __init__(self, source_dict):
        self.source_dict = source_dict

    def reverse(self):
        """get the reversed version of source_dict"""
        k, v = self.__split_items(self.source_dict)
        flatten_list = self.__flatten_to_list(k, v)

        return reduce(
            lambda x, y: {y: x},
            flatten_list
        )

    def __flatten_to_list(self, key, value):
        """Call by `reverse` to get a flatten list"""
        if isinstance(value, dict):
            child_key, child_value = self.__split_items(value)
            return [key] + self.__flatten_to_list(child_key, child_value)
        else:
            return [key, value]

    def __split_items(self, source):
        """Called by `__flatten_to_list` to get 'key' and 'value' of dict"""
        for key, value in source.items():
            return key, value
