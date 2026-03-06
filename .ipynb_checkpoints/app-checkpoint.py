{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0a3a669e-698a-42be-a23d-29ab2aaa05bc",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstreamlit\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mst\u001b[39;00m\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mjoblib\u001b[39;00m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mnumpy\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mnp\u001b[39;00m\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'streamlit'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# 1. Load the pre-trained 'brains'\n",
    "try:\n",
    "    model = joblib.load('poly_model.pkl')\n",
    "    transformer = joblib.load('poly_transformer.pkl')\n",
    "except:\n",
    "    st.error(\"Missing files! Make sure 'poly_model.pkl' is in the same folder.\")\n",
    "\n",
    "st.title(\"🎓 Student Score Predictor\")\n",
    "\n",
    "# 2. User Input\n",
    "hours = st.number_input(\"How many hours did you study?\", min_value=0, max_value=100, value=20)\n",
    "\n",
    "if st.button(\"Predict My Score\"):\n",
    "    # 3. Transform input to Polynomial (This matches your Degree 2 math)\n",
    "    input_array = np.array([[hours]])\n",
    "    transformed_input = transformer.transform(input_array)\n",
    "    \n",
    "    # 4. Predict\n",
    "    prediction = model.predict(transformed_input)\n",
    "    st.success(f\"Your predicted Exam Score is: {prediction[0]:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f7e6470-0fe1-4d72-a9e8-d84a40f09d02",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
