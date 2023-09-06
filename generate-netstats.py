#!/usr/bin/env python3

import os,sys
import glob
import pandas as pd
import pybrainlife.data.manipulate as blmanip
import jgf
import igraph
import json

def build_network_df(path,subjectID,sessionID,tags,datatype_tags):

    df = pd.DataFrame()
    igraphs = []

    tmp = jgf.igraph.load(path,compressed=True)
    igraphs = igraphs + [tmp[0]]
    
    df['subjectID'] = [ subjectID for f in range(len(igraphs)) ]
    df['sessionID'] = [ sessionID for f in range(len(igraphs)) ]
    df['tags'] = [ tags for f in range(len(igraphs)) ]
    df['datatype_tags'] = [ tags for f in range(len(igraphs)) ]
    df['igraph'] = igraphs

    return df

def main():

    with open('config.json') as config_f:
        config = json.load(config_f)

    network = config['network']
    subjectID = config['_inputs'][0]['meta']['subject']

    if 'session' in config['_inputs'][0]['meta'].keys():
        sessionID = config['_inputs'][0]['meta']['session']
    else:
        sessionID = '1'

    if 'tags' in config['_inputs'][0]['meta'].keys():
        tags = config['_inputs'][0]['meta']['tags']
    else:
        tags = ['tmp']

    if 'datatype_tags' in config['_inputs'][0]['meta'].keys():
        datatype_tags = config['_inputs'][0]['meta']['datatype_tags']
    else:
        datatype_tags = ['tmp']

    if not os.path.isdir('net-stats'):
        os.mkdir('net-stats')
        os.mkdir('net-stats/net-stats')

    network_df = build_network_df(network,subjectID,sessionID,tags,datatype_tags)

    i=0
    conmats = blmanip.build_temporary_network_dataframe(network_df.iloc[i]['igraph'],'connectivity',network_df.iloc[i]['subjectID'],network_df.iloc[i]['sessionID'],network_df.iloc[i]['tags'],network_df.iloc[i]['datatype_tags'])

    conmats = conmats.drop(columns=['tags','datatype_tags'])

    conmats.to_csv('./net-stats/net-stats/conmats.csv')

if __name__ == "__main__":
    main()
