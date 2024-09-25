import os
import sys

cur_dir = os.path.abspath(os.path.dirname(__file__))

sys.path.append(cur_dir + "/../lib/")
from yaml import YamlUtils
from seed import SeedUtils


class TemplateFactory:
    """ 
    TemplateFactory
    """
    CONF = "template.yaml"

    def __init__(self):
        """ __init__ """
        self.__setup()
    
    def __setup(self):
        """ setup """
        self.__set_utils()
        self.__set_conf()
    
    def __set_utils(self):
        """ set_utils """
        self.yaml_utils = YamlUtils()
        self.seed_utils = SeedUtils()

    def __set_conf(self):
        """ set_conf """
        self.conf = self.yaml_utils.read(cur_dir + "/../conf/" + CONF)
    
    def __set_seeds(self):
        """ set_seed """
        seeds = {}
        for seed in self.conf["seeds"]:
            seeds[seed["name"]] = self.seed_utils.read(seed["file"])
        self.seeds = seeds

    def get_fewshots(self, type, num=None):
        """ get_fewshots """
        fewshots = random.sample(self.seeds[type], num)
        method = getattr(self, type)
        prompt = method(fewshots)
        return prompt

    def select(self, fewshots):
        """ select """
        prompt = ""
        for index, fewshot in enumerate(fewshots):
            prefix = f"###例{index+1}###"
            question_type = "题型: " + fewshot["question_type"]
            exam_subject = "科室: " + fewshot["exam_subject"]
            question = "问题: " + fewshot["question"]
            options = []
            for s, v in fewshot["option"].items():
                if len(v) == 0: continue
                options += [s + "." + v]
            options = "选项: " + str(options)
            answer = "答案: " + fewshot["answer"]
            stop  = "[END]"
            prompt += prefix + "\n"
            prompt += question_type + "\n"
            prompt += exam_subject + "\n"
            prompt += question + "\n"
            prompt += options + "\n"
            prompt += answer + "\n"
            prompt += stop + "\n"
        return prompt

    def know(self, num):
        """ know """
        pass
    
    def corpus(self):
        """ corpus """
        pass

    
    def sft(self):
        """ sft """
        pass

TEMPLATES = TemplateFactory()