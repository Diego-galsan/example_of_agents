import serial
import time
import re
import subprocess
import sys
from datetime import datetime
from google.adk.tools import google_search as search

import os

def run_code(code: str, language: str = "python") -> str:
  """
  Ejecuta código en el lenguaje especificado y retorna el resultado.
  
  Args:
    code: El código que se ejecutará.
    language: El lenguaje de programación (por defecto 'python').
  
  Returns:
    Una cadena con el resultado de la ejecución.
  """
  try:
    if language.lower() == "python":
      # Crear un archivo temporal para ejecutar el código
      import tempfile
      with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
        temp_file.write(code)
        temp_file_path = temp_file.name
      
      # Ejecutar el código
      result = subprocess.run([sys.executable, temp_file_path], 
                            capture_output=True, text=True, timeout=30)
      
      # Limpiar archivo temporal
      os.unlink(temp_file_path)
    
      if result.returncode == 0:
        return f"✅ Ejecución exitosa:\n{result.stdout}"
      else:
        return f"❌ Error en la ejecución:\n{result.stderr}"
    else:
      return f"❌ Lenguaje '{language}' no soportado. Solo se soporta Python por ahora."
  except subprocess.TimeoutExpired:
    return "❌ Timeout: El código tardó más de 30 segundos en ejecutarse."
  except Exception as e:
    return f"❌ Error ejecutando código: {str(e)}"

def crear_archivo_py(nombre_archivo: str, contenido: str) -> str:
  """
  Crea y guarda un archivo .py con el contenido especificado.

  Args:
    nombre_archivo: El nombre del archivo (sin la extensión .py).
    contenido: El código o texto que se escribirá en el archivo.
    
  Returns:
    Mensaje de confirmación del resultado de la operación.
  """
  # Asegurarse de que el nombre del archivo termine con .py
  if not nombre_archivo.endswith('.py'):
    nombre_archivo += '.py'

  try:
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
      archivo.write(contenido)
    return f"✅ Archivo '{nombre_archivo}' creado y guardado exitosamente en {os.path.abspath(nombre_archivo)}"
  except IOError as e:
    return f"❌ Error al crear o guardar el archivo: {e}"

