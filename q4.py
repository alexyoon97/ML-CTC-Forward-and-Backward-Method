import numpy as np

# Purpose: To label unsegmented voice data, calculate all possible paths and sum their probabilities for the desire output.
# Logic: Inittialize the 'alpha' and 'beta' matrix to store possibilties for forward and backward, assign value of the 'inputs'.
#        Lastly, compute the CTC loss calculation for each timestep by multiplying 'alpha' and 'beta'.
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
        for s in range(num_label):
            output_probs[t, s] = alpha[t, s] * beta[t, s]
    return output_probs


# Purpose: To determine all next possible paths from time and state
#   By implementing a forward algorithm we are able to calculate the alpha value by multiplying the probability of every time sequence
#   Alpha value can be used on next time sequence to find probability with less calculation by re-using alpha t -1 value
# Logic: Iterate over the time steps from 1 to T and length of labels.
#       Calculate the next probability based on the previous forward variables and input values
def forward(alpha, T, S, inputs, labels):
    for t in range(1, T):
        for s in range(S):
            if s == 0:
                alpha[t, s] = alpha[t-1, s] + inputs[t, labels[s]]
            else:
                alpha[t, s] = alpha[t-1, s] + alpha[t-1, s-1] + inputs[t, labels[s]]
# Logic: Iterate over the time steps from 1 to T and length of labels.
#       Calculate the previous probability based on the t + 1 variables and input values
def backward(beta, T, S, inputs, labels):
    for t in range(T-2, -1, -1):
        for s in range(S-1, -1, -1):
            if s == S-1:
                beta[t, s] = beta[t+1, s] + inputs[t, labels[s]]
            else:
                beta[t, s] = beta[t+1, s] + beta[t+1, s+1] + inputs[t, labels[s]]

#Example usage

#Initialize nessessory variables
inputs = np.array([[0.1, 0.2, 0.3, 0.4],
                   [0.5, 0.6, 0.7, 0.8],
                   [0.9, 1.0, 1.1, 1.2]])

labels = np.array(['A', 'B', 'C'])
# Convert alphabet labels to integer indices
label_indices = np.arange(len(labels))
time_seq, num_label = inputs.shape[0], labels.shape[0]

result = ctc_dynamic_programming(inputs, label_indices, time_seq, num_label)

#Prefix decoding method
#Pick highest probability, and convert back to desire label
output_labels = []
for t in range(result.shape[0]):
  data =  [labels[np.argmax(result[t])] ]
  output_labels.append(data)

print(output_labels)
