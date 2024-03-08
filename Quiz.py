import requests
import json
import random

url = 'https://opentdb.com/api.php?amount=10&type=multiple'
response = requests.get(url)
data = json.loads(response.text)
questions = data['results']

def ask_question(question):
    options = question['incorrect_answers']
    options.append(question['correct_answer'])
    random.shuffle(options)
    print(question['question'])
    for i, option in enumerate(options):
        print(f"{i+1}.{option}")
    while True:
        user_answer = input("Masukan Jawaban Anda (1-4) atau ketik 'x' untuk berhenti :")
        if user_answer.lower() == 'x':
            return None
        elif user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            break
        else:
            print("Jawaban yang dimasukkan tidak ada, silahkan masukkan nomor yang benar atau 'x' untuk berhenti.")
    correct_answer = options.index(question['correct_answer']) + 1

    if int(user_answer) == correct_answer:
        print("Jawaban Anda benar, selamat!")
        return 1
    else:
        print ("Jawaban Anda salah, ayo coba lagi.")
        return 0
    
def run_quiz():
    score = 0
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}:")
        result = ask_question(question)
        if result is None:
            break
        else:
            score += result
    if result is not None:
        print(f"\nYour Score: {score}/{len(questions)}")
    else:
        print("Anda telah keluar dari kuis.")

run_quiz()