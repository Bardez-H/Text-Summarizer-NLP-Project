import torch

print("Number of GPUs:", torch.cuda.device_count())
print("Current GPU Device:", torch.cuda.get_device_name(0))

# import  torch

# print(torch.cuda.is_available())