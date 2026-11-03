import torch
import torch.nn as nn
import torch.optim as optim

#crete a simple neural network model
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

y = [
    0,
    0,
    0,
    1
]

#covert the data in appropriate format
x = torch.tensor(X,dtype=torch.float32)
y = torch.tensor(y,dtype=torch.float32).reshape(-1,1)

#explicitly define the model
class mymodel(nn.Module):

    def __init__(self):
        super().__init__()

        self.layer1 = nn.Linear(2,4)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(4,1)

    def forward(self,x):
        x=self.layer1(x)
        x= self.relu(x)
        x= self.layer2(x)

        return x

model = mymodel()
#optimizer and loss function

criteria = nn.BCEWithLogitsLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr= 0.01
)

#train the model
for epoch in range(100):
    output = model(x)
    loss = criteria(output,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

#evaluate the model
model.eval()
with torch.no_grad():
    output = model(x)
    probabilities = torch.sigmoid(output)

    # Convert probability to 0 or 1
    predictions = torch.round(probabilities)

    accuracy = (predictions == y).float().mean()
    print("Accuracy:", accuracy.item())

#make prediction
model.eval()

with torch.no_grad():
    output = model(x)
    probabilities = torch.sigmoid(output)

    predictions = torch.round(probabilities)

print(predictions)

#save the model
torch.save(
    model.state_dict(),
    "my_model.pth"
)