import re
import logging

class BaseAdapter:
    REQUEST = """
    Given business statement "{statement}". Generate a {model} model, with answer formatted as:
    {answer_template}
    """

    SEGMENTS = []

    def  __init__(self, model):
        self.model = model

    def parse(self, response):
        res = {}

        for i, seg in enumerate(self.SEGMENTS):
            pattern = r"{cate}:[ \r\n]*(.*?)$" if i == len(self.SEGMENTS) - 1 else r"{cate}:[ \r\n]*(.*?)\n"
            try:
                key = seg.lower()
                value = re.search(pattern.format(cate=seg), response, re.DOTALL).group(1)
                res.update({key: value})
            except Exception as e:
                logging.error(f"Error parsing {seg}. {e}")

        return res

    def generate_question(self, business_statement, answer_data_type="paragraph"):
        lst_answer_template = []
        for seg in self.SEGMENTS:
            lst_answer_template.append(f"{seg}:<{answer_data_type}>;")

        return self.REQUEST.format(statement=business_statement, model=self.model, answer_template="\n".join(lst_answer_template))


    def get_prompt(self, business_statement):
        question = self.generate_question(business_statement)
        logging.info(f"Question: {repr(question)}")
        messages = [
            {"role": "system", "content": "You are a helpful business analyst"},
            {"role": "user", "content": question},
        ]
        return messages