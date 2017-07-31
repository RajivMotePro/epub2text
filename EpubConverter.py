from ChapterConverter import ChapterConverter
import sys
import os
import zipfile
import glob

class EpubConverter:
    chapter_converter = ChapterConverter()
    out_dir = "./"
    chapter_dir = os.path.join(out_dir, "TEXT")

    def convert_epub(self, in_filename):
        #Unzip in_filename to temporary directory
        out_dir = in_filename + "_temp"
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        with zipfile.ZipFile(in_filename, 'r') as zip_ref:
            zip_ref.extractall(out_dir)
        #Get list of html files to convert, sort by name
        chapter_files = glob.glob(out_dir + "/OEBPS/*_ch*.html")
        chapter_files.sort()
        #Iterate through html files, converting them in a new directory
        chapter_dir = os.path.join(out_dir, "TEXT")
        if not os.path.exists(chapter_dir):
            os.makedirs(chapter_dir)
        for chapter_file in chapter_files:
            chapter_dir_name, chapter_file_name = os.path.split(chapter_file)
            out_chapter_file = os.path.join(chapter_dir, chapter_file_name)
            self.chapter_converter.out_dir = chapter_dir
            print("Converting: " + chapter_dir + " to " + out_chapter_file + ".txt")
            chapter_text_file = self.chapter_converter.convert_chapter(chapter_file)
            print("Converted: " + chapter_text_file)
        #Zip text files
        with zipfile.ZipFile(in_filename + ".zip", 'w', zipfile.ZIP_DEFLATED) as text_zip:
            print("Creating: " + text_zip.filename)
            text_files = glob.glob(chapter_dir + "/*.txt")
            for text_file in text_files:
                path, arcname = os.path.split(text_file)
                print("Adding: " + arcname)
                text_zip.write(text_file, arcname)
            #Return zip file
            return text_zip

def main():
    # file_name = "C:/Users/rajiv_000/Documents/Books/Wheel Of Time/NewSpring/OEBPS/9781429961530_ch01.html"
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        ec = EpubConverter()
        ec.convert_epub(file_name)
        print("Converted.")
    else:
        print("No filename specified")

if __name__ == "__main__":
    main()
