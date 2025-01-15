# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
    GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys
from traceback import print_exception
from pyparsing import*
import json

base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path, 'modules','regex', 'libs')

if cur_path not in sys.path:
    sys.path.append(cur_path)

from _regex import Regex


"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

if module == "start_with": 
    data = GetParams("data")
    text = GetParams("text")
    result_var = GetParams("result") 
    
    

    try:
        regex= Regex(text)
        result = regex.start_with(text,data)
        if result is not None and result != "":
            SetVar(result_var,result)
        else:
            SetVar(result_var,"No matches")
            

    except Exception as e:
        print_exception(e)  
        SetVar(result_var,"Error")
        raise e

    

if module == "contains": 
    data = GetParams("data")
    text = GetParams("text")
    result_var = GetParams("result") 
    
    

    try:
        regex= Regex(text)
        result = regex.contains(data)
        if result is not None and result != "":
            SetVar(result_var,result)
        else:
            SetVar(result_var,"No matches")
            

    except Exception as e:
        print_exception(e)  
        SetVar(result_var,"Error")
        raise e

if module == "get_dates": 
    text = GetParams("text")
    result_var = GetParams("result") 
    
    

    try:
        regex= Regex(text)
        result = regex.get_dates(text)
        if result is not None and result != "":
            SetVar(result_var,result)
        else:
            SetVar(result_var,"No matches")
            

    except Exception as e:
        print_exception(e)  
        SetVar(result_var,"Error")
        raise e

if module == "get_phone": 
    text = GetParams("text")
    result_var = GetParams("result") 
    
    

    try:
        regex= Regex(text)
        result = regex.get_phone(text)
        if result is not None and result != "":
            SetVar(result_var,result)
        else:
            SetVar(result_var,"No matches")
            

    except Exception as e:
        print_exception(e)  
        SetVar(result_var,"Error")
        raise e

if module == "get_email": 
    text = GetParams("text")
    result_var = GetParams("result") 
    
    

    try:
        regex= Regex(text)
        result = regex.get_email(text)
        if result is not None and result != "":
            SetVar(result_var,result)
        else:
            SetVar(result_var,"No matches")
            

    except Exception as e:
        print_exception(e)  
        SetVar(result_var,"Error")
        raise e

























        
""" De la linea 67 van los codigos de HTML hacia abajo"""

#     if module == "listToTable":
#         """
#         List to regex Table: convert a list to a regex format table
#         """
#         var_ = GetParams('result')
#         list = GetParams('list')
#         res = None
        
#         try:
#             list = eval(list)
#             regex_table = regex.list_to_table(list)
            
#         except Exception as e:
#             PrintException()
#             raise e
        
#         if var_:
#             res = regex_table
#             SetVar(var_, res)

#     if module == "tableToList":
#         """
#         regex Table to List: convert a regex format table to a list
#         """
#         var_ = GetParams('result')
#         table = GetParams('table')
#         res = None
        
#         try:
            
#             regex_list = regex.table_to_list(table)
            
#         except Exception as e:
#             PrintException()
#             raise e
        
#         if var_:
#             res = regex_list
#             SetVar(var_, res)

#     if module == 'saveregex':
#         path_save = GetParams('pathSave')
#         var_ = GetParams('result')
#         session = GetParams('session')
#         decode = GetParams('decode')

#         if not session:
#             session = SESSION_DEFAULT
        
#         if not decode:
#             decode = 'utf-8'

#         res = True
        
#         try:
#             regex = mod_regex_sessions[session]['regex']
#             regex.save_regex(path_save, decode)
            
#         except Exception as e:
#             PrintException()
#             res= False
#             raise e
        
#         if var_:
#             SetVar(var_, res)

# except Exception as e:
#     PrintException()
#     raise e


