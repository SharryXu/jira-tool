from jira_tool.priority import Priority
from jira_tool.story import *


class TestStory:
    def test_compare_story(self):
        storyFactory = StoryFactory(
            [
                (1, "regulatory", Priority, False, False, 5),
                (2, "partnerPriority", Priority, False, True, 4),
                (3, "productValue", Priority, False, True, 3),
                (4, "marketingUrgency", Priority, False, True, 2),
                (5, "revenue", Priority, False, True, 1),
            ]
        )

        s1 = storyFactory.create_story()
        s1["regulatory"] = Priority.NA
        s1["partnerPriority"] = Priority.MIDDLE
        s1["productValue"] = Priority.MIDDLE
        s1["marketingUrgency"] = Priority.NA
        s2 = storyFactory.create_story()
        s2["regulatory"] = Priority.NA
        s2["partnerPriority"] = Priority.LOW
        s2["productValue"] = Priority.HIGH
        s2["marketingUrgency"] = Priority.NA
        s3 = storyFactory.create_story()
        s3["regulatory"] = Priority.NA
        s3["partnerPriority"] = Priority.MIDDLE
        s3["productValue"] = Priority.HIGH
        s3["marketingUrgency"] = Priority.NA

        assert s1 > s2
        assert s1 < s3
        assert s2 < s3

    def test_sort_stories(self):
        storyFactory = StoryFactory(
            [
                (1, "regulatory", Priority, False, False, 5),
                (2, "partnerPriority", Priority, False, True, 4),
                (3, "productValue", Priority, False, True, 3),
                (4, "marketingUrgency", Priority, False, True, 2),
                (5, "revenue", Priority, False, True, 1),
            ]
        )

        stories = [
            storyFactory.create_story(),
            storyFactory.create_story(),
        ]

        stories = sorted(stories, reverse=True)

        for i in range(len(stories) - 1):
            assert stories[i] <= stories[i + 1]
