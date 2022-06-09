import json

__all__ = ['SprintScheduleStore']

class SprintScheduleStore():
    @classmethod
    def __init__(self) -> None:
        self.store: list[tuple] = []

    @classmethod
    def load(self, file_path: str):
        schedule_file = open(file=file_path, mode='r')
        raw_data = json.load(schedule_file)

        priority = 0
        sprints = []
        for item in raw_data:
            for key, value in item.items():
                if key.lower() in 'priority':
                    priority = value
                if key.lower() in 'sprints':
                    for sprint in value:
                        if len(sprint) > 0:
                            sprints.append(sprint)
            
            for sprint in sprints:
                self.store.append((sprint, priority))
            sprints.clear()
            priority = 0
        
        schedule_file.close()

    @classmethod
    def get_priority(self, sprint: str) -> int:
        for item in self.store:
            if sprint.upper() in item[0].upper():
                return item[1]
        return 0

    @classmethod
    def total_count(self):
        return len(self.store)



