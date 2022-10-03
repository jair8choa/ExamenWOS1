import json


PATH = "/home/jochoa/escuela/python/examen/"
ARCHIVO_ALUMNOS = "Estudiantes.prn"
ARCHIVO_MATERIAS = "Kardex.txt"  
    
def traer_alumnos():  
  try:
    archivo_alumnos =  open(PATH+ARCHIVO_ALUMNOS, "r")
    
    alumnos_array = archivo_alumnos.read().splitlines()
    archivo_alumnos.close()
    alumnos = []    
    
    for alumno in alumnos_array:
      NC = alumno[0:8]
      nombre = alumno[8:]
      alumnos.append([NC,nombre])  
    
    return alumnos
      
  except:
      print(f"No existe el archivo") 
      return ["error"]

def traer_materias():  
  try:
    archivo_materias =  open(PATH+ARCHIVO_MATERIAS, "r", errors="ignore")
    
    materias_array = archivo_materias.read().splitlines()
    archivo_materias.close()
    materias = []    
    
    for materia in materias_array:
      arr = materia.split('|')
      materias.append([arr[0],arr[1]])
    
    return materias
      
  except:
      print(f"No existe el archivo") 
      return ["error"]

def createJSON(*kargs):
  
  res = []
  materias_arr = []
  alumno_map = {}
  
  if len(kargs) == 0:
    for alumno in alumnos:
      alumno_map["Nombre"] = alumno[1]
      for materia in materias:
        if alumno[0] == materia[0]:
          materias_arr.append(materia[1])
      alumno_map["Materias"] = materias_arr.copy()
      materias_arr.clear()
      res.append(alumno_map.copy())   
  else:
    for alumnoBuscar in kargs:
      for alumno in alumnos:
        if alumno[0] == alumnoBuscar:
          alumno_map["Nombre"] = alumno[1]
          for materia in materias:
            if alumno[0] == materia[0]:
              materias_arr.append(materia[1])
          alumno_map["Materias"] = materias_arr.copy()
          materias_arr.clear()
          res.append(alumno_map.copy())
  return res
  
    
if __name__ == "__main__":
    alumnos = traer_alumnos()
    materias = traer_materias()
    
    # res = createJSON("18420473","18420470","18420100")
    res = createJSON()
    
    jsonString = json.dumps(res, indent=4)
    jsonFile = open("res.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    