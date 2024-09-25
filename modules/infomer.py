import sys
from dataclasses import dataclass

cur_dir = os.path.abspath(os.path.dirname(__file__))

sys.path.append(cur_dir + "/../templates/")
from template import TEMPLATES


@dataclass
class Informer:
    """ 
    Informer
    """
    template_id: int 
    fewshot_num: int
    generate_num: int
    retry: bool

    def get_info(self):
        """ get_info """
        





