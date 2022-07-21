import timm
from torch import nn


# pretrained_model = 


class CustomModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.backbone = timm.create_model(
            'resnet50',
            pretrained=True)
        self.linear = nn.Linear(1000, 1)


    def forward(self, x):
        hidden = self.backbone(x)
        pred = self.linear(hidden)
        return pred
