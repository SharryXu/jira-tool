from datetime import datetime

from jira_tool.story import *


class TestStory:
    def test_compare_story(self):
        storyFactory = StoryFactory(
            [
                (1, "name", str, False, False, 1),
                (2, "age", int, False, True, 2),
                (3, "tel", str, False, True, 3),
                (4, "dob", datetime, False, True, 4),
            ]
        )

        s1 = storyFactory.create_story()
        s2 = storyFactory.create_story()

        assert s1 == s2

        s3 = storyFactory.create_story()
        s3["age"] = 30

        assert s3 > s2
