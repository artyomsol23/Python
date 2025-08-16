from PIL import Image
import torchvision.transforms as tfs
# import torchvision.transforms.v2 as tfs_v2 - недоступен на Stepik

img_pil = Image.new(mode="RGB", size=(128, 128), color=(0, 128, 255))

# здесь продолжайте программу
img = tfs.ToTensor()
img = img(img_pil)

# img = tfs.ToTensor()(img_pil)
