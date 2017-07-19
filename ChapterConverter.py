from HtmlStripper import MLStripper

class ChapterConverter:
    def __init__(self):
        stripper = MLStripper()
        dest_dir = "./"

    def convert_chapter(self, in_filename):
        try:
            with open(in_filename, "r") as in_file:
                content = in_file.read()
                self.stripper.feed(content)
                out_text = self.stripper.get_data()
                if out_text.__len__() > 0:
                    print(text)
                else:
                    print("Text was not read")
        except BaseException:
            print("Caught an exception: " + BaseException.__str__())
