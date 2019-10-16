PATH = 'dataset/'

from fastai.vision import *
from fastai.metrics import accuracy

tfms = get_transforms()
data = ImageDataBunch.from_folder(PATH, valid='validation', ds_tfms=tfms, bs=64, num_workers=4).normalize(imagenet_stats)

model = cnn_learner(data, models.resnet152, metrics=accuracy, pretrained=True)
model.fit_one_cycle(20, max_lr=1.32e-06)

interp = ClassificationInterpretation.from_learner(model)
interp.plot_confusion_matrix()
interp.plot_top_losses(4, figsize=(8,8))

model.save('alzheimers')
model.export()