"""keyword arguments parameter"""


def tuner(**kwargs):
    brightness = kwargs.get('brightness', .7)
    contrast = kwargs.get('contrast')
    hue = kwargs.get('hue', .7)

    print(brightness, contrast, hue)


tuner()
tuner(brightness=.18)
tuner(brightness=.8, contrast=.69, hue=.78)
param = {'brightness': 0.77, 'contrast': 0.66, 'hue': 0.88}
tuner(**param)

