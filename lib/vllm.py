import os
import sys

cur_dir = os.path.abspath(os.path.dirname(__file__))

from yaml import YamlUtils


class VllmHelper:
    """ 
    VllmHelper 
    """
    CONF = "vllm.yaml"

    def __init__(self):
        """ __init__ """
        self.__setup()

    def __setup(self):
        """ setup """
        self.__set_utils()
        self.__set_conf()
        self.__set_client()
    
    def __set_utils(self):
        """ set_"""
        self.yaml_utils = YamlUtils()

    def __set_conf(self):
        """ set_conf """
        self.conf = self.yaml_utils.read(cur_dir + "/../conf/" + CONF)
    
    def __set_client(self):
        """ set_client """
        self.client = OpenAI(api_key=self.conf["api_key"], base_url=self.conf["base_url"])
    
    def call_prompt(self, prompt):
        """ call_prompt """
        response = client.completions.create(model=self.conf["model_name"],
                                             prompt=prompt,
                                             max_tokens=self.conf["max_tokens"],
                                             temperature=self.conf["temperature"],
                                             stop=self.conf["stop"]).choices[0].text.strip()
        return response
    
    def call_intruction(self, instruction):
        """ call_intruction """
        messages = [{"role": "system", "content": self.conf["system"]}, {"role": "user", "content": instruction}]
        response = client.chat.completions.create(model=self.conf["model_name"],
                                                  messages=messages,
                                                  temperature=self.conf["temperature"]).choices[0].message.content
        return response

