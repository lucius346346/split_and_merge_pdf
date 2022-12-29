import argparse
import os
import joinPDF
import splitPDF

# przyjmuje parametr ścięzki z zewnątrz
parser = argparse.ArgumentParser()
parser.add_argument("dir", nargs='+')
args = parser.parse_args()

paths = args.dir
# wyciągą nazwę pliku bez rozszerzenia

os.chdir(os.path.dirname(paths[0]))

# jeśli przesłany został jeden plik rozdziel go na strony
if len(paths) == 1:
    file_name = os.path.splitext(os.path.basename(paths[0]))[0]
    splitPDF.merge(paths[0], file_name)
# w przeciwnym wypadku złącz pliki
else:
    joinPDF.join(paths)

