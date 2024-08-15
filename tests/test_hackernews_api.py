import asyncio

from conf import config, constants
from libraries.core import Core
from libraries.helpers import Helpers

core = Core()
helpers = Helpers()


class TestHackernewsAPI:

    def test_top_stories_api(self):
        top_stories_url = config.hosts['default'] + config.endpoints['top_stories']
        top_stories_response = core.make_request_and_get_response(constants.GET_REQUEST, top_stories_url)
        core.verify_200_ok_response_code(top_stories_response.status_code, top_stories_url)
        core.validate_json_schema(top_stories_response.json(), 'top_stories.json')

    def test_get_current_top_story(self):
        top_stories_url = config.hosts['default'] + config.endpoints['top_stories']
        items_url = config.hosts['default'] + config.endpoints['items']
        top_stories_response = core.make_request_and_get_response(constants.GET_REQUEST, top_stories_url)
        top_stories = top_stories_response.json()
        current_top_story = asyncio.run(helpers.get_current_top_story_from_items(top_stories, items_url))
        core.validate_json_schema(current_top_story, 'current_top_story.json')

    def test_get_first_comment(self):
        top_stories_url = config.hosts['default'] + config.endpoints['top_stories']
        items_url = config.hosts['default'] + config.endpoints['items']
        top_stories_response = core.make_request_and_get_response(constants.GET_REQUEST, top_stories_url)
        top_stories = top_stories_response.json()
        first_comment = asyncio.run(helpers.get_comment_from_items(top_stories, items_url, comment_number=1))
        core.validate_json_schema(first_comment, 'comment.json')