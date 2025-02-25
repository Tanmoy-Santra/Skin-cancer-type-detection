# 🏥 Skin-Cancer-Type-Detection  

## 📌 Project Description  

## 📂 **Database and Preprocessing Drive Link**  
[Click here to access the dataset](https://drive.google.com/drive/folders/1qvTAbpOEorUi-vTXffzbA0rfPig2BBke?usp=sharing)

### **🔹 Introduction**  
Skin cancer is one of the most common types of cancer worldwide. Early detection and classification of different skin cancer types can significantly improve treatment success. This project leverages **Deep Learning** to classify skin cancer types using **Convolutional Neural Networks (CNNs)**.  

### **🎯 Goal:**  
- **Preprocess and clean** the dataset to improve model accuracy.  
- **Train a CNN model** using deep learning techniques.  
- **Deploy the model** with a Flask API backend and a React-based frontend hosted on Vercel.  

### **📊 Dataset Used**  
We use the **HAM10000 dataset** (Human Against Machine dataset), which contains **10,000+ images** of skin lesions categorized into **seven classes**:  
1. **Actinic keratoses (AKIEC)**  
2. **Basal cell carcinoma (BCC)**  
3. **Benign keratosis-like lesions (BKL)**  
4. **Dermatofibroma (DF)**  
5. **Melanoma (MEL)**  
6. **Melanocytic nevi (NV)**  
7. **Vascular lesions (VASC)**  

---

## 🔄 **Project Workflow**  

### **1️⃣ Data Preprocessing (Cleaning & Augmentation)**  
✅ **Sorting Images** → Organized into **7 classes** based on the provided metadata.  
✅ **Hair Removal** → Applied **BlackHat filtering** and **inpainting**.  
✅ **Class Balancing** →  
   - **Oversampled classes reduced** (Max **1000 images per class**).  
   - **Augmentation applied to undersampled classes**.  
✅ **Renaming & Resizing** → Standardized filenames & resized images to **128x128** or **256x256 pixels**.  

### **2️⃣ Model Training & Evaluation**  
✅ **Deep Learning Model** → CNN built using **Keras & TensorFlow**.  
✅ **Performance Metrics** → Accuracy, Precision, Recall, Confusion Matrix.  

### **3️⃣ Deployment & Hosting**  
✅ **Backend:** Flask serves the trained model.  
✅ **Frontend:** Vite (React.js) for UI, hosted on **Vercel**.  
✅ **API Communication:** Flask exposes an endpoint for predictions.  

---

## 🛠️ **Tools & Technologies Used**  

### 🔹 **Machine Learning & Data Processing**  
- **Google Colab & Jupyter Notebook** (for model training & evaluation)  
- **TensorFlow & Keras** (deep learning model)  
- **Scikit-learn (sklearn)** (for preprocessing & evaluation metrics)  
- **Seaborn & Matplotlib** (for data visualization)  

### 🔹 **Web Development & Deployment**  
- **Flask** (Backend for model API)  
- **Vite (React.js)** (Frontend for UI)  
- **Vercel** (Frontend hosting)  

---

## 📂 **Preprocessing Pipeline**  

### **1️⃣ Data Cleaning & Organization**  
✔ **Images sorted** based on diagnosis in `HAM10000_metadata.csv`.  
✔ **Duplicate images removed** to avoid bias.  

### **2️⃣ Hair Removal**  
✔ Used **BlackHat filtering** & **inpainting** techniques for image enhancement.  

### **3️⃣ Data Augmentation & Balancing**  
✔ **Oversampled classes reduced** (Max 1000 per class).  
✔ **Synthetic images generated** for underrepresented classes using:  
   - **Rotation**  
   - **Zooming**  
   - **Flipping**  
   - **Contrast Adjustment**  

### **4️⃣ Standardization & Normalization**  
✔ Resized images to **128x128 or 256x256 pixels** for uniformity.  
✔ Applied **MinMax scaling** to pixel values.  

---

## 🚀 **How to Run the Project?**  

### **🔹 Backend (Flask API)**  
1. **Install dependencies:**  
   ```bash
   pip install flask tensorflow numpy pandas scikit-learn ```
2. **Run the Flask app:**
```bash
   python app.py
### ** 🔹 Frontend (Vite + React.js)**
1. **Install dependencies:**

 npm install

2. Start the frontend server:

npm run dev
