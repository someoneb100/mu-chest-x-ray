# mu-chest-x-ray

Projekat testira razne arhitekture konvolucionih neuronskih mreža na
skupu podataka crno-belih rendgenskih snimaka grudnog koša sa kaggle sajta ([link ka skupu](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)).

Slike su već skinute i mogu se naći na Google drajvu na [ovoj adresi](https://drive.google.com/drive/folders/11dYMiRJGWQBm9R-RhRcIsXQHhXNQNavH?usp=drive_link).

Pošto sam morao da koristim Google Colaboratory za treniranje modela usled nedostatka hardvera, ceo projekat (Svaki Notebook, sačuvani podaci i modeli) nalaze se na [ovoj adresi](https://drive.google.com/drive/folders/1lyoUvf1tIdcL9ir_DTBZ9V6tgEDKUpcb?usp=drive_link).

Na repozitorijumu se nalaze samo skinuti Notebook-ovi sa google colaboratory, nisu predviđeni za pokretanje.

Projekat samostalno radi Petar Đorđević 1088/2022

Korišćene biblioteke:
- tensorflow
- keras
- numpy
- pandas
- matplotlib

Linkovi ka odgovarajućim Notebook-ovima:
- [analiza i pretprocesiranje podataka](https://colab.research.google.com/drive/1kYCvDYCTRXri8uAo31QbRxygu7qmnPDr?usp=sharing)
- [jednostavan model](https://colab.research.google.com/drive/1k875iRdiVcQgofLd0wWjAg0lGp0H8Kgu?usp=sharing)
- [manji model od prethodnog](https://colab.research.google.com/drive/16ulrVoqDEFsTZnA0DXipncZVWQ5wLtTC?usp=drive_link)
- [manji sa šumom](https://colab.research.google.com/drive/1OZn3sQnSJtRR2T63PiLzqRr6YGP6uMXf?usp=drive_link)
- [potpuno konvolutivna mreža](https://colab.research.google.com/drive/1GiM4WDhNDb516Ghox7PawPzZ6Sn6Q85o?usp=drive_link)
- [alexnet](https://colab.research.google.com/drive/1WstB98S1yDEAdOiq9vryDVVbZtWIAvKK?usp=drive_link)
- [vgg16](https://colab.research.google.com/drive/1LfaVNv3ltNBeAvMBu2Phk1NbX-zwXhwQ?usp=drive_link)

Reference:
 - [Introduction to The Architecture of Alexnet | Analytics Vidhya](https://www.analyticsvidhya.com/blog/2021/03/introduction-to-the-architecture-of-alexnet/)
 - [Understanding VGG16: Concepts, Architecture, and Performance | datagen](https://datagen.tech/guides/computer-vision/vgg16/#)