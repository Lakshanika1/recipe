# 🍳 AI Recipe Generator

## 📌 Project Overview

The **AI Recipe Generator** is a Python-based application that uses Google's Gemini AI to generate recipes based on the food ingredients provided by the user.

The application accepts a list of food ingredients as input and generates a recipe with a dish name, required ingredients, and step-by-step preparation instructions.

It uses the **Google Gemini 2.5 Flash model** to understand user input and generate relevant recipe suggestions. The application also validates the input through prompt-based instructions to ensure that it focuses only on recipe generation.

## ✨ Features

- **AI-Powered Recipe Generation:** Generates recipes using Google Gemini AI.
- **Ingredient-Based Suggestions:** Creates recipes based on the ingredients provided by the user.
- **Structured Output:** Displays recipes in an organized format with dish name, ingredients, and preparation steps.
- **Input Validation:** Provides a predefined response when the input is not a list of food ingredients.
- **Interactive Command-Line Interface:** Allows users to generate multiple recipes in a single session.
- **Secure API Key Management:** Uses environment variables to protect API credentials.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **AI Model:** Google Gemini 2.5 Flash
- **AI Integration:** Google GenAI SDK
- **Environment Management:** Python-dotenv

## 📂 Project Structure

```text
gemini-chatbot/
│
├── .gitignore
├── recipe.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Lakshanika1/recipe.git
```

### 2. Navigate to the Project Directory

```bash
cd recipe
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Google Gemini API Key

- Obtain an API key from [Google AI Studio](https://aistudio.google.com/).
- Create a `.env` file in the project directory.
- Add your API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

**Note:** Never upload your `.env` file or expose your API key on GitHub.

### 5. Run the Application

```bash
python recipe.py
```

## 💻 Usage

1. Run the Python application.
2. Enter a list of available food ingredients.
3. The Gemini AI model processes the input.
4. The application generates a recipe with the dish name, ingredients, and preparation steps.
5. Enter `exit` to terminate the application.

### Example Input

```text
Enter ingredients (or type 'exit'): tomato, onion, potato, salt
```

### Example Output

```text
Dish Name: Potato Tomato Curry

Ingredients Required:
- Potato
- Tomato
- Onion
- Salt
- Oil
- Spices

Steps:
1. Wash and chop the potatoes, tomatoes, and onions.
2. Heat oil in a pan and sauté the onions.
3. Add tomatoes and spices and cook until soft.
4. Add potatoes and mix well.
5. Add water and cook until the potatoes become tender.
6. Serve hot.
```

*Note: The generated recipe may vary depending on the input and AI response.*

### Invalid Input Example

```text
Enter ingredients (or type 'exit'): Hello

I can only generate recipes from ingredients provided.
```

## 📦 Requirements

The project requires the following Python packages:

```text
google-genai
python-dotenv
```

Install them using:

```bash
pip install google-genai python-dotenv
```

## 🔐 Security

- API credentials are stored in a `.env` file.
- Environment variables are loaded using `python-dotenv`.
- The `.env` file should be included in `.gitignore`.
- Never commit API keys or other sensitive credentials to a public repository.

## 🚀 Future Enhancements

- Add a graphical user interface using Streamlit.
- Support dietary preferences such as vegetarian and vegan recipes.
- Include cooking time and serving suggestions.
- Add cuisine-based recipe recommendations.
- Display nutritional information for generated recipes.

## 🎯 Conclusion

The AI Recipe Generator demonstrates the practical integration of Generative AI into a Python application using Google's Gemini API.

By accepting available food ingredients and generating structured cooking instructions, the project showcases API integration, prompt engineering, environment variable management, and interactive application development.

It provides a simple foundation for building more advanced AI-powered cooking and food recommendation applications.

## 👩‍💻 Author

**Lakshanika A P**

B.E. Computer Science and Engineering

---

⭐ If you find this project useful, consider giving this repository a star!
