import sys
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, data):
        self.fed.append(data)

    def get_data(self):
        return "".join(self.fed)

def main():
    #file_name = "C:/Users/rajiv_000/Documents/Books/Wheel Of Time/NewSpring/OEBPS/9781429961530_ch01.html"
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        try:
            with open(file_name, "r") as content_file:
                content = content_file.read()
                s = MLStripper()
                s.feed(content)
                text = s.get_data()
                if text.__len__() > 0:
                    print(text)
                else:
                    print("Text was not read")
        except BaseException:
            print("Caught an exception: " + BaseException.__str__())
    else:
        print("No filename specified")

if __name__ == "__main__":
    main()
