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

    # NA, Middle, Middle, NA
    s1 = storyFactory.create_story()
    s1["regulatory"] = Priority.NA
    s1["partnerPriority"] = Priority.MIDDLE
    s1["productValue"] = Priority.MIDDLE
    s1["marketingUrgency"] = Priority.NA
    # NA, Low, High, NA
    s2 = storyFactory.create_story()
    s2["regulatory"] = Priority.NA
    s2["partnerPriority"] = Priority.LOW
    s2["productValue"] = Priority.HIGH
    s2["marketingUrgency"] = Priority.NA
    # NA, Middle, High, NA
    s3 = storyFactory.create_story()
    s3["regulatory"] = Priority.NA
    s3["partnerPriority"] = Priority.MIDDLE
    s3["productValue"] = Priority.HIGH
    s3["marketingUrgency"] = Priority.NA
    # NA, High, High, NA
    s4 = storyFactory.create_story()
    s4["regulatory"] = Priority.NA
    s4["partnerPriority"] = Priority.HIGH
    s4["productValue"] = Priority.HIGH
    s4["marketingUrgency"] = Priority.NA
    # High, NA, High, NA
    s5 = storyFactory.create_story()
    s5["regulatory"] = Priority.HIGH
    s5["partnerPriority"] = Priority.NA
    s5["productValue"] = Priority.HIGH
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
