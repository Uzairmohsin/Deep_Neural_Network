# Deep_Neural_Network
**Experiment 1:**
Theoretical Background of the MP Neuron

The MP neuron, short for the McCulloch–Pitts neuron, is the earliest mathematical model of a biological neuron, introduced in 1943 by Warren McCulloch and Walter Pitts. It represents a foundational concept in the development of artificial neural networks and computational neuroscience. The model was primarily designed to simulate basic logical operations using a simplified abstraction of neural behavior.

The MP neuron operates with binary input and output signals. Each input can take only two possible values, 0 or 1, and the neuron produces a single binary output. Every input is associated with a fixed weight, which can be either excitatory (positive) or inhibitory (negative) in nature.

The neuron computes the weighted sum of all its inputs and compares this sum to a predefined threshold value (θ). If the weighted sum is greater than or equal to the threshold, the neuron becomes active and produces an output of 1 (fires). Otherwise, the neuron remains inactive and outputs 0.

The original MP neuron model does not include any learning mechanism. The weights and threshold values are manually defined in advance to achieve a desired logical function, such as AND, OR, or NOT gates.

Despite its historical significance, the MP neuron has notable limitations. Due to its fixed parameters and binary nature, it is capable of solving only linearly separable problems and cannot handle more complex, non-linear decision boundaries. Consequently, while it laid the groundwork for modern neural models, it is not directly used in contemporary deep neural networks.
