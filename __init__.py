import random
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util.audio_utils import play_audio_file
import time

def generate_round_questions(round_num):
    if round_num == 0:
        questions = [
            "Drinkt een piraat graag thee",
            "Drinkt een piraat graag sterke rum?"
        ]

        correct_answers = [False, True]

        # Set audio files for round 0
        intro = "./skill_quiz/scene0/q0intro.mp3"
        outro = "./skill_quiz/scene0/tutorialoutro.mp3"
        main_question = "./skill_quiz/scene0/tutorialq.mp3"
        question_audio_files = ["./skill_quiz/scene0/tutorialqa1.mp3", "./skill_quiz/scene0/tutorialqa2.mp3"]
        correct_answer_audio = "./skill_quiz/scene0/tutorialqcorrect.mp3"
        false_answer_audio = "./skill_quiz/scene0/tutorialqincorrect.mp3"
        duration_intro = 33


    elif round_num == 1:
        questions = [
            "Is dit een scheetkussen",
            "Is dit een kat?",
            "Is dit een piraat",
            "Is dit een badeendje?"
        ]

        correct_answers = [False, False, False, True]

        # Set audio files for round 1
        intro = "./skill_quiz/scene1/q1intro.mp3"
        outro = "./skill_quiz/scene1/q1outro.mp3"
        main_question = "./skill_quiz/scene1/q1.mp3"
        question_audio_files = ["./skill_quiz/scene1/q1a1.mp3", "./skill_quiz/scene1/q1a2.mp3", "./skill_quiz/scene1/q1a3.mp3", "./skill_quiz/scene1/q1a4.mp3"]
        correct_answer_audio = "./skill_quiz/scene1/q1correct.mp3"
        false_answer_audio = "./skill_quiz/scene1/q1incorrect.mp3"
        duration_intro = 51

    elif round_num == 2:
        questions = [
            "Is het een zeeschildpad?",
            "Is het snuf de hond?",
            "Is het Iniminie van Sesamstraat?",
            "Is het CoCo de papegaai?"
        ]

        correct_answers = [False, False, False, True]

        # Set audio files for round 2
        intro = "./skill_quiz/scene2/q2intro.mp3"
        outro = "./skill_quiz/scene2/q2outro.mp3"
        main_question = "./skill_quiz/scene2/q2.mp3"
        question_audio_files = ["./skill_quiz/scene2/q2a1.mp3", "./skill_quiz/scene2/q2a2.mp3", "./skill_quiz/scene2/q2a3.mp3", "./skill_quiz/scene2/q2a4.mp3"]
        correct_answer_audio = "./skill_quiz/scene2/q2correct.mp3"
        false_answer_audio = "./skill_quiz/scene2/q2incorrect.mp3"
        duration_intro = 31

    elif round_num == 3:
        questions = [
            "Is het een jonkvrouw?",
            "Wandelende slak?",
            "Is het grote smurf?",
            "Is het kapitein Roodbaard?"
        ]

        correct_answers = [False, False, False, True]

        # Set audio files for round 3
        intro = "./skill_quiz/scene3/q3intro.mp3"
        outro = "./skill_quiz/scene3/q3outro.mp3"
        main_question = "./skill_quiz/scene3/q3.mp3"
        question_audio_files = ["./skill_quiz/scene3/q3a1.mp3", "./skill_quiz/scene3/q3a2.mp3", "./skill_quiz/scene3/q3a3.mp3", "./skill_quiz/scene3/q3a4.mp3"]
        correct_answer_audio = "./skill_quiz/scene3/q3correct.mp3"
        false_answer_audio = "./skill_quiz/scene3/q3incorrect.mp3"
        duration_intro = 23


    elif round_num == 4:
        questions = [
            "vraag 4.1",
            "vraag 4.2",
            "vraag 4.3",
            "vraag 4.4"
        ]

        correct_answers = [False, False, False, True]

        # Set audio files for round 4
        intro = "./skill_quiz/scene3/q4intro.mp3"
        outro = "./skill_quiz/scene3/q4outro.mp3"
        main_question = "./skill_quiz/scene3/q4.mp3"
        question_audio_files = ["./skill_quiz/scene3/q4a1.mp3", "./skill_quiz/scene3/q4a2.mp3", "./skill_quiz/scene3/q4a3.mp3", "./skill_quiz/scene3/q4a4.mp3"]
        correct_answer_audio = "./skill_quiz/scene3/q4correct.mp3"
        false_answer_audio = "./skill_quiz/scene3/q4incorrect.mp3"
        duration_intro = 18


    # Shuffle the questions, their corresponding correct answers, and audio files together
    combined = list(zip(questions, correct_answers, question_audio_files))
    random.shuffle(combined)
    questions, correct_answers, question_audio_files = zip(*combined)

    return questions, correct_answers, question_audio_files, correct_answer_audio, false_answer_audio, intro, outro, main_question, duration_intro

class QuizGameSkill(MycroftSkill):
    def __init__(self):
        super().__init__()

    @intent_handler("StartQuiz.intent")
    def start_quiz(self, message):
        self.play_game()

    def play_game(self):
        total_rounds = 4

        for round_num in range(0, total_rounds + 1):
            self.gui.show_text(f"Round {round_num}:")
            self.gui.show_text("Ronja en de piraten", override_idle=True)

            questions, correct_answers, question_audio_files, correct_answer_audio, false_answer_audio, intro, outro, main_question, duration_intro = generate_round_questions(round_num)

            for question, correct_answer, question_audio_file in zip(questions, correct_answers, question_audio_files):

                # Play the question audio using Mycroft's play_audio_file
                play_audio_file(intro)
                time.sleep(duration_intro)

                # Play the question audio using Mycroft's play_audio_file
                play_audio_file(main_question)
                time.sleep(4)

                # Play the question audio using Mycroft's play_audio_file
                self.gui.show_text(question, override_idle=True)
                play_audio_file(question_audio_file)
                time.sleep(6)

                reply = None
                while reply not in ['ja', 'nee']:
                    response = self.get_response()

                    if response:
                        reply = response.lower()
                    else:
                        self.speak("Kies maar, ja of nee.")


                if reply == 'ja' and correct_answer:
                    # Play the correct answer audio using Mycroft's play_audio_file
                    play_audio_file(correct_answer_audio)
                    self.gui.show_text('Top', override_idle=True)
                    if outro:
                        play_audio_file(outro)
                        time.sleep(5)
                        break
                    else:
                        time.sleep(5)
                        break
                elif (reply == 'ja' and not correct_answer) or (reply == 'nee' and correct_answer):
                    # Play the false answer audio using Mycroft's play_audio_file
                    play_audio_file(false_answer_audio)
                    if outro:
                        play_audio_file(outro)
                        time.sleep(5)
                        break
                    else:
                        time.sleep(5)
                        break

                elif round_num == total_rounds:
                    #self.speak('Congratulations! You completed all rounds.')
                    return

    def stop(self):
        pass

def create_skill():
    return QuizGameSkill()



