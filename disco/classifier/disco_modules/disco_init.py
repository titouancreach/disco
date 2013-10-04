
#
# CNET - Content Solution
#
# Disco classifier
#
# Module name : disco_init
#
# Titouan CREACH
#
# titouan.creach@gmail.com
# titouan.creach@cbsi.com
#

import json
import sys

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.lda import LDA
from sklearn.qda import QDA
from sklearn.neighbors import KNeighborsClassifier

from disco_classifiers import *
from disco_classifier import *


def init_classifier():
    """
    Return a list of differents classifiers from sklearn
    """
    list_classifier = disco_classifiers([])

    clf = SVC(kernel='linear', C=0.025)
    list_classifier.append(disco_classifier(clf, 'SVM linear'))

    clf = SVC(gamma=2, C=1)
    list_classifier.append(disco_classifier(clf, 'SVC SVM'))

    clf = DecisionTreeClassifier(max_depth=5)
    list_classifier.append(disco_classifier(clf, 'Decision Tree'))

    clf = AdaBoostClassifier()
    list_classifier.append(disco_classifier(clf, 'AdaBoost'))

    clf = GaussianNB()
    list_classifier.append(disco_classifier(clf, 'Naive Bayes'))

    return list_classifier
