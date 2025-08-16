from PIL import Image
import torchvision.transforms.v2 as tfs_v2


img_pil = Image.new(mode="RGB", size=(128, 128), color=(0, 128, 255))

# здесь продолжайте программу
transforms = tfs_v2.Compose([tfs_v2.Grayscale(),
                          tfs_v2.ToTensor(),
                          tfs_v2.Normalize([0.5], [1])
                         ])

img = transforms(img_pil)
