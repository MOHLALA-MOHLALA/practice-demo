import cv2

# Load the image
img = cv2.imread("image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a mask
ret, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# Apply the mask to the original image
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Save the output image
cv2.imwrite("output.jpg", masked_img)
