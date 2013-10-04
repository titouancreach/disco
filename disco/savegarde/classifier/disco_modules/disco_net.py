#
# CNET - Content Solution
#
# Disco classifier
#
# Module name : disco_net
#
# Titouan CREACH
#
# titouan.creach@gmail.com
# titouan.creach@cbsi.com
#

from flask import Flask, request, session
from flask.ext.classy import FlaskView, route

import json

from disco_classifiers import *
from disco_classifier import *
from disco_init import *
from disco_const import *
from disco_decorator import *

import os.path

g_list_of_classifier = disco_classifiers([])

class   disco_net(FlaskView):
    """
    disco_net is the main module, implement the web service
    url_base : http://server/classifier/'action'
    for action, please read the following
    """
    route_base = '/classifier/'

    #-------------------------------------------------------------------------
    @route('/predict', methods=['PUT'])
    def do_predict(self):
        """
        Make a prediction for sets of scores
        """
        answer = []
        response = []

        for it_predictions in json.loads(request.data.decode('UTF-8')):
            prediction = it_predictions['score']
            for ite_clf in g_list_of_classifier:
                    answer.append(ite_clf.predict(prediction))
            if answer.count(True) > answer.count(False):
                    response.append({'answer' : True})
            else:
                    response.append({'answer' : False})
        return json.dumps(response, indent=4)
    #-------------------------------------------------------------------------
    @staticmethod
    def _reset():
        """
        private function for reset the disco_net from scratch
        """
        global g_list_of_classifier
        global g_state

        g_state = False
        g_list_of_classifier = disco_classifiers([])

    #-------------------------------------------------------------------------
    @route('/learn', methods=['PUT'])
    def do_training(self):
        """
        function for send datas sets to classifiers
        usr : urlbase/learn
        method : PUT

        body must be like the following :
        [
            {
                'score'  : [0.1, 0.5, 0.8 ... ],
                'answer' : true
            },
            ...
        ]

        """
        json_data = request.data
        global g_list_of_classifier

        datas = json.loads(json_data.decode('UTF-8')) #datas = liste

        for ite_clf in g_list_of_classifier:
            for data in datas:
                ite_clf.add_data(data['score'], data['answer'])
            print(ite_clf.get_info())
        return ''

    #-------------------------------------------------------------------------
    @route('/make', methods=['POST'])
    def do_make_(self):
        """
            this function make classifier,
            to use when datas sets are already defined,
            becareful when you use it, performances are very slow

            url : urlbase/make
            method : POST
        """
        global g_list_of_classifier

        for ite_clf in g_list_of_classifier:
            ite_clf.learn()
        return ''

    #-------------------------------------------------------------------------
    @route('/load', methods=['PUT'])
    def do_load(self):
        """
        Load function load list of classifiers from a file or init new a new
        one if the file doesn't exist.

        url : urlbase/load
        the body must contain and id defined like that:

            {
                'id' : 1
            }

        this function RESET actuals classifiers, be careful to save before
        load if an other classifier is in use
        """
        global g_state
        global g_list_of_classifier

        id_client = json.loads(request.data.decode('UTF-8'))['id']
        self._reset()
        if os.path.exists(CLASSIFIER_PATH + str(id_client) + '.cls'):
            g_list_of_classifier.load_from_file(CLASSIFIER_PATH  + 
                str(id_client) + '.cls')
        else:
            g_list_of_classifier = init_classifier()
        return ''

    @route('/reset', methods=['PUT'])
    def do_reset(self):
        _reset()

    #-------------------------------------------------------------------------
    @route('/save', methods=['PUT'])
    def do_save(self):
        """
        Save function save dump classifiers into a file
        url : urlbase/save

        body request must have an client id. Watch for "Load" for any else
        informations

        """
        id_client = json.loads(request.data.decode('UTF-7'))['id']
        g_list_of_classifier.save_in_file(CLASSIFIER_PATH + str(id_client) + 
            '.cls')
        return ''
    #-------------------------------------------------------------------------
