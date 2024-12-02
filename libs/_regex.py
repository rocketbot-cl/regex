import re
from pyparsing import Word, alphas, nums,Literal, Optional, OneOrMore

class Regex:
    
    def __init__(self, code):
        self.code = code
    
    def start_with(self, code, prefix): 
        if not code:
            raise ValueError("insert code")
        if not prefix:
            raise ValueError("insert prefix")
        pattern = rf'\b{re.escape(prefix)}\w*'
        matches = re.findall(pattern, code)
        return matches
    

    def  contains_only(self): #Detecta las cadenas de texto que contienen unicamente numeros o letras.
        alpha_word = Word(alphas)
        numeric_word = Word(nums)
        
        if not self.code:
            raise ValueError("insert code")
        
        result = [] # Se crea una lista para guardar las cadenas de texto
        
        matches_alpha = alpha_word.searchString(self.code)   
        result.extend([match[0] for match in matches_alpha if match[0].isalpha()]) # Agregar coincidencias solo con letras
        matches_numeric =  numeric_word.searchString(self.code)
        result.extend([match[0] for match in matches_numeric if match[0].isdigit()])
        result = [item for item in result if item.isalpha() or item.isdigit()]
        
        if not result:  # Si no se encontraron coincidencias, se muestra el siguiente mensaje
            print("Ingrese un texto que contenga palabras o numeros")
        return result

    def contains_date(self, date_str: str):
        day = Word(nums, exact=2)("day")
        month = Word(nums, exact=2)("month")
        year = Word(nums, exact=4)("year")
        format_date = year + Literal("/") + month + Literal("/") + day

        try:
            
            final_format = format_date.parseString(date_str)
            year_val = int(final_format["year"])
            month_val = int(final_format["month"])
            day_val = int(final_format["day"])

            # Valida el año
            if not (1900 <= year_val <= 2100):
                print("El año debe estar entre 1900 y 2100.")
                return False

            # Valida el mes
            if not (1 <= month_val <= 12):
                print("El mes debe estar comprendido entre 1 y 12.")
                return False

            # Valida el día
            if not (1 <= day_val <= 31):
                print("El día no es válido para el mes/año especificado.")
                return False

            # Verifica meses con 30 días
            if month_val in {4, 6, 9, 11} and day_val > 30:
                print(f"El mes {month_val} no tiene más de 30 días.")
                return False

            # Verifica febrero
            if month_val == 2:
                if (year_val % 4 == 0 and year_val % 100 != 0) or (year_val % 400 == 0):  # Año bisiesto
                    if day_val > 29:
                        print("Febrero no tiene más de 29 días en un año bisiesto.")
                        return False
                else:
                    if day_val > 28:
                        print("Febrero no tiene más de 28 días en un año no bisiesto.")
                        return False

            # Si todo es válido, guarda la fecha
            self.list_date.append(date_str)
            return f"Fecha válida y guardada: {date_str}"

        except Exception as e:
            return f"Error al analizar la fecha: {e}"

    def contains_phone(self, phone:str):
        plus_sign = Literal("+")
        country_code = Word(nums, min=1, max=3)  # El código de país puede ser de 1 a 3 digitos
        separator = Literal("-")
        prefix = Word(nums, exact=1)  # El prefijo es de un numero
        line_number = OneOrMore(Word(nums, exact=2))  # La funcion Oneormore hace que tengan formato de 2 numeros
        
        #Er del formato para nuestro numero de telefono
        number_phone = Optional(plus_sign) + country_code + separator + prefix + OneOrMore(separator + Word(nums, exact=2))

        try:
            #Se hace el parseo con la funcion de la libs/ Verifica  una cadena de texto y si sigue un patron.
            parsed_phone = number_phone.parseString(phone) 
            
            self.list_phone_numbers.append(phone) #captura y guarda el numero
            #Printea el numero de telefono
            print("Número de teléfono:", parsed_phone)
            return parsed_phone
    
        
        except Exception as e:
            print(f"Error al analizar el número de teléfono: {e}")
            return None