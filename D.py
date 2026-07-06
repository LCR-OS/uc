"""
idee IT
python può trasformare i dizionari in liste di tuple.  
arricchire const_print()
Capire come scegliere il motore con tanti file e motori. 
ragionare su architettura: conv -> scegli motre -> motore converte

ideas EN
Python can transform dictionaries into lists of tuples.
Enrich/Enhance const_print()
Understand how to choose the engine with many files and engines.
Think about architecture: conv -> choose engine -> engine converts
"""

#   Imports
from PIL import Image
from PIL import UnidentifiedImageError
from tkinter import filedialog
from pathlib import Path

#   Formats_lists
input_f = [
    ('BMP', '*.bmp'),
    ('DIB', '*.dib'),
    ('GIF', '*.gif'),
    ('JPEG', '*.jpg *.jpeg *.jpe'),
    ('JPEG2000', '*.jp2 *.j2k *.jpc *.jpf *.jpx *.j2c'),
    ('PNG', '*.png'),
    ('TIFF', '*.tif *.tiff'),
    ('WEBP', '*.webp'),
    ('ICO', '*.ico'),
    ('ICNS', '*.icns'),
    ('PPM', '*.ppm'),
    ('PGM', '*.pgm'),
    ('PBM', '*.pbm'),
    ('PNM', '*.pnm'),
    ('TGA', '*.tga'),
    ('DDS', '*.dds'),
    ('EPS', '*.eps'),
    ('PSD', '*.psd'),
    ('PDF', '*.pdf'),
    ('MPO', '*.mpo'),
    ('PCX', '*.pcx'),
    ('XBM', '*.xbm'),
    ('BLP', '*.blp'),
    ('BUFR', '*.bufr'),
    ('CUR', '*.cur'),
    ('FITS', '*.fits'),
    ('FLI/FLC', '*.fli *.flc'),
    ('GBR', '*.gbr'),
    ('HDF5', '*.h5'),
    ('IM', '*.im'),
    ('IPTC', '*.iim'),
    ('MSP', '*.msp'),
    ('PALM', '*.palm'),
    ('PIXAR', '*.pxr'),
    ('SGI', '*.sgi *.rgb'),
    ('SPIDER', '*.spi'),
    ('SUN', '*.ras'),
    ('WAL', '*.wal'),]

output_f = [
    ('BMP', '*.bmp'),
    ('GIF', '*.gif'),
    ('ICO', '*.ico'),
    ('ICNS', '*.icns'),
    ('JPEG', '*.jpg *.jpeg *.jpe'),
    ('JPEG2000', '*.jp2 *.j2k *.jpc *.jpf *.jpx *.j2c'),
    ('PNG', '*.png'),
    ('TIFF', '*.tif *.tiff'),
    ('WEBP', '*.webp'),
    ('PPM', '*.ppm'),
    ('PGM', '*.pgm'),
    ('PBM', '*.pbm'),
    ('PNM', '*.pnm'),
    ('TGA', '*.tga'),
    ('DDS', '*.dds'),
    ('XBM', '*.xbm'),
    ('PDF', '*.pdf'),]

#   First time trying libraries - needed to ask AI how to write line 111 shame on me 
MESSAGGI = {
     FileNotFoundError : 'File not converted, File Not Found Error.',
     OSError : 'File not converted, OS/IO Error.',
     UnidentifiedImageError : 'File not converted, Unidentified Immage Error.',
     ValueError : 'File not converted, Value Error.',
     KeyError : 'File not converted, Key Error.',
     "success" : 'File converted!'

}

#   constant_print
def const_print(x):
    print(x)

#   GUI I/O
def GUI_IO():
    file_name = filedialog.askopenfilename(
        title='Convert - I/o - matic',
        filetypes=input_f)
    new_format = filedialog.asksaveasfilename(
        title='Convert - i/O - matic',
        filetypes=output_f)
    return file_name, new_format

#   NEW: Errors get handled in their own func - I didn't remember I could write errors(func, *args, **kwargs)
def errors(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except Exception as e:
         const_print(MESSAGGI.get(type(e), f"Error {e}")) #    I need to understand it better, it didn't came from myself. 

#   PILLOW IMG Conversion Engine
def motore_conversione_pillow(a, b):
            with Image.open(a) as img:
                img.save(b)
                const_print(MESSAGGI['success'])
      
def main():
    file_name, new_format = GUI_IO()
    errors(motore_conversione_pillow, file_name, new_format)


if __name__ == '__main__':
    main()
