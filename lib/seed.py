

class SeedUtils:
    """
    SeedUtils
    """

    def read(self, file):
        """ read """
        datas = []
        with open(file) as f:
            for line in f:
                datas.append(eval(line.strip()))
        return datas
        