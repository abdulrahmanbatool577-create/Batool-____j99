
---
title: Kidney CT Scan Classification
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
---

# 🩺 Kidney CT Scan Classification using Deep Learning (CNN)

نظام ذكاء اصطناعي يعتمد على الشبكات العصبية الالتفافية (CNN) لتصنيف صور الأشعة المقطعية للكلى تلقائياً والتعرف على الحالات المرضية بدقة عالية.

---

## 📌 1. Overview (نظرة عامة)
يهدف هذا المشروع إلى التمييز وتصنيف أربع حالات رئيسية للكلى من خلال تحليل صور الأشعة المقطعية (CT Scan):
* 🔴 **Tumor** (أورام الكلى)
* 🟡 **Cyst** (أكياس الكلى)
* 🔵 **Stone** (حصوات الكلى)
* 🟢 **Normal** (سليمة)

---

## 🛠️ 2. Tech Stack (التقنيات المستخدمة)
* **Framework & Model:** TensorFlow / Keras (CNN Model)
* **User Interface:** Gradio Interactive Web UI
* **Programming Language:** Python 3
* **Libraries:** NumPy, Pillow, Matplotlib

---

## 📁 3. Project Structure (هيكلية المشروع)
```text
├── app.py              # ملف التشغيل الرئيسي وواجهة Gradio التفاعلية
├── model.h5            # نموذج الذكاء الاصطناعي المدرَّب (CNN Model)
├── requirements.txt    # قائمة المكتبات والاعتماديات البرمجية
└── README.md           # التوثيق والشرح التفصيلي للمشروع


## 🖼️ نتيجة التجربة التشخيصية (Live Test Result)
![تشخيص الكلى](Screenshot_٢٠٢٦-٠٢-٢١-١٧-٠٤-٠٧-٩٧٥_Google.jpg)
*(ملاحظة: تأكدي فقط أن اسم الصورة في الكود مطابق تماماً لاسم الصورة التي رفعتيها، أو يمكنكِ نسخ اسم ملف الصورة من القائمة ولصقه).*
