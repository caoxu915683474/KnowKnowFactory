import yaml


class YamlUtils:
    """
    YamlUtils
    """

    def read(self, file):
        """ read """
        with open(file, "r", encoding="utf-8") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        return config
        