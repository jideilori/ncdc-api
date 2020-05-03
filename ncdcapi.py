from flask_restful import Resource, request
import requests
import json
from lxml import html

url = "https://covid19.ncdc.gov.ng/"

class ncdc(Resource):
    def get(self):
        try:
            global response 
            response = requests.get(url)
        except:
            return {"message": "could not reach server.Please try again later"}
        if response.status_code ==200:
            return {"states":self.states_cases(),"summary": self.total_cases()}
        else:
            return {"message": "could not reach server. Please try again ..."}

    def total_cases(self):
        tree = html.fromstring(response.text)
        summary = {}
        for i in range(5):
            cases = tree.cssselect('h6.text-white')
            result = tree.cssselect('h2 span')
            summary.update({cases[i].text: result[i].text})
        return summary

    def states_cases(self):
        tree = html.fromstring(response.text)
        states_summary = {}
        for i in range(len(tree.cssselect('td:nth-child(1)'))):
            states = tree.cssselect('td:nth-child(1)')[i].text.strip()
            confirmed = tree.cssselect('td:nth-child(2)')[i].text.strip()
            discharged = tree.cssselect('td:nth-child(4)')[i].text.strip()
            deaths = tree.cssselect('td:nth-child(5)')[i].text.strip()
            states_summary.update( {states: [ {'confirmed':confirmed,"discharged": discharged,"deaths": deaths}]})
        return states_summary

    

#   def put(self, id):
