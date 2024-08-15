import asyncio
import ssl

import aiohttp
import certifi

from conf import constants
from libraries.core import Core


class Helpers(Core):

    def __init__(self):
        super().__init__()

    async def get_all_top_stories(self, session, url):
        sslcontext = ssl.create_default_context(cafile=certifi.where())
        async with session.get(url, ssl=sslcontext) as res:
            self.verify_200_ok_response_code(res.status, url)
            return await res.json()

    async def get_current_top_story_from_items(self, items, base_url):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for item in items:
                url = base_url.format(item)
                tasks.append(self.get_all_top_stories(session, url))
            responses = await asyncio.gather(*tasks)
        stories = []
        for response in responses:
            if 'type' in response.keys() and response['type'] == 'story':
                stories.append(response)
        sorted_top_stories = sorted(stories, key=lambda x: x['time'], reverse=True)
        return sorted_top_stories[0]

    async def parse_item_for_comment(self, session, url, comment_number):
        sslcontext = ssl.create_default_context(cafile=certifi.where())
        async with session.get(url, ssl=sslcontext) as res:
            response = await res.json()
            self.verify_200_ok_response_code(res.status, url)
            if 'type' in response.keys() and 'kids' in response.keys() and response['kids'] and response['type'] == 'story':
                first_comment_item_id = response['kids'][comment_number - 1]
                return first_comment_item_id

    async def get_comment_from_items(self, items, items_url, comment_number):
        """
        This method can be reused to get any comment based on the comment_number provided
        :param items: these are the top stories
        :param items_url: url with items endpoint
        :param comment_number: 1 for first comment, 2 for 2nd comment and so on.
        Caution: This value should be known ahead of time to avoid causing IndexError exception
        :return: The comment text based on comment_number
        """
        async with aiohttp.ClientSession() as session:
            tasks = []
            for item in items:
                url = items_url.format(item)
                tasks.append(self.parse_item_for_comment(session, url, comment_number))
                if tasks:
                    break
            first_comment_item_id = await asyncio.gather(*tasks)
        for item_id in first_comment_item_id:
            comment_response = self.make_request_and_get_response(constants.GET_REQUEST, items_url.format(item_id))
            self.verify_200_ok_response_code(comment_response.status_code, items_url.format(item_id))
            return comment_response.json()['text']
