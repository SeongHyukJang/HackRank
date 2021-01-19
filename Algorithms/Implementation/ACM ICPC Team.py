#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    teamNumber = 0
    knownTopics = 0
    maxKnown = 0
    
    count = 1
    for i in range(len(topic)):
        topic1 = int(topic[i],2)
        for j in range(i+1, len(topic)):
            topic2 = int(topic[j],2)
            res = str(bin(topic1 | topic2)).lstrip('0b')
            
            if res.count('1') > maxKnown:
                maxKnown = res.count('1')
                knownTopics = maxKnown
                teamNumber = 1
            
            elif res.count('1') == maxKnown:
                teamNumber += 1
                
    return [knownTopics, teamNumber]


            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
