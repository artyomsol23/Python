from PIL import Image
import torchvision.transforms.v2 as tfs_v2


img_pil = Image.new(mode="RGB", size=(128, 128), color=(0, 128, 255))

# здесь продолжайте программу
transforms = tfs.Compose([tfs_v2.CenterCrop(64),
                          tfs_v2.Resize(128),
                          tfs_v2.ToTensor()
                         ])

img = transforms(img_pil)
