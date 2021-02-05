#!/usr/bin/env python3
"""
Our __main__ module.
"""
from jinja2 import Template

import config
from github_feeds import GithubFeeds
from notify import Notify
from utils import changed_after_days

bot_message = """(bot message)

The following event organisers have updated their github organisations this
week:

{% for org in data %}* {{ org }}\n{% endfor %}
"""

def main(datapath):
    """
    Just a generic entrypoint for testing.
    """
    notify = Notify(config.gitter_token, config.gitter_community)
    go_back = changed_after_days()

    ghf = GithubFeeds(datapath + '/github.yml', go_back)

    updates = ghf.update()
    results = []
    for org in updates.keys():
        if updates[org]:
            results.append(org)

    if len(results) > 0:
        message_template = Template(bot_message)
        message = message_template.render(data=results)
        print(message)
        #notify.send(config.gitter_channel, message)


if __name__ == "__main__":
    main('./sources')
