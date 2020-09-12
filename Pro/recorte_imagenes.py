from PIL import Image
import numpy as np

region=(1400,400,2400,2000)
k=np.arange(15,65,5)
i=0
for i in k:
    namI='img/img_c_ilu/'+str(i)+'.jpg'
    img=Image.open(namI)
    imageS=img.crop(region)
    namIS=str(i)+'_c.jpg'
    imageS.save(namIS)

  


