#
# CNET - Content Solution
#
# Disco classifier
#
# Module name : disco_classifiers
#
# Titouan CREACH
#
# titouan.creach@gmail.com
# titouan.creach@cbsi.com
#

import pickle

class disco_classifiers(list):
    """
    List of disco_classifier, use to stock different kind of classifier
    inherit from python's list
    """
    def __init__(self, *args):
        list.__init__(self, *args)

    def save_in_file(self, path):
        """
        Write classifiers in a file defined by path (String)
        classifiers are dumped by pickle
        """
        with open(path, 'wb') as f:
            pick = pickle.Pickler(f)
            pick.dump(self)

    def load_from_file(self, path):
        """
        Load classifier from a path
        """
        with open(path, 'rb') as f:
            pick = pickle.Unpickler(f)
            for i in pick.load():
                self.append(i)


