import os #importeert de os module
from PIL import Image #import vanuit pillow library de image class

output_dir = 'Python/data2fish/PDFs/' #een variabel aanmaken om de convereted screenshots naar deze map te sturen
source_dir = 'Python/data2fish/screenshots_py/' #dit is waar de screenshot/images vandaan worden gehaald

for file in os.listdir(source_dir): #het pad naar het bestand geven
    if file.split('.')[-1] in ('png', 'jpg', 'jpeg'): #checken wat voor extensie het bestand is in het geval dat het geen normaal bestaand is
        image = Image.open(os.path.join(source_dir, file)) #het bestand openen met de library
        image_converted = image.convert('RGB') #ervoor zorgen dat het kleuren profiel in RGB is
        image_converted.save(os.path.join(output_dir, '{0}.pdf'.format(file.split('.')[-2]))) #hier word ervoor gezorgd dat het opslaat als een pdf bestand en de extensie aldus verandert.