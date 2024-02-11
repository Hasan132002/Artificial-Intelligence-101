from PIL import Image, ImageFilter, ImageEnhance

def remove_features(image):
    return image.filter(ImageFilter.GaussianBlur(radius=2))

def apply_image_processing(image_path):
    original_image = Image.open(image_path)

    edge_detected_image = original_image.filter(ImageFilter.FIND_EDGES)

    blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=2))

    sharpened_image = original_image.filter(ImageFilter.SHARPEN)

    grayscale_image = original_image.convert("L")

    enhancer = ImageEnhance.Brightness(original_image)
    brightened_image = enhancer.enhance(1.5)  

    feature_removed_image = remove_features(original_image)

    original_image.show(title="Original Image")
    edge_detected_image.show(title="Edge Detected Image")
    blurred_image.show(title="Blurred Image")
    
    sharpened_image.show(title="Sharpened Image")
    grayscale_image.show(title="Grayscale Image")
    brightened_image.show(title="Brightened Image")
    feature_removed_image.show(title="Feature Removed Image")

apply_image_processing('1.jpeg')
