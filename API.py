# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 17:31:10 2017

@author: VICTOR
"""

import json

from pprint import pprint
from octopus import Octopus


def request(urls):
    data = []
    
    otto = Octopus(
            concurrency = 4, auto_start = True, cache = True, expiration_in_seconds=10
            )
    def handle_url_response(url, response):
        if "Not found" == response.text:
            print("URL Not Found: %s" %url)
        else:
            data.append(response.text)
            
    for url in urls:
        otto.enqueue(url, handle_url_response)
    otto.wait()
    
    json_data = json.JSONEncoder(indent = None,
                                 separators = (',', ':')).encode(data)
    return pprint(json_data)

print (create_request(['https://en.wikipedia.org/w/api.php']))
