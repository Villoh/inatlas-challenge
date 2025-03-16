# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

class RotateUserAgentMiddleware:
    """Rotates User-Agent headers to avoid being blocked by websites."""
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        """Returns an instance of RotateUserAgentMiddleware."""
        settings = crawler.settings
        user_agents = settings.get('ROTATE_USER_AGENTS', [])
        return cls(user_agents=user_agents)

    def process_request(self, request, spider):
        """
        Sets the User-Agent header for each request to a randomly selected User-Agent string from the `user_agents` list.
        
        :param request: Scrapy Request object
        :param spider: Scrapy Spider object
        """
        request.headers['User-Agent'] = random.choice(self.user_agents)