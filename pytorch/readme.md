
# [PyTorch](http://pytorch.org)

PyTorch is a deep learning framework that puts Python first. Tensors and Dynamic neural networks in Python with strong
GPU acceleration. We are in an early-release Beta. Expect some adventures.


## Basics - [`basics/`](basics/)
- [`tensors.ipynb`](basics/tensors.ipynb) - Understand PyTorch’s tensors and how to create them from Numpy arrays.
- [`autograd.ipynb`](basics/autograd.ipynb) - Automatic differentiation of tensor calculation graphs.

![Example Computational Graph](basics/graph.svg)


## Neural Networks - [`neural_network/`](neural_network/)
- [`neural_network.ipynb`](neural_network/neural_network.ipynb) - Neural Network module and example network with cost function.
- [`cifar10.ipynb`](neural_network/cifar10.ipynb) - Train a small neural network to classify CIFAR10 dataset images.

![AlexNet Neural Network Computational Graph](neural_network/alexnet.svg)


## Deep Q-Network Algorithm - [`dqn/`](dqn/)
- [`dqn.ipynb`](dqn/dqn.ipynb) - DQN agent trained on the `CartPole` environment with experience replay.

![DQN Algorithm Acting on the CartPole OpenAI Gym Environment](dqn/cartpole.gif)


## Cross-Entropy Method - [`cem/`](cem/)
- [`cem.ipynb`](cem/cem.ipynb) - Cross-entropy optimization method implemeted as `pytorch.optim.Optimizer`.
- [`cem.pdf`](cem/cem.pdf) - Explanation

![Cross-Entropy Method Pseudo Code](cem/cem.png)



### Requirements
- [Jupyter](http://jupyter.org/) - Application to create documents with contain code, equations, visualizations and text.
- [PyTorch](http://pytorch.org/) - Tensor manipulation framework with automatic differentiation.
- [Open AI Gym](http://gym.openai.com/) - Toolkit for developing and comparing reinforcement learning algorithms.
