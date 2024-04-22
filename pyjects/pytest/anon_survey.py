class AnonymousSurvey:

    def __init__(self, q: str) -> None:
        self.question = q
        self.responses = []

    
    def show_question(self):
        print(f"{self.question}")

    
    def store_response(self, answer):
        self.responses.append(answer)


    def show_results(self):
        print("\n Results:")
        [print(f"\n - {resp}") for resp in self.responses]