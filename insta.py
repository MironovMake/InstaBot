from instapy import InstaPy
from instapy import smart_run
import tg
session = InstaPy(username="mag._aleks",
                  password="6r5hreno464")
session.login()

session.set_relationship_bounds(enabled=True, max_followers=300)
session.set_do_follow(True, percentage=100)
session.set_dont_like(["nsfw","18+"])
session.like_by_tags(["физика","physic","ньютон","newton"], amount=30)

session.end()

