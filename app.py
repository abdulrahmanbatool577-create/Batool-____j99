
import gradio as gr
import tensorflow as tf
from PIL import Image
import numpy as np

# تحميل النموذج
model = tf.keras.models.load_model("model.h5")

# أسماء الفئات/الأمراض
labels = ['Cyst', 'Normal', 'Stone', 'Tumor']

def predict(img):
    img = img.resize((224, 224)) # تغيير الحجم ليناسب النموذج
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    predictions = model.predict(img_array)
    confidence = {labels[i]: float(predictions[0][i]) for i in range(len(labels))}
    return confidence

# إنشاء واجهة Gradio
interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=4),
    title="Kidney CT Scan Classification",
    description="قم برفع صورة أشعة الكلية للكشف عن الحالة."
)

if __name__ == "__main__":
    interface.launch()
