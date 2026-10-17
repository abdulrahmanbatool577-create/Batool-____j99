
# 🩺 نظام تشخيص أمراض الكلى الذكي باستخدام الشبكات العصبية الالتفافية
### Advanced Kidney CT Scan Multi-Class Classification Framework

---

## 🌟 نبذة عن المشروع (Project Overview)
نظام تشخيصي متكامل يعتمد على تقنيات **الرؤية الحاسوبية (Computer Vision)** و**التعلم العميق (Deep Learning)**، تم تطويره خصيصاً لتحليل ومعالجة صور الأشعة المقطعية (CT Scans) للكلى وتصنيفها فورياً بدقة عالية، مما يسهم في دعم اتخاذ القرار الطبي والتشخيص المبكر للآفات والأورام.

---

## 📊 كفاءة النموذج وأداء التشخيص (Model Benchmark & Metrics)
* **دقة التدريب والتقييم (Model Accuracy):** **93%**
* **نسبة الثقة في الاختبار الحقيقي (Live Prediction Confidence):** **93.42%** (تشخيص مؤكد لفئة الأورام).
* **نموذج التصنيف (Model Architecture):** Deep Convolutional Neural Network (CNN).
* **عدد الفئات المستهدفة:** 4 فئات تشخيصية دقيقة.

---

## 🎯 الفئات التشخيصية المستهدفة (Diagnostic Taxonomy)

1. **Tumor (أورام الكلى):** الكشف عن الكتل والنمو النسيجي غير الطبيعي في أنسجة الكلية.
2. **Cyst (أكياس الكلى):** التمييز الدقيق بين الأكياس الممتلئة بالسوائل والتغيرات النسيجية.
3. **Stone (حصوات الكلى):** رصد وتحديد مكان الترسبات الصلبة والبلورات المعدنية.
4. **Normal (نسيج سليم):** التحقق المباشر من سلامة الكلية وخلوها من أي حيوية مرضية.

---

## 🖼️ إثبات النتيجة والتجربة التشخيصية (Live Inference Result)

توضح الصورة أدناه النتيجة المباشرة لمعالجة إحدى صور الأشعة المقطعية عبر الواجهة التفاعلية للنظام، حيث أظهر النموذج قدرة فائقة على التعرف وتصنيف الحالة بدقة عالية ونسبة ثقة بلغت **93.42%**:

!![نتيجة تشخيص الكلى](https://raw.githubusercontent.com/abdulrahmanbatool577-create/Batool----j99/main/Screenshot_%D9%A2%D9%A0%D9%A2%D9%A2%D9%A0%D9%A2%D9%A1%D9%A1%D9%A7%D9%A0%D9%A4%D9%A0%D9%A7%D9%A9%D9%A7%D9%A5_Google.jpg)

---

## ⚙️ البنية البرمجية والبيئة التقنية (Tech Stack & Libraries)
* **Core Language:** Python 3
* **Deep Learning Framework:** TensorFlow / Keras (CNN Architecture)
* **Image Processing & Analytics:** OpenCV, NumPy, Pillow (PIL)
* **Interactive UI & Deployment:** Gradio Web Interface
* **Development Environment:** Google Colab / Jupyter Notebook

---

## 📂 الهيكلية التنظيمية للمستودع (Repository Structure)
* **`app.py`:** المحرك التنفيذي للواجهة البرمجية والتفاعلية المباشرة (Gradio UI).
* **`training.py`:** البرمجية الخاصة بمعالجة البيانات، بناء المعمارية العصبية، والتدريب.
* **`requirements.txt`:** حزمة الاعتماديات والمكتبات البرمجية المطلوبة للتشغيل.
* **`Screenshot_...jpg`:** وثيقة إثبات الأداء والتجربة التشخيصية الحية للنموذج.
* **`README.md`:** التوثيق التقني والتقرير الشامل لبنية النظام.

---

## 🚀 دليل التشغيل المحلي (Quick Execution Guide)

1. **تثبيت حزمة المكتبات والاعتماديات البرمجية:**
   ```bash
   pip install -r requirements.txt
