import cv2 as cv
import os
import numpy as np

imgPath = "image/patch_yuyan.jpg"
imgName = os.path.splitext(imgPath)[0].split('/')[-1]
img = cv.imread(imgPath, cv.IMREAD_UNCHANGED)
h, w, _ = img.shape

patch_h = 0
patch_w = 0

print(w, h)

while w > 2560 or h > 1440:
    if w > 2560 and h > 1440:
        patch_h = h // 2
        patch_w = w // 2
        h = patch_h
        w = patch_w
    elif w > 2560 and h <= 1440:
        patch_w = w // 2
        w = patch_w
    elif w <= 2560 and h > 1440:
        patch_h = h // 2
        h = patch_h

print(w, h)
print(patch_w, patch_h)

H, W, _ = img.shape
start_w, start_h = 0, 0
count = 1
print(len(img))
while start_h < H:
    if start_w + patch_w < W and start_h + patch_h < H:
        patch = img[start_h:start_h + patch_h, start_w:start_w + patch_w, :]
        start_w += patch_w
        cv.imwrite('image/patch/' + imgName + str(count) + '.jpg', patch)

    elif start_w + patch_w >= W and start_h + patch_h >= H:
        patch = img[start_h:, start_w:, :]
        cv.imwrite('image/patch/' + imgName + str(count) + '.jpg', patch)
        break

    elif start_w + patch_w >= W and start_h + patch_h < H:
        patch = img[start_h:start_h + patch_h, start_w:, :]
        start_w = 0
        start_h += patch_h
        cv.imwrite('image/patch/' + imgName + str(count) + '.jpg', patch)

    elif start_w + patch_w < W and start_h + patch_h >= H:
        patch = img[start_h:, start_w:start_w + patch_w, :]
        start_w += patch_w
        cv.imwrite('image/patch/' + imgName + str(count) + '.jpg', patch)

    count += 1

# cv.namedWindow('patch', 0)

# while W >= patch_w and H >= patch_h:
#     patch = img[:patch_w, :patch_h, :]
#     cv.imshow('patch', patch)
#     cv.waitKey(0)
