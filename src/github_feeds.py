"""
Module to parse event organisers github atom feeds, to maybe get a sneaky hint
of an event coming up :)
"""
import requests
import yaml

from utils import isodate


class GithubFeeds:
    """
    Class for dealing with the github feeds.
    """
    def __init__(self, token, data, go_back):
        """
        Our constructor, really doesn't do anything but read in the github urls
        """
        self.token = token
        self.data = GithubFeeds.get_locations(data)
        self.go_back = go_back

    def update(self):
        """
        Iterates through the list of feeds provided, checking when they were
        last updated.
        """
        data = {}
        for item in self.data:
            feed_url = "https://api.github.com/users/%s/events" % item['name']
            (recently_updated, _) = self.feed(
                feed_url, changed_after=self.go_back)

            data[item['organisation']] = recently_updated
      
        return data

    @staticmethod
    def get_locations(path):
        """
        Just reads in the yaml object listing github urls.
        """
        return yaml.load(open(path), Loader=yaml.Loader)['githubs']

    def feed(self, feed_url, changed_after):
        """
        Our tool to read the feeds.
        """
        print("checking %s" % feed_url)
        res = False
        r = requests.get(
            feed_url,
            headers={
                'Authorization': 'token %s' % self.token
            }
        )
        fp = r.json()
        if len(fp) > 0:
            last_changed = isodate(fp[0]['created_at'])
            res = last_changed > changed_after

        return (res, fp)
        
