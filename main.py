import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

DICE_SIZE = 10
SCALE = 0.5

def pixel_to_dice(pixel):
    if pixel < 50:
        return 1
    elif pixel < 100:
        return 2
    elif pixel < 150:
        return 3
    elif pixel < 200:
        return 4
    elif pixel < 250:
        return 5
    else:
        return 6

def load_dices():
    lados = []
    for i in range(1, 7):
        dado = cv.imread(f'dados/lado_{i}.jpg')
        dado = cv.resize(dado, (DICE_SIZE, DICE_SIZE))
        lados.append(dado)
    return lados

def image_to_dices(img, dices):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    h, w = gray.shape
    new_w = int(w * SCALE)
    new_h = int(h * SCALE)
    resized = cv.resize(gray, (new_w, new_h))
    nova_imagem = np.zeros((new_h * DICE_SIZE, new_w * DICE_SIZE, 3), dtype=np.uint8)
    for i in range(0, new_h * DICE_SIZE, DICE_SIZE):
        for j in range(0, new_w * DICE_SIZE, DICE_SIZE):
            dado = dices[pixel_to_dice(resized[i // DICE_SIZE, j // DICE_SIZE]) - 1]
            nova_imagem[i:i+DICE_SIZE, j:j+DICE_SIZE] = dado
    return nova_imagem

def main():
    image_path = 'images/panda.webp'
    example_path = 'examples/panda.webp'
    
    img = cv.imread(image_path)
    
    dices = load_dices()
    nova_imagem = image_to_dices(img, dices)
    
    cv.imwrite(example_path, nova_imagem)
    
    plt.imshow(nova_imagem)
    plt.show()
    
    
if __name__ == '__main__':
    main()


