"""
Hi! This is my first Python program - Hope you enjoy it!
"""

#   Imports
from PIL import Image
from PIL import UnidentifiedImageError
from tkinter import filedialog

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

#   constants
success = 'File Converted!'
FileNotFoundError_const = 'File not converted, File Not Found Error.'
OSError_IOError_const = 'File not converted, OS/IO Error.'
UnidentifiedImageError_const = 'File not converted, Unidentified Immage Error.'
ValueError_const = 'File not converted, Value Error.'
KeyError_const = 'File not converted, Key Error.'

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

#   PILLOW IMG Conversion Engine
def motore_conversione_pillow(a, b):
    try:
        with Image.open(a) as img:
            img.save(b)
            const_print(success)
    except FileNotFoundError:
        const_print(FileNotFoundError_const)
    except UnidentifiedImageError:
        const_print(UnidentifiedImageError_const)
    except (OSError, IOError):
        const_print(OSError_IOError_const)
    except ValueError:
        const_print(ValueError_const)
    except KeyError:
        const_print(KeyError_const)
    
def main():
    file_name, new_format = GUI_IO()
    motore_conversione_pillow(file_name, new_format)
        
main()
