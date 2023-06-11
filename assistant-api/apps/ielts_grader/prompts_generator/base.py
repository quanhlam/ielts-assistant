import re
import logging

class BaseAdapter:
    REQUEST = """
    Given ielts question task "{task_number}", question is: "{question}".
    This is my writing: "{writing_answer}" 
    Give scores and review base on the following criteria, formatted as:
    {criteria_template}.
    For each criteria, give at least 50 words explain in details the writer's strength and weakness, point out specifically in the paragraph.
    """

    SEGMENTS = []

    def  __init__(self, model):
        self.model = model

    def parse(self, response):
        res = {}

        for i, seg in enumerate(self.SEGMENTS):
            pattern = r"{cate}:[ \r\n]*(.*?)$" if i == len(self.SEGMENTS) - 1 else r"{cate}:[ \r\n]*(.*?)\n"
            try:
                key = seg.lower().strip().replace(" ", "_")
                value = re.search(pattern.format(cate=seg), response, re.DOTALL).group(1)
                res.update({key: value})
            except Exception as e:
                logging.error(f"Error parsing {seg}. {e}")

        return res

    def generate_question(self, task_number, question, writing_answer, answer_data_type="paragraph"):
        lst_answer_template = []
        for seg in self.SEGMENTS:
            if seg == "Overall Score":
                lst_answer_template.append(f"{seg}:<number>;")
            else:
                lst_answer_template.append(f"{seg}:<{answer_data_type}>;")

        return self.REQUEST.format(task_number=task_number,
                                   question=question,
                                   writing_answer=writing_answer,
                                   criteria_template="\n".join(lst_answer_template))

    def get_prompt(self, task_number, question, writing_answer):
        question = self.generate_question(task_number, question, writing_answer)
        logging.info(f"Question: {repr(question)}")
        messages = [
            {"role": "system", "content": "You are a helpful ielts assistant"},
            {"role": "user", "content": question},
        ]
        return messages