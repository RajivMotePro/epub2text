from HtmlStripper import MLStripper
import sys
import os
import xml.etree.ElementTree

class WoTTocParser:
    def parse_to_one_file(self, base_dir_name):
        toc_file_name = os.path.join(base_dir_name, "toc.ncx")
        with open(toc_file_name, "r") as toc_file:
            root = xml.etree.ElementTree.parse(toc_file).getroot()
            navMap = root[3]
            wot_text_name = os.path.join(base_dir_name, "wot_all.txt")
            with open(wot_text_name, "w", encoding="utf8") as wot_text_file:
                for book in navMap:
                    bookName = book[0][0].text
                    if bookName.isupper():
                        print(bookName)
                        self.write_book_chapters(base_dir_name, book, wot_text_file)

    def parse_to_book_files(self, base_dir_name):
        toc_file_name = os.path.join(base_dir_name, "toc.ncx")
        with open(toc_file_name, "r") as toc_file:
            root = xml.etree.ElementTree.parse(toc_file).getroot()
            navMap = root[3]
            bookNumber = 0
            for book in navMap:
                bookName = book[0][0].text
                if bookName.isupper():
                    print(bookName)
                    wot_text_name = os.path.join(base_dir_name, "wot_%02d_" % (bookNumber) + bookName + ".txt")
                    print("Writing: " + wot_text_name)
                    with open(wot_text_name, "w", encoding="utf8") as wot_text_file:
                        self.write_book_chapters(base_dir_name, book, wot_text_file)
                    bookNumber = bookNumber + 1

    def write_book_chapters(self, base_dir_name, book, wot_text_file):
        for chapter in book.findall("{http://www.daisy.org/z3986/2005/ncx/}navPoint"):
            chapterName = chapter[0][0].text
            if (chapterName.startswith("Prologue")
                    | chapterName.startswith("Epilogue")
                    | chapterName[:1].isdigit()):
                source = chapter[1].get("src").split("#")[0]
                source_file_name = os.path.join(base_dir_name, source)
                print(chapterName + '\t' + source_file_name)
                with open(source_file_name, "r", encoding="utf8") as source_file:
                    stripper = MLStripper()
                    chapter_text = source_file.read()
                    stripper.feed(chapter_text)
                    chapter_text = stripper.get_data()
                    wot_text_file.write(chapter_text)


def main():
    if len(sys.argv) > 1:
        base_dir_name = sys.argv[1]
        parser = WoTTocParser()
        try:
            print("Converting: " + base_dir_name)
            parser.parse_to_book_files(base_dir_name)
            print("Converted: " + base_dir_name)
        except BaseException as ex:
            print(ex)
    else:
        print("No directory specified")

if __name__ == "__main__":
    main()