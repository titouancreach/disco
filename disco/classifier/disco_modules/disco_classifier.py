#
# CNET - Content Solution
#
# Disco classifier
#
# Module name : disco_classifier
#
# Titouan CREACH
#
# titouan.creach@gmail.com
# titouan.creach@cbsi.com
#

import numpy
from sklearn import svm

class disco_classifier:
    """
    Encapsule any type of classifiers

    this class implement any usefuls informations like the number of tests or
    the number of datas

    """
    def __init__(self, classifier, name):
        """
        classifier is an instance of any kind of classifier, could be loaded
        directly from a file or generated from disco_init

        name is the name of the classifier, it's very useful for statistics
        """
        self._nbr_test = 0
        self._nbr_data = 0
        self._answer = []
        self._data = []
        self._clf = None
        self._name = ''

        self._clf = classifier
        self._name = name

    def predict(self, data):
        """
        data is a vector of scores fetched from the java web service
        """
        return self._clf.predict(data)[0]

    def add_data(self, adata, aanswer):
        """
        adata is a vector of scores
        aanswer is a boolean, in order to learn the classifiers
        """
        self._answer.append(aanswer)
        self._data.append(adata)
        self._nbr_data += 1

    def learn(self):
        """
        Make a classifier from this datas and answers
        """
        self._clf.fit(self._data, self._answer)
        self._nbr_test += 1

    def get_name(self):
        """
        Return the name of the classifiers
        """
        return self._name

    def set_classifier(self, clf):
        """
        Change the classifier
        """
        self._clf = clf

    def reset(self):
        """
        Reset the classifier from scratch
        """
        self._nbr_test = 0
        self._nbr_test = 0
        self._nbr_data = 0
        self._answer = []
        self._data = []
        self._clf = None

    def get_info(self):
        """
        return classifier informations
        """
        return [self._nbr_test]

