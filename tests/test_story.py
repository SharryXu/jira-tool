from jira_tool.priority import Priority
from jira_tool.story import *


def mock_data() -> list:
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
    # 1
    s1["regulatory"] = Priority.NA
    # 2
    s1["partnerPriority"] = Priority.MIDDLE
    # 3
    s1["productValue"] = Priority.MIDDLE
    # 4
    s1["marketingUrgency"] = Priority.NA
    s2 = storyFactory.create_story()
    # 1
    s2["regulatory"] = Priority.NA
    # 2
    s2["partnerPriority"] = Priority.LOW
    # 3
    s2["productValue"] = Priority.HIGH
    # 4
    s2["marketingUrgency"] = Priority.NA
    s3 = storyFactory.create_story()
    # 1
    s3["regulatory"] = Priority.NA
    # 2
    s3["partnerPriority"] = Priority.MIDDLE
    # 3
    s3["productValue"] = Priority.HIGH
    # 4
    s3["marketingUrgency"] = Priority.NA
    s4 = storyFactory.create_story()
    # 1
    s4["regulatory"] = Priority.NA
    # 2
    s4["partnerPriority"] = Priority.HIGH
    # 3
    s4["productValue"] = Priority.HIGH
    # 4
    s4["marketingUrgency"] = Priority.NA
    s5 = storyFactory.create_story()
    # 1
    s5["regulatory"] = Priority.HIGH
    # 2
    s5["partnerPriority"] = Priority.NA
    # 3
    s5["productValue"] = Priority.HIGH
    # 4
    s5["marketingUrgency"] = Priority.NA

    return [s1, s2, s3, s4, s5]


class TestStory:
    def test_compare_story(self):
        data = mock_data()
        s1 = data[0]
        s2 = data[1]
        s3 = data[2]
        s4 = data[3]
        s5 = data[4]
        assert s1 < s2
        assert s1 < s3
        assert s2 < s3
        assert s4 > s5

    def test_sort_stories(self):
        data = mock_data()

        stories = sorted(data, reverse=False)

        for i in range(len(stories) - 1):
            assert stories[i] <= stories[i + 1]
