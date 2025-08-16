from PIL import Image
import torchvision.transforms.V2 as tfs_v2


img_pil = Image.new(mode="RGB", size=(128, 128), color=(0, 128, 255))

# здесь продолжайте программу
img = tfs_v2.ToTensor()
img = img(img_pil)

# img = tfs_v2.ToTensor()(img_pil)
