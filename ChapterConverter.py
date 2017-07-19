from HtmlStripper import MLStripper
import sys
import os.path

class ChapterConverter:
    stripper = MLStripper()

    def convert_chapter(self, in_filename):
        try:
            out_filename = in_filename + ".txt"
            with open(in_filename, "r") as in_file:
                content = in_file.read()
                self.stripper.feed(content)
                out_text = self.stripper.get_data()
                if out_text.__len__() > 0:
                    with open(out_filename, "w") as out_file:
                        out_file.write(out_text)
                    return out_filename
                else:
                    print("Text was not read")
        except BaseException:
            print("Caught an exception: " + BaseException.__str__())

def main():
    #file_name = "C:/Users/rajiv_000/Documents/Books/Wheel Of Time/NewSpring/OEBPS/9781429961530_ch01.html"
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        cc = ChapterConverter()
        out_filename = cc.convert_chapter(file_name)
        print("Wrote " + out_filename)
    else:
        print("No filename specified")

if __name__ == "__main__":
    main()
