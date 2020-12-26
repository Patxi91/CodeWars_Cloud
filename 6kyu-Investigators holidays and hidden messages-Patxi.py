class Investigator:
    message = ''
    def __init__(self):
        pass

    def postcard(self, text):
        print(text)
        if "  " in text:
            for i in range(text.count("  ")):
                text2 = text[text.index("  ")+2:]
                text = text[:text.index("  ")]
                self.message = self.message+''.join(c for i,c in enumerate(text) if (c.isupper() and i!=0 and text[i-1].islower()))
                self.message = self.message+' '
                text=text2
            self.message = self.message+''.join(c for i,c in enumerate(text) if (c.isupper() and i!=0 and text[i-1].islower()))
        else:
            self.message = self.message+''.join(c for i,c in enumerate(text) if (c.isupper() and i!=0 and text[i-1].islower()))
        pass

    def hidden_message(self):
        return self.message