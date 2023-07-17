# Purpose: To label voice speech by calculating all possible path to get right output by summing over the probabilty of all possible sequence
#           CTC can inference label without giving any data.
# Logic:  By excuting dynamic programming to find best possible path with time efficinty and re-using the data
def __main__():
    
    
# Purpose: To determine all next possible path from time and state
# Logic: by implemending forward algorithm we are able to calcualte alpha value by multiplying probability of evey time sequence
#        Alpha value can be used on next time sequence to find probabilty with less calcuation by re-using alpha t -1 value
#The sequence can start with a blank token or the first character token and end with a blank token or the last character token. So we have to consider both paths.
def forward():
    

def backward():

#Purpose: Calculats joint probability of the sequence at every timestep with value of alpha and beta
#Logic: Get total probability of all paths going though sequence at timestep t by multiplying alpha and beta value 
def CTC_LOSS():