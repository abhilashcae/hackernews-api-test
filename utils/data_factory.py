import json


class JsonReader:
    """
    Deals with reading the JSON data files
    """

    @classmethod
    def read_json_file(cls, file_name, file_path):
        """

        Args:
            file_name: file name
            file_path: path of the json test data file

        Returns: file object

        """
        with open(file_path + '/' + file_name) as data_file:
            data_object = json.load(data_file)
            return data_object
