import os
import sys

cur_dir = os.path.abspath(os.path.dirname(__file__))

sys.path.append(cur_dir + "/../lib/")
from yaml import YamlUtils
from matiral import MatrialBase
from infomer import Informer
from predicter import Predicter
from checker import Checker
from saver import Saver


class Controller:
    """
    Controller
    """
    CONF = "control.yaml"

    def __init__(self):
        """ __init__ """
        self.__setup()

    def __setup(self):
        """ setup """
        self.__set_utils()
        self.__set_conf()
        self.__set_matrial_base()
        self.__set_pipline()
    
    def __set_utils(self):
        """ set_utils """
        self.yaml_utils = YamlUtils()
    
    def __set_conf(self):
        """ set_conf """
        self.conf = self.yaml_utils.read(cur_dir + "/../conf/" + CONF)
    
    def __set_matrial_base(self):
        """ set_matrial_base """
        self.matrial_base = MatrialBase()
    
    def __set_pipline():
        """ set_pipline """
        pipline = self.yaml_utils.read(self.conf["pipline"])
        steps = []
        for step in self.pipline:
            name = step["name"]
            template_id = step["template_id"]
            fewshot_num = step["fewshot_num"]
            generate_num = step["generate_num"]
            retry = step["retry"]
            informer = Informer(template_id, fewshot_num, generate_num, retry)
            predicter = Predicter(mode)
            checker = Checker(filter)
            saver = Saver(outfile)
            steps.append({"informer": informer, "predicter": predicter, "checker": checker, "saver": saver})
        self.steps = steps

    def __run_pipline(self, matrial):
        """ run_pipline """
        for step in self.steps:
            informer = step["informer"]
            predicter = step["predicter"]
            checker = step["checker"]
            saver = step["saver"]
            infos = informer.get_info(matrial)
            for info in infos:
                response = predicter.predict(info)
                response = checker.check(response)
                saver.save(response)
    
    def start(self):
        """ start """
        while True:
            matrial = self.matrial_base.get_matrial()
            if not matrial: break
            self.__run_pipline(matrial)