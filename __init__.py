import random
from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler
from ovos_audio.service import PlaybackService
import time

def generate_round_questions(round_num):
    if round_num == 0:
        questions = [
            "Drinkt een piraat graag thee",
            "Drinkt een piraat graag sterke rum?"
        ]

        correct_answers = [False, True]

        # Set audio files for round 0
        intro = "./skill_quiz/scene0/tijdelijk.mp3"
        outro = "./skill_quiz/scene0/tijdelijk.mp3"
        main_question = "./skill_quiz/scene0/tutorialq.mp3"
        question_audio_files = ["./skill_quiz/scene0/tutorialqa1.mp3", "./skill_quiz/scene0/tutorialqa2.mp3"]
        correct_answer_audio = "./skill_quiz/scene0/tutorialqcorrect.mp3"
        false_answer_audio = "./skill_quiz/scene0/tutorialqincorrect.mp3"
        duration_intro = 2 #34
        duration_outro = 2 #6
        duration_main = 3
        duration_correct = 7
        duration_false = 6
        duration_answers = 4
        
    elif round_num == 1:
        questions = [
            "Is dit een scheetkussen",
            "Is dit een kat?",
            "Is dit een piraat",
            "Is dit een badeendje?"
        ]

        correct_answers = [False, False, False, True]

        # Set audio files for round 1
        intro = "./skill_quiz/scene1/tijdelijk.mp3"
        outro = "./skill_quiz/scene1/tijdelijk.mp3"
        main_question = "./skill_quiz/scene1/q1.mp3"
        question_audio_files = ["./skill_quiz/scene1/q1a1.mp3", "./skill_quiz/scene1/q1a2.mp3", "./skill_quiz/scene1/q1a3.mp3", "./skill_quiz/scene1/q1a4.mp3"]
        correct_answer_audio = "./skill_quiz/scene1/q1correct.mp3"
        false_answer_audio = "./skill_quiz/scene1/q1incorrect.mp3"
        duration_intro = 2 #52
        duration_outro = 2 #79
        duration_main = 2
        duration_correct = 4
        duration_false = 5
        duration_answers = 5

    elif round_num == 2:
        questions = [
            "Is het een zeeschildpad?",
            "Is het snuf de hond?",
            "Is het Iniminie van Sesamstraat?",
            "Is het CoCo de papegaai?"
        ]

        correct_answers = [False, False, False, True]

        # Set audio files for round 2
        intro = "./skill_quiz/scene2/tijdelijk.mp3"
        outro = None
        main_question = "./skill_quiz/scene2/q2.mp3"
        question_audio_files = ["./skill_quiz/scene2/q2a1.mp3", "./skill_quiz/scene2/q2a2.mp3", "./skill_quiz/scene2/q2a3.mp3", "./skill_quiz/scene2/q2a4.mp3"]
        correct_answer_audio = "./skill_quiz/scene2/q2correct.mp3"
        false_answer_audio = "./skill_quiz/scene2/q2incorrect.mp3"
        duration_intro = 2 #32
        duration_outro = 0
        duration_main = 7
        duration_correct = 10
        duration_false = 11
        duration_answers = 6

    elif round_num == 3:
        questions = [
            "Is het een jonkvrouw?",
            "Wandelende slak?",
            "Is het grote smurf?",
            "Is het kapitein Roodbaard?"
        ]

        correct_answers = [False, False, False, True]

        # Set audio files for round 3
        intro = "./skill_quiz/scene3/tijdelijk.mp3"
        outro = None
        main_question = "./skill_quiz/scene3/q3.mp3"
        question_audio_files = ["./skill_quiz/scene3/q3a1.mp3", "./skill_quiz/scene3/q3a2.mp3", "./skill_quiz/scene3/q3a3.mp3", "./skill_quiz/scene3/q3a4.mp3"]
        correct_answer_audio = "./skill_quiz/scene3/q3correct.mp3"
        false_answer_audio = "./skill_quiz/scene3/q3incorrect.mp3"
        duration_intro = 2 #23
        duration_outro = 0
        duration_main = 4
        duration_correct = 7
        duration_false = 9
        duration_answers = 6


    elif round_num == 4:
        questions = [
            "Waar er gekookt wordt?",
            "Waar de tafel gedekt wordt?",
            "Aan de onderkant van het schip?",
            "Voorin het schip?"
        ]

        correct_answers = [False, False, False, True]

        # Set audio files for round 4
        intro = "./skill_quiz/scene3/tijdelijk.mp3"
        outro = None
        main_question = "./skill_quiz/scene3/q4.mp3"
        question_audio_files = ["./skill_quiz/scene3/q4a1.mp3", "./skill_quiz/scene3/q4a2.mp3", "./skill_quiz/scene3/q4a3.mp3", "./skill_quiz/scene3/q4a4.mp3"]
        correct_answer_audio = "./skill_quiz/scene3/q4correct.mp3"
        false_answer_audio = "./skill_quiz/scene3/q4incorrect.mp3"
        duration_intro = 2 #18
        duration_outro = 0
        duration_main = 5
        duration_correct = 6
        duration_false = 7
        duration_answers = 6

    elif round_num == 5:
        questions = [
            "Lekker bij de haard",
            "Rijg je aan m'n zwaard",
            "Trek de kapitein aan z'n baard",
            "Stelen lijkt me niet de moeite waard"
        ]

        correct_answers = [False, False, False, True]

        # Set audio files for round 5
        intro = "./skill_quiz/scene4/tijdelijk.mp3"
        outro = "./skill_quiz/scene4/tijdelijk.mp3"
        main_question = "./skill_quiz/scene4/q5.mp3"
        question_audio_files = ["./skill_quiz/scene4/q5a1.mp3", "./skill_quiz/scene4/q5a2.mp3", "./skill_quiz/scene4/q5a3.mp3", "./skill_quiz/scene4/q5a4.mp3"]
        correct_answer_audio = "./skill_quiz/scene4/q5correct.mp3"
        false_answer_audio = "./skill_quiz/scene4/q5incorrect.mp3"
        duration_intro = 2 #66
        duration_outro = 2 #46
        duration_main = 4
        duration_correct = 10
        duration_false = 10
        duration_answers = 7


    elif round_num == 6:
        questions = [
            "Speedboot?",
            "Kapitein op een luchtbed?",
            "Een roze dolfijn?",
            "Een zeemeermin?"
        ]

        correct_answers = [False, False, False, True]

        # Set audio files for round 6
        intro = "./skill_quiz/scene5/tijdelijk.mp3"
        outro = "./skill_quiz/scene5/tijdelijk.mp3"
        main_question = "./skill_quiz/scene5/q6.mp3"
        question_audio_files = ["./skill_quiz/scene5/q6a1.mp3", "./skill_quiz/scene5/q6a2.mp3", "./skill_quiz/scene5/q6a3.mp3", "./skill_quiz/scene5/q6a4.mp3"]
        correct_answer_audio = "./skill_quiz/scene5/q6correct.mp3"
        false_answer_audio = "./skill_quiz/scene5/q6incorrect.mp3"
        duration_intro = 2 #35
        duration_outro = 2 #14
        duration_main = 4
        duration_correct = 3
        duration_false = 4
        duration_answers = 3


    elif round_num == 7:
        questions = [
            "Aan het einde van de duikplank?",
            "Achterin bij het roer?",
            "Vooraan het schip?",
            "Helemaal bovenin?"
        ]

        correct_answers = [False, False, False, True]

        # Set audio files for round 7
        intro = "./skill_quiz/scene5/tijdelijk.mp3"
        outro = "./skill_quiz/scene5/tijdelijk.mp3"
        main_question = "./skill_quiz/scene5/q7.mp3"
        question_audio_files = ["./skill_quiz/scene5/q7a1.mp3", "./skill_quiz/scene5/q7a2.mp3", "./skill_quiz/scene5/q7a3.mp3", "./skill_quiz/scene5/q7a4.mp3"]
        correct_answer_audio = "./skill_quiz/scene5/q7correct.mp3"
        false_answer_audio = "./skill_quiz/scene5/q7incorrect.mp3"
        duration_intro = 2 #54
        duration_outro = 2 #8
        duration_main = 6
        duration_correct = 8
        duration_false = 9
        duration_answers = 7



    # Shuffle the questions, their corresponding correct answers, and audio files together
    combined = list(zip(questions, correct_answers, question_audio_files))
    random.shuffle(combined)
    questions, correct_answers, question_audio_files = zip(*combined)

    return questions, correct_answers, question_audio_files, correct_answer_audio, false_answer_audio, intro, outro, main_question, duration_intro, duration_outro, duration_main, duration_correct, duration_false, duration_answers


class QuizGameSkill(OVOSSkill):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.audio = PlaybackService(self.bus)

    @intent_handler("StartQuiz.intent")
    def start_quiz(self, message):
        self.play_game()

    def play_game(self):
        total_rounds = 6

        for round_num in range(0, total_rounds + 1):
            self.gui.show_text(f"Round {round_num}:")
            self.gui.show_text("Ronja en de piraten", override_idle=True)

            questions, correct_answers, question_audio_files, correct_answer_audio, false_answer_audio, intro, outro, main_question, duration_intro, duration_outro, duration_main,  duration_correct, duration_false, duration_answers = generate_round_questions(round_num)

            # Track if intro is already played for the current round
            intro_played = False

            for question, correct_answer, question_audio_file in zip(questions, correct_answers, question_audio_files):

                if not intro_played:
                    # Play the question audio
                    self.play_audio(intro)
                    time.sleep(duration_intro)

                    # Set intro_played to True after playing the intro
                    intro_played = True

                    # Play the main question audio 
                    self.play_audio(main_question)
                    time.sleep(duration_main)

                # Play the question/answer audio
                self.gui.show_text(question, override_idle=True)
                #play_audio_file(question_audio_file)
                self.play_audio(question_audio_file)
                time.sleep(duration_answers)


                reply = None
                while reply not in ['ja', 'nee']:
                    response = self.get_response()

                    if response:
                        reply = response.lower()
                    else:
                        self.speak("Kies maar, ja of nee.")

                if reply == 'ja' and correct_answer:
                    # Play the correct answer audio 
                    self.play_audio(correct_answer_audio)
                    time.sleep(duration_correct)
                    self.gui.show_text('Goed!', override_idle=True)
                    if outro:
                        self.play_audio(outro)
                        self.gui.show_text('Ronja', override_idle=True)
                        time.sleep(duration_outro)
                        break
                    else:
                      #  time.sleep(5)
                        break
                elif (reply == 'ja' and not correct_answer) or (reply == 'nee' and correct_answer):
                    # Play the false answer audio using Mycroft's play_audio_file
                    self.play_audio(false_answer_audio)
                    self.gui.show_text('Ronja', override_idle=True)
                    time.sleep(duration_false)
                    if outro:
                        self.play_audio(outro)
                        time.sleep(duration_outro)
                        break
                    else:
                       # time.sleep(5)
                        self.gui.show_text('Else', override_idle=True)
                        break
 

                elif round_num == total_rounds:
                    self.gui.show_text('Einde', override_idle=True)
                    return
                    self.stop()

    def stop(self):
        pass
