import sys
import os
import xml.etree.ElementTree

class WoTTocParser:
    def parse(self, base_dir_name):
        toc_file_name = os.path.join(base_dir_name, "toc.ncx")
        with open(toc_file_name, "r") as toc_file:
            root = xml.etree.ElementTree.parse(toc_file).getroot()
            navMap = root[3]
            for book in navMap:
                bookName = book[0][0].text
                if bookName.isupper():
                    print(bookName)
                    for chapter in book.findall("{http://www.daisy.org/z3986/2005/ncx/}navPoint"):
                        chapterName= chapter[0][0].text
                        if chapterName.startswith("Prologue") | chapterName.startswith("Epilogue") | chapterName[:1].isdigit():
                            source = chapter[1].get("src")
                            print(chapterName + '\t' + source)

def main():
    if len(sys.argv) > 1:
        base_dir_name = sys.argv[1]
        try:
            print("Converting: " + base_dir_name)
            parser = WoTTocParser()
            parser.parse(base_dir_name)
            print("Converted: " + base_dir_name)
        except BaseException:
            print("Caught an exception: " + BaseException.__str__())
    else:
        print("No directory specified")

if __name__ == "__main__":
    main()