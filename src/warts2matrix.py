#!/usr/bin/python
import sys
import os
import traceback
import subprocess
import json
from pprint import PrettyPrinter

def readWarts(fileName):
    try:
        lines = subprocess.check_output(["sc_warts2json", fileName], universal_newlines=True)
        jsonData = json.loads(lines)
        return jsonData
    except:
        traceback.print_exc()

def updateDict(jsonData):
    for entry in jsonData:
        src = entry['src']
        dst = entry['dst']
        if src not in dataDict.keys():
            dataDict[src]={}
        if dst not in dataDict[src].keys():
            dataDict[src][dst]=set()

        for hop in entry['hops']:
            hopIP = hop['addr']
            dataDict[src][dst].add(hopIP)

if __name__=="__main__":
    pp=PrettyPrinter()
    dataDict={}
    jData=readWarts(sys.argv[1])
    updateDict(jData)
    pp.pprint(jData)
