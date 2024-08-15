import os

# Paths
root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
paths = {
    'project_root': root,
    'allure_results': root + '/allure-results',
    'json_schema': root + '/schema',
    'config': root + '/conf',
    'tests': root + '/tests',
    'utils': root + '/utils',
}

hosts = {
    'default': 'https://hacker-news.firebaseio.com',
    'staging': '',
}

endpoints = {
    'top_stories': '/v0/topstories.json',
    'items': '/v0/item/{}.json',
}
