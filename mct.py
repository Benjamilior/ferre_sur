
import re
import json
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'  # Cambiar check
SPREADSHEET_ID = '1l2jZGmnAZN7Y8cELYIP_6eeKvBz9ivrJLgW5faYvMs0'  # Cambiar check
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar en modo headless (sin ventana)
chrome_options.add_argument("--window-size=1920x1080")
start_time = time.time()  # Tiempo de inicio de la ejecución
driver = webdriver.Chrome(options=chrome_options)

# URLs y SKUs
sku2 = {"Vinagrmanare6": "https://mct.cl/ficha/50571/rodillo-poliester-hela-160mm"}  # Se usa para probar funcionalidades sin tener que correr todo

sku={
    "Ferresurdotu1": "https://mct.cl/ficha/87199/cemento-bio-bio-especial-25kg",
    "Ferresurdotu4": "https://mct.cl/ficha/8854/fierro-liso-red-8mm-sae-1020-x-6-mts",
    "Ferresurdotu7": "https://mct.cl/ficha/11169/tornillo-hex-cgoma-pta-broca-zn-12-x-112-100u",
    "Ferresurdotu11": "https://mct.cl/ficha/11177/tornillo-hex-cgoma-pta-broca-zn-12-x-2-100u",
    "Ferresurdotu13": "https://mct.cl/ficha/9180/fierro-liso-red-6mm-x-6mts-comercial-n",
    "Ferresurdotu29": "https://mct.cl/ficha/11197/tornillo-volchgrueso-pfina-crs-6x158-zn-100u",
    "Ferresurdotu33": "https://mct.cl/ficha/16937/terciado-estructural-cd-18mm-122x244mt",
    "Ferresurdotu44": "https://mct.cl/ficha/56156/brocha-estampa-3",
    "Ferresurdotu46": "https://mct.cl/ficha/56157/brocha-estampa-4",
    "Ferresurdotu48": "https://mct.cl/ficha/78995/pellet-15kg",
    "Ferresurdotu51": "https://mct.cl/ficha/30138/codo-875-grsanitario-gris-40-mm",
    "Ferresurdotu52": "https://mct.cl/ficha/17836/tubo-pvc-hidr-40mmx6mts-pn-10-cem-tigre",
    "Ferresurdotu58": "https://mct.cl/ficha/56154/brocha-estampa-2",
    "Ferresurdotu62": "https://mct.cl/ficha/11776/aguarras-solvente-1-lts",
    "Ferresurdotu73": "https://mct.cl/ficha/17837/tubo-pvc-hidr-50mmx6mts-pn-10-cem-tigre",
    "Ferresurdotu76": "https://mct.cl/ficha/2193/clavo-ctes-3-x-10",
    "Ferresurdotu83": "https://mct.cl/ficha/78995/pellet-15kg",
    "Ferresurdotu85": "https://mct.cl/ficha/30139/codo-875-grsanitario-gris-50-mm",
    "Ferresurdotu89": "https://mct.cl/ficha/16937/terciado-estructural-cd-18mm-122x244mt",
    "Ferresurdotu91": "https://mct.cl/ficha/50178/adhesivo-ceramico-polvo-standar-25kg-weber",
    "Ferresurdotu92": "https://mct.cl/ficha/25072/terciado-estructural-cd-09mm-122x244mt",
    "Ferresurdotu93": "https://mct.cl/ficha/22606/pino-cepillado-seco-2-x-3-x-3200",
    "Ferresurdotu103": "https://mct.cl/ficha/30140/codo-875-grsanitario-gris-75-mm",
    "Ferresurdotu107": "https://mct.cl/ficha/2375/codo-pvc-sanitario-d110-x-875-ccem-vinilit",
    "Ferresurdotu121": "https://mct.cl/ficha/47952/diluyente-piroxpxl-std-1-lts-duco",
    "Ferresurdotu124": "https://mct.cl/ficha/2390/adhesivo-101-pomo-60cc-vinilit",
    "Ferresurdotu133": "https://mct.cl/ficha/47952/diluyente-piroxpxl-std-1-lts-duco",
    "Ferresurdotu134": "https://mct.cl/ficha/11837/fibrocemento-permanit-base-ceram-6-mm-12-x-24",
    "Ferresurdotu136": "https://mct.cl/ficha/56744/terciado-ranurado-clasico-cpc-12mm-122-x-244mt",
    "Ferresurdotu138": "https://mct.cl/ficha/16935/terciado-estructural-cd-12mm-122x244mt",
    "Ferresurdotu139": "https://mct.cl/ficha/33768/pino-dimensionado-verde-2-x-4-x-3200",
    "Ferresurdotu140": "https://mct.cl/ficha/84413/osb-multiplac-90-x-122-x-244-mts",
    "Ferresurdotu159": "https://mct.cl/ficha/53080/rollete-impregnado-de-4-5-x-2400-110mm-120mm",
    "Ferresurdotu167": "https://mct.cl/ficha/56243/pino-impregnado-2-x-6-x-3200",
    "Ferresurdotu168": "https://mct.cl/ficha/30844/fibrocemento-volcanboard-5mm-1200-x-2400",
    "Ferresurdotu169": "https://mct.cl/ficha/78492/sellotec-montaje-300ml-blco",
    "Ferresurdotu171": "https://mct.cl/ficha/30132/codo-45-grsanitario-gris-75-mm",
    "Ferresurdotu179": "https://mct.cl/ficha/58889/sifon-lavaplatos-loa-1-12-a-1-14-salcur",
    "Ferresurdotu186": "https://mct.cl/ficha/70542/esmalte-al-agua-semibrillo-blco-sipa",
    "Ferresurdotu210": "https://mct.cl/ficha/71636/zincalum-5v-030-x-895-x-3000-az80",
    "Ferresurdotu223": "https://mct.cl/ficha/17834/tubo-pvc-hidr-25mmx6mts-pn-125-cem-tigre",
    "Ferresurdotu233": "https://mct.cl/ficha/43840/clavo-ctes-2-x-12-bwg",
    "Ferresurdotu236": "https://mct.cl/ficha/87240/llave-gas-12-hi-he",
    "Ferresurdotu239": "https://mct.cl/ficha/68450/valvula-bola-llave-jardin-34",
    "Ferresurdotu241": "https://mct.cl/ficha/58889/sifon-lavaplatos-loa-1-12-a-1-14-salcur",
    "Ferresurdotu253": "https://mct.cl/ficha/22464/pino-cepillado-seco-2-x-2-x-3200",
    "Ferresurdotu258": "https://mct.cl/ficha/19113/soldadura-6011-x-332-indura",
    "Ferresurdotu264": "https://mct.cl/ficha/59488/anticorrosivo-negro-sipa",
    "Ferresurdotu266": "https://mct.cl/ficha/70526/latex-extracubriente-blanco-sipa",
    "Ferresurdotu271": "https://mct.cl/ficha/38883/fibrocemento-volcanboard-ranurado-6mm-1200x2400",
    "Ferresurdotu278": "https://mct.cl/ficha/45143/vitrolux-63-barniz-semibrillo-chilcorrof",
    "Ferresurdotu281": "https://mct.cl/ficha/72818/pintura-techo-acrizinc-negro-g-sipa",
    "Ferresurdotu283": "https://mct.cl/ficha/50571/rodillo-poliester-hela-160mm",
    "Ferresurdotu305": "https://mct.cl/ficha/88875/latex-extracubriente-blanco-4-sipa",
    "Ferresurdotu309": "https://mct.cl/ficha/63807/rodillo-chiporro-18cm-pl-natural-hela",
    "Ferresurdotu320": "https://mct.cl/ficha/13177/caneria-cobre-pagua-12-x-6000-tipo-m",
    "Ferresurdotu326": "https://mct.cl/ficha/56709/flexible-12-hi-x-12-hi-30-cm",
    "Ferresurdotu328": "https://mct.cl/ficha/13156/caneria-cobre-tipo-l-12-x-6000",
    "Ferresurdotu337": "https://mct.cl/ficha/98700/fibrocemento-permanit-8mm-120-x-240",
    "Ferresurdotu345": "https://mct.cl/ficha/64530/silicona-1100-negra-310-ml-agorex",
    "Ferresurdotu351": "https://mct.cl/ficha/33221/malla-cuadrada-n-5014-x-150-mts-x-25-mts",
    "Ferresurdotu353": "https://mct.cl/ficha/28515/malla-c-139-se-10-x-10-26-x-5-mt",
    "Ferresurdotu360": "https://mct.cl/ficha/14525/sifon-lavaplato-1-12-curva-ampl40-m-vin",
    "Ferresurdotu384": "https://mct.cl/ficha/1905/esmalte-al-agua-pzafach-blanco-ceresita",
    "Ferresurdotu397": "https://mct.cl/ficha/42015/protector-madera-cerestain-encina",
    "Ferresurdotu418": "https://mct.cl/ficha/37627/desague-lavatorio-1-14-crebalse-y-cola",
    "Ferresurdotu424": "https://mct.cl/ficha/98712/piso-flotante-er-gold-teak-80m-18954m2",
    "Ferresurdotu425": "https://mct.cl/ficha/66949/candado-bronce-pulido-30-mm-p-2000-lioi",
    "Ferresurdotu427": "https://mct.cl/ficha/68455/flexible-agua-metalico-he-hi-12-25-cm",
    "Ferresurdotu452": "https://mct.cl/ficha/17403/desague-crebalse-ptina-112",
    "Ferresurdotu489": "https://mct.cl/ficha/88819/latex-constructor-blanco-4-soquina",
    "Ferresurdotu494": "https://mct.cl/ficha/36832/puerta-int-terc-200-x-080",
    "Ferresurdotu501": "https://mct.cl/ficha/42015/protector-madera-cerestain-encina",
    "Ferresurdotu513": "https://mct.cl/ficha/6367/soldadura-7018-rh-x-18",
    "Ferresurdotu542": "https://mct.cl/ficha/60721/calefont-splendid-7-ltsgas-lic-ionizado",
    "Ferresurdotu553": "https://mct.cl/ficha/36831/puerta-int-terc-200-x-075",
    "Ferresurdotu563": "https://mct.cl/ficha/36834/puerta-int-terc-200-x-090",
    "Ferresurdotu565": "https://mct.cl/ficha/33219/malla-cuadrada-n-5014-x-100-mts-x-25-mts",
    "Ferresurdotu566": "https://mct.cl/ficha/45939/sifon-trampa-tipo-s-112-salida-40mm-hoff"
}

results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element(By.XPATH, '/html/body/div[13]/div/div[2]/div[1]/div/div/div[2]/p[2]/span')  # Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_normal_element = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span/span/span[2]')  # Cambiar
        precio_normal = precio_normal_element.text  # Guarda el precio normal
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div[2]/div[3]/p/span[2]')  # Cambiar
            precio_normal = precio_normal_element.text  # Guarda el precio normal
        except NoSuchElementException as e:
            print(f"No se pudo encontrar el precio en la URL {url} - {e}")

    # Extraer solo los números del precio
    precio_normal = re.sub(r'\D', '', precio_normal)  # Eliminar todo excepto los dígitos
    precio_oferta = re.sub(r'\D', '', precio_oferta)  # Eliminar todo excepto los dígitos

    data = {
        "SKU": sku_key,
        "Precio": precio_normal,
        "Precio_oferta": precio_oferta
    }
    results.append(data)
    print(data)
    time.sleep(0.5)

driver.quit()

df = pd.DataFrame(results)
competitor = "mct" 
# Guardar el DataFrame en un archivo Excel (opcional)
# nombre_archivo = "datos_productos.xlsx"  # Nombre del archivo Excel
# df.to_excel(nombre_archivo, index=False)  # El parámetro index=False evita que se incluyan los índices en el archivo Excel
# print(f"Datos guardados en {nombre_archivo}")

end_time = time.time()  # Tiempo de finalización de la ejecución
execution_time = end_time - start_time
print("Tiempo de ejecución: %.2f segundos" % execution_time)

# Fecha de Extracción
now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
data = {"": now_str}
json_data = json.dumps(data)
values = [[json_data]]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
                               range='mct!F2',  # CAMBIAR
                               valueInputOption='USER_ENTERED',
                               body={'values': values}).execute()

# Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'], item['Precio_oferta']] for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
                               range='mct!A2:C83',  # CAMBIAR
                               valueInputOption='USER_ENTERED',
                               body={'values': values}).execute()
print(f"Datos insertados correctamente")

# Enviar datos a otro Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
NEW_SPREADSHEET_ID = '1ofzsOShcjwZn_lo_yvQhtteoUQfNxPfP8O-4wo-u1vo'  # ID de la nueva hoja de cálculo

creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Obtener la última fila con datos en la nueva hoja
result = sheet.values().get(spreadsheetId=NEW_SPREADSHEET_ID, range='ferre_sur!A:A').execute() #Cambiar donde llega la info
values = result.get('values', [])
last_row = len(values) + 1  # Obtener el índice de la última fila vacía

# Convertir resultados a la lista de valores
values = [[row['SKU'], competitor, row['Precio'], row['Precio_oferta'], now_str] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'ferre_sur!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

print(f"Datos insertados correctamente en la nueva hoja de Google Sheets en el rango {update_range}")