from pyjects.pytest.anon_survey import AnonymousSurvey

question = "\n What is your favorite programming language?"
survey = AnonymousSurvey(question)

while(True):
    answer = input("\n Enter response: ") 
    if answer.lower() == "q":
        break
    else:
        survey.show_question()
        survey.store_response(answer)

survey.show_results()