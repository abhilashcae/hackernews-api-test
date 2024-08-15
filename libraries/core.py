import json
import os
import shutil
import traceback

import jsonschema
import pytest
import requests

from conf import config, constants
from utils.data_factory import JsonReader
from utils.errors import Errors


class Core:

    def __init__(self):
        pass

    def validate_json_schema(self, instance, schema_file_name, schema_file_path=config.paths['json_schema']):
        schema = JsonReader.read_json_file(schema_file_name, schema_file_path)
        try:
            jsonschema.validate(json.loads(json.dumps(instance)), schema)
        except:
            self.mark_test_fail()

    def make_request_and_get_response(self, request_type, url, payload=None, headers=None):
        if isinstance(payload, dict): payload = json.dumps(payload)
        response = requests.get(url, headers=headers) if request_type == constants.GET_REQUEST else \
            requests.post(url, data=payload, headers=headers) if request_type == constants.POST_REQUEST else \
                requests.delete(url, headers=headers) if request_type == constants.DELETE_REQUEST else \
                    requests.put(url, data=payload, headers=headers)
        return response

    def verify_200_ok_response_code(self, status_code, url):
        try:
            assert status_code == requests.codes.ok, Errors.invalid_response_code(status_code, url, requests.codes.ok)
        except:
            self.mark_test_fail()

    def mark_test_fail(self, message='', logs=''):
        message += '\n\nStack Trace: {}'.format(traceback.format_exc())
        pytest.fail(message + '\n' + logs)

    def remove_directory(self, directory_path):
        """
        Remove directory if it exists
        :param directory_path: path of the directory to be removed
        """
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)