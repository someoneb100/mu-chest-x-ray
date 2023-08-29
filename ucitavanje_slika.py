import numpy as np
from PIL import Image
from os import path, listdir

def count_files(src_path) -> int:
    return sum(map(
        lambda f: path.isfile(path.join(src_path, f)),
        listdir(src_path)
    ))

def load_images_to_numpy(src_path: str) -> np.ndarray:
    res = listdir(src_path)
    res = map(lambda f: path.join(src_path, f), res)
    res = map(Image.open, res)
    res = map(np.asarray, res)
    res = np.stack([*res], axis=0)
    return res

def load_images(src_path: str):
    def load(dir: bool):
        img = load_images_to_numpy(path.join(src_path, str(dir)))
        target_f = np.ones if dir else np.zeros
        target = target_f((img.shape[0], ), dtype=np.uint8) 
        return img, target
    true_img, true_target = load(True)
    false_img, false_target = load(False)
    img = np.concatenate([true_img, false_img])
    target = np.concatenate([true_target, false_target])
    return (img, target)
