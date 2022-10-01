# pip install qrcode pillow

from os import link
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)

#Kommentiere einen der folgenden Links aus um den QR-Code zu generieren
# 1
# link = "https://www.suj-muenchen.de/"
# 2
# link = "mailto:info@suj-muenchen.de"
# 3
# link = "https://www.suj-muenchen.de/info-mail-verwaltung"
# 4
# link = "https://www.technik-in-bayern.de/fileadmin/sn_config/mediapool_tib/bilder/Aktives_Archiv/TiB_02-2021_Konzepte_der_Robotik.pdf"
# 5
# link = "https://www.linkedin.com/in/maximilian-listl/"
# 6
# link = "https://github.com/Ichigomaxi"
# 7
link = "https://github.com/Ichigomaxi/spatio-temporal-graph-builder"

# entscheide Dateiname (kommentiere rest aus)
# 1
# datei_name = "suj_muenchen_website"
# 2
# datei_name = "suj_muenchen_mail"
# 3
# datei_name = "suj_muenchen_newsletter"
# 4
# datei_name = "Konzepte_der_Robotik_QR_Code"
# 5
# datei_name = "LinkedIn_QR_Code"
# 6
# datei_name = "Github_QR_Code"
# 7
datei_name = "Github_Master_thesis_QR_Code"

qr.add_data(link)

#Unterschiedliche Styles die man aussuchen kann
img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_3 = qr.make_image(image_factory=StyledPilImage)


# 3 unterschiedliche Styles werden generiert 
# Dateien werden in current directory dieser datei gespeichert
img_1.save(datei_name + "_1.png")
img_2.save(datei_name + "_2.png")
img_3.save(datei_name + "_3.png")