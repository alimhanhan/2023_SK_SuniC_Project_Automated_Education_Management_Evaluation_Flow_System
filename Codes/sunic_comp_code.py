# -*- coding: utf-8 -*-
"""SuniC_Comp_Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hSGJiL-WPweMFbEC6REIMWEMT8s7K6B7
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class EducationUnderstandingBot:
    def __init__(self):
        self.summary_data = []
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None

    def add_summary(self, summary):
        self.summary_data.append(summary)
        self._update_tfidf_matrix()

    def _update_tfidf_matrix(self):
        self.tfidf_matrix = self.vectorizer.fit_transform(self.summary_data)

    def calculate_similarity(self, user_summary):
        if not self.summary_data:
            return 0.0

        if self.tfidf_matrix is None:
            self._update_tfidf_matrix()

        user_tfidf = self.vectorizer.transform([user_summary])
        similarity_scores = cosine_similarity(user_tfidf, self.tfidf_matrix).flatten()

        average_similarity = sum(similarity_scores) / len(similarity_scores)
        return average_similarity * 100

bot = EducationUnderstandingBot()

# User interaction
print("HRD 교육 후 교육 이해도 측정을 시작합니다.")
user_summary = input("교육 수강자님, 본인이 이해한 대로 교육 내용을 요약하여 입력해주세요: ")

# Save user response to a text file
user_response_file_path = "/content/user.txt"
with open(user_response_file_path, "w", encoding="utf-8") as user_file:
    user_file.write(user_summary)

bot.add_summary(user_summary)

# Read content from file and store in chatgpt_summary
file_path = "/content/test.txt"
with open(file_path, "r", encoding="utf-8") as file:
    chatgpt_summary = file.read()

print(f"\nChatGPT의 요약본: {chatgpt_summary}")

# Calculate and display education understanding score
score = bot.calculate_similarity(chatgpt_summary)
print(f"\n측정 이해도: {score:.2f}%")