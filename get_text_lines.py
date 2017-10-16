import cv2

org_img = cv2.imread("0.jpg")

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
imS = cv2.resize(org_img, (600, 600))
cv2.imshow('image', imS)
cv2.waitKey(0)

org_gray = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
imS = cv2.resize(org_gray, (600, 600))
cv2.imshow('image', imS)
cv2.waitKey(0)

morphStructure = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
gradient = cv2.morphologyEx(org_gray, cv2.MORPH_GRADIENT, morphStructure)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
imS = cv2.resize(gradient, (600, 600))
cv2.imshow('image', imS)
cv2.waitKey(0)

ret2, binary = cv2.threshold(gradient, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
imS = cv2.resize(binary, (600, 600))
cv2.imshow('image', imS)
cv2.waitKey(0)

morphStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 15))
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, morphStructure)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
imS = cv2.resize(closed, (600, 600))
cv2.imshow('image', imS)
cv2.waitKey(0)

_, contours, hierarchy = cv2.findContours(closed, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

rectangle_position = []

for cnt in contours:
    if cv2.contourArea(cnt) > 50:
        [x, y, w, h] = cv2.boundingRect(cnt)

        if h < 10 or w < 10:
            continue

        crop_closed = closed[y:y+h, x:x+w]

        r = cv2.countNonZero(crop_closed)/(w * h)

        if r > 0.45:
            rectangle_position.append((x, y, x + w, y + h, ((y + y + h) / 2)))
            cv2.rectangle(org_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
imS = cv2.resize(org_img, (600, 600))
cv2.imshow('image', imS)
cv2.waitKey(0)
