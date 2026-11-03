#Using pytorch to implement a simple CNN model for image classification
import torch.nn as nn


class CIFAR10Model(nn.Module):

    def __init__(self):
        super().__init__()

        # First convolution
        self.conv1 = nn.Conv2d(
            in_channels=3,
            out_channels=32,
            kernel_size=3,
            padding=1
        )

        # Activation
        self.relu1 = nn.ReLU()

        # Pooling
        self.pool1 = nn.MaxPool2d(
            kernel_size=2,
            stride=2
        )

        # Second convolution
        self.conv2 = nn.Conv2d(
            in_channels=32,
            out_channels=64,
            kernel_size=3,
            padding=1
        )

        self.relu2 = nn.ReLU()

        self.pool2 = nn.MaxPool2d(
            kernel_size=2,
            stride=2
        )

        # Flatten
        self.flatten = nn.Flatten()

        # Fully connected layer
        self.fc1 = nn.Linear(
            64 * 8 * 8,
            128
        )

        self.relu3 = nn.ReLU()

        # Output layer
        self.fc2 = nn.Linear(
            128,
            10
        )


    def forward(self, x):

        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)

        x = self.conv2(x)
        x = self.relu2(x)
        x = self.pool2(x)

        x = self.flatten(x)

        x = self.fc1(x)
        x = self.relu3(x)

        x = self.fc2(x)

        return x

model = CIFAR10Model()

print(model)