import json
import requests
import os
import tarfile

datasources = "datasources.json"

with open(datasources) as sources:
    downloads = json.load(sources)
    
    for line in downloads['data_source']:
        if line['download']:
            filename = line['url'].split('/')[-1]
            print("Downloading {}...".format(line['url']))
            r = requests.get(line['url'], allow_redirects=True)
            open('data/'+filename, 'wb').write(r.content)

            os.chdir('data/')
            tf = tarfile.open(filename)
            tf.extractall()

            os.remove(filename)