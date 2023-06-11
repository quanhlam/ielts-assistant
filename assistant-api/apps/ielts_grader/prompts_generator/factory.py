from apps.ielts_grader.prompts_generator.writing import IeltsWritingGrader


class PromptGeneratorFactory:
    def __init__(self, task_name):
        self.task_name = task_name

    def create_generator(self):
        if self.task_name == "ielts_writing_grader":
            return IeltsWritingGrader()

        raise Exception("Invalid task for prompt factory")