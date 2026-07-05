from PIL import Image
from PIL import UnidentifiedImageError
from tkinter import filedialog

#   liste formati
formati_input = [
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

formati_output = [
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

#   costanti
hooray = 'hooray'
non_hooray = 'non hooray'

#   stampo le costanti
def const_print(x):
    print(x)

#   GUI I/O
def convo():
    nome_file = filedialog.askopenfilename(
        title='Convertitore Super Figo',
        filetypes=formati_input)
    nuovo_formato = filedialog.asksaveasfilename(
        title='Convertitore Super Figo',
        filetypes=formati_output)
    return nome_file, nuovo_formato

#   Conversione immagini
def motore_conversione_pillow(a, b):
    try:
        with Image.open(a) as img:
            img.save(b)
            const_print(hooray)
    except FileNotFoundError:
        const_print(non_hooray)
    except (OSError, IOError):
        const_print(non_hooray)
    except UnidentifiedImageError:
        const_print(non_hooray)
    except ValueError:
        const_print(non_hooray)
    except KeyError:
        const_print(non_hooray)
    
def main():
    nome_file, nuovo_formato = convo()
    motore_conversione_pillow(nome_file, nuovo_formato)
        
main()
