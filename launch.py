import os

# Lista de nombres de los scripts que deseas ejecutar
scripts = [
    "mct.py",
    "meli.py",
    "sodimac.py",
    "ferre.py"]

# Iteramos sobre la lista de scripts y los ejecutamos uno por uno
for script in scripts:
    # Construimos la ruta completa al script
    script_path = os.path.join(os.path.dirname(__file__), script)
    print(f"Ejecutando {script}...")
    # Ejecutamos el script usando execfile (Python 2) o exec(open().read()) (Python 3)
    # Ejecutar scripts directamente con execfile o exec(open().read()) no es recomendado por razones de seguridad.
    # Aquí asumimos que los scripts son seguros.
    exec(open(script_path).read())
    print(f"{script} ejecutado.")
