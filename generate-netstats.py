#!/usr/bin/env python3

import os,sys
import glob
import pandas as pd
import pybrainlife.data.manipulate as blmanip
import jgf
import igraph
import json

def build_network_df(path,subjectID,sessionID):

    df = pd.DataFrame()
    igraphs = []

    tmp = jgf.igraph.load(path,compressed=True)
    igraphs = igraphs + [tmp[0]]
    
    df['subjectID'] = [ subjectID for f in range(len(igraphs)) ]
    df['sessionID'] = [ sessionID for f in range(len(igraphs)) ]
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

    if not os.path.isdir('net-stats'):
        os.mkdir('net-stats')
        os.mkdir('net-stats/net-stats')

    networks_df = build_network_df(network,subjectID,sessionID)

    conmats, global_measures, local_measures = blmanip.parse_networks(networks_df)

    global_measures = global_measures.reset_index(drop=True)

    local_measures = local_measures.reset_index(drop=True)

    conmats.to_csv('./net-stats/net-stats/conmats.csv')
    global_measures.to_csv('./net-stats/net-stats/global_measures.csv',index=False)
    local_measures.to_csv('./net-stats/net-stats/local_measures.csv',index=False)

if __name__ == "__main__":
    main()
