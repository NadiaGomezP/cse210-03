class TerminalService:

    def read_text(self, prompt):

        return input(prompt).capitalize()
        
    def write_text(self, text, list=[]):

        if (len(list) > 0):
            print("".join(list))
        else:
            print(text)

    def draw(self, list):
      
        for i in list:
            print(i)