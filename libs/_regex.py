import re
from pyparsing import Word, alphas, nums,Literal,Optional,OneOrMore

class Regex:
    
    def __init__(self,code:str):
        self.code = code
        self.list_date = []
        
    
    def start_with(self, code, prefix): # Detecta las cadenas de texto ya sea que empiecen con numeros o letras.
        if not code:
            raise ValueError("insert code")
        if not prefix:
            raise ValueError("insert prefix")
        pattern = rf'\b{re.escape(prefix)}\w*'
        matches = re.findall(pattern, code,flags=re.IGNORECASE)
        return matches


    def contains(self, data):
        if not self.code:
            raise ValueError("Insert code")

        if not data:  # Verifica si el dato está vacío
            raise ValueError("Data cannot be empty")

        pattern = r'\w*(?:' + re.escape(data) + r')\w*'

        matches = re.findall(pattern, self.code,flags=re.IGNORECASE)

    

        return matches


    def get_dates(self, text:str):
        
        if text is None:
            return "Error: The parameter provided is None."
        if not isinstance(text, str):
            return "Error: The parameter provided is not a valid text string."
        
        if not text.strip(): 
            return "The text provided is empty or null."

        # Expresiones regulares para formatos diferentes
        patterns = [
            r"\b(\d{4})[-/](\d{2})[-/](\d{2})\b",  # YYYY-MM-DD o YYYY/MM/DD
            r"\b(\d{2})[-/](\d{2})[-/](\d{4})\b",  # DD-MM-YYYY o DD/MM/YYYY
        ]

        matches = []
        for pattern in patterns:
            matches.extend(re.findall(pattern, text))
    

        if not matches:
            return "No dates found in the text."

        for match in matches:
            
            if len(match[0]) == 4:  # YYYY-MM-DD
                year_val, month_val, day_val = map(int, match)
            else:  # DD-MM-YYYY
                day_val, month_val, year_val = map(int, match)

            # Validación del año
            if not (1900 <= year_val <= 2100):
                print(f"La fecha {day_val:02d}-{month_val:02d}-{year_val} tiene un año fuera del rango permitido (1900-2100).")
                

            # Validación del mes
            if not (1 <= month_val <= 12):
                print(f"La fecha {day_val:02d}-{month_val:02d}-{year_val} tiene un mes inválido.")
                

            # Validación del día
            if not (1 <= day_val <= 31):
                print(f"La fecha {day_val:02d}-{month_val:02d}-{year_val} tiene un día inválido.")
                

            # Verifica meses con 30 días
            if month_val in {4, 6, 9, 11} and day_val > 30:
                print(f"La fecha {day_val:02d}-{month_val:02d}-{year_val} tiene más de 30 días en un mes que solo permite 30 días.")
                

            # Verifica febrero
            if month_val == 2:
                if (year_val % 4 == 0 and year_val % 100 != 0) or (year_val % 400 == 0):  # Año bisiesto
                    if day_val > 29:
                        print(f"La fecha {day_val:02d}-{month_val:02d}-{year_val} tiene más de 29 días en un año bisiesto.")
                        
                else:
                    if day_val > 28:
                        print(f"La fecha {day_val:02d}-{month_val:02d}-{year_val} tiene más de 28 días en un año no bisiesto.")
                        

            # Si es válida, la añade a la lista en formato estándar YYYY/MM/DD
            valid_date = f"{year_val:04d}/{month_val:02d}/{day_val:02d}"
            self.list_date.append(valid_date)

        return self.list_date
        
    def get_phone(self, text: str = ""):
        patterns = [
        r'\+?\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{2,4}[-.\s]?\d{2,4}'
        ]
        phone_numbers = []
        for pattern in patterns:
            matches = re.findall(pattern, text)
        for match in matches:
            prefix = "+" if match.startswith("+") else ""
            normalized_number = prefix + re.sub(r'\D', '', match)
            phone_numbers.append(normalized_number)
        return phone_numbers
    
    def get_email(self, text: str = ""):
        if not text:
            raise ValueError("insert text")
        
        patterns =  r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(patterns, text)
        return emails
        
        
        

    
