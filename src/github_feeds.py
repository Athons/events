"""
Module to parse event organisers github atom feeds, to maybe get a sneaky hint
of an event coming up :)
"""
import feedparser
import yaml


class GithubFeeds:
    """
    Class for dealing with the github feeds.
    """
    def __init__(self, data, go_back):
        """
        Our constructor, really doesn't do anything but read in the github urls
        """
        self.data = GithubFeeds.get_locations(data)
        self.go_back = go_back

    def update(self):
        """
        Iterates through the list of feeds provided, checking when they were
        last updated.
        """
        data = {}
        for item in self.data:
            feed_url = "%s.atom" % item['url']
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

    @staticmethod
    def feed(feed_url, changed_after):
        """
        Our tool to read the feeds.
        """
        fp = feedparser.parse(feed_url)
        last_changed = fp['feed']['updated_parsed']
        print(last_changed)
        return (last_changed > changed_after, fp)
