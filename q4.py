import numpy as np

# Purpose: To label unsegment voice data, by calculating all possible path to get right output by summing over the probabilty of all possible sequence
#           CTC can inference label the sequence by predicting.
# Logic:  By excuting dynamic programming to find best possible path with time efficinty and re-using the data
def ctc_dynamic_programming(inputs, labels, time_seq, num_label):
    
# Initialize the forward variables
    alpha = np.zeros((time_seq, num_label))
    alpha[0, 0] = inputs[0, labels[0]]
    alpha[0, 1:] = inputs[0, labels[1:]]
    forward(alpha, time_seq, num_label, inputs, labels)
    
# Initialize the backward variables
    beta = np.zeros((time_seq, num_label))
    beta[time_seq-1, num_label-1] = inputs[time_seq-1, labels[num_label-1]]
    beta[time_seq-1, :num_label-1] = inputs[time_seq-1, labels[:num_label-1]]
    backward(beta, time_seq, num_label, inputs, labels)

# Compute the output probabilities
    output_probs = np.zeros((time_seq, num_label))
    for t in range(time_seq):
        for c in range(num_label):
            output_probs[t, c] = alpha[t, c] * beta[t, c]
    return output_probs


# Purpose: To determine all next possible path from time and state
#          by implemending forward algorithm we are able to calcualte alpha value by multiplying probability of evey time sequence
#        Alpha value can be used on next time sequence to find probabilty with less calcuation by re-using alpha t -1 value
# Logic: Iterate over the time steps from 1 to T and length of labels, update the alpha values based on preivous alpha value
def forward(alpha, T, C, inputs, labels):
    for t in range(1, T):
        for c in range(C):
            if c == 0:
                alpha[t, c] = alpha[t-1, c] + inputs[t, labels[c]]
            else:
                alpha[t, c] = alpha[t-1, c] + alpha[t-1, c-1] + inputs[t, labels[c]]
def backward(beta, T, C, inputs, labels):
    for t in range(T-2, -1, -1):
        for c in range(C-1, -1, -1):
            if c == C-1:
                beta[t, c] = beta[t+1, c] + inputs[t, labels[c]]
            else:
                beta[t, c] = beta[t+1, c] + beta[t+1, c+1] + inputs[t, labels[c]]


# Purpose: The value of output will be too small after implement forward-backward algorithm, to prevent underflow rescale the value
# def rescaling():

# Purpose: To filter out e and repeative character from forward-backward algorithm output
# Logic: Get total probability of all paths going though sequence at timestep t by multiplying alpha and beta value
# def beam_search_decoding():

inputs = np.array([[0.1, 0.2, 0.3, 0.4],
                   [0.5, 0.6, 0.7, 0.8],
                   [0.9, 1.0, 1.1, 1.2]])

labels = np.array(['A', 'B', 'C'])
# Convert alphabet labels to integer indices
label_indices = np.arange(len(labels))
time_seq, num_label = inputs.shape[0], labels.shape[0]
result = ctc_dynamic_programming(inputs, label_indices, time_seq, num_label)

# Convert the output probabilities back to alphabet labels by picking most highest probability.
output_labels = np.array([labels[np.argmax(result[t])] for t in range(result.shape[0])])
print(output_labels)
