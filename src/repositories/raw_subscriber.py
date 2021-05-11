
import dataclasses
import json
import logging
import os
import requests

# An endpoint that handles unprocessed JSON forwarded from notifications.
class RawSubscriber:
    def __init__(self, url_endpoint):
        self._url_endpoint = url_endpoint

    def post_commit_status(self, commit_status):
        json_data = dataclasses.asdict(commit_status[1])
        logging.debug("Sending raw json to subscriber: " + json.dumps(json_data))
        response = requests.post(url=self._url_endpoint, json=json_data)

class RawSubscriberFactory:
    @staticmethod
    def new_raw_subscribers() -> list[RawSubscriber]:
        # TODO(tcare): Dynamically pick up subscribers via CRD or similar
        # Currently we only have one subscriber
        subscribers = []
        subscriber = RawSubscriber(os.getenv("SPEKTATE_ENDPOINT"))
        subscribers.append(subscriber)

        return subscribers
