This app is a personalized AI-powered tutoring system called Yukthi-Mitra. It helps users learn by offering a dynamic quiz, analyzing their performance, and generating a personalized study plan.
***
### Core Features

1. Personalized Quizzes: The app uses Google's **Gemini AI** to generate unique quizzes on demand.
    The `generate_questions_with_ai` function sends a prompt to the AI specifying the language and difficulty level (`Beginner`, `Intermediate`, `Advanced`).
    The AI responds with a perfectly formatted JSON object of questions, which the app then uses to create a multiple-choice quiz.
2. Performance Analysis: After the user submits the quiz, the app calculates a score and identifies **"weak topics"** by checking which question topics the user answered incorrectly.
    This data is stored in a `users.json` file, so the user's progress is saved between sessions.
3. Actionable Insights: Based on the weak topics, the app provides three personalized tools:
    Dashboard: A visual summary of the last quiz's score and weak topics using a bar chart.
    Timetable: A 7-day study plan that allocates recommended study hours to each weak topic, creating a structured path for improvement.
    Pace Tracker: A doughnut chart that visually breaks down a user's learning pace, classifying topics as "Fast," "Medium," or "Slow" based on the number of mistakes, and estimates the time needed to master them.
4.  AI Chatbot: A built-in chatbot allows users to ask follow-up questions about concepts they struggle with, providing immediate, conversational help powered by the Gemini AI model.
5.  Study Materials: The app also provides access to curated external web links and YouTube videos related to the weak topics to provide additional resources for the user.

In short, Yukthi-Mitra goes beyond a simple quiz app. It uses AI to adapt to the user's performance, providing a comprehensive, **personalized learning ecosystem** that helps them understand not only *what* they don't know but also *how* to improve.
