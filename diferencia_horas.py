import pandas as pd
import numpy as np
from datetime import timedelta 
import calendar


list_rangos = []

def ultimo_dia_del_mes(anio, mes):
    # La función monthrange() devuelve el primer día de la semana y el último día del mes
    _, ultimo_dia = calendar.monthrange(anio, mes)
    return ultimo_dia

def genera_fechas(p_fecha_inicio,p_fecha_fin,p_anotacion,p_ducto,p_id_sitrac):
        #rango = pd.date_range(p_fecha_inicio.replace(hour=0,minute=0,second=0),p_fecha_fin)
        rango = pd.date_range(p_fecha_inicio.date(),p_fecha_fin.date())
        ran_idx_max = len(rango)-1
        if p_ducto =='Oleoducto 30"-24"/20" Nuevo Teapa-Tula -Salamanca':
            pass
        if len(rango)==1:
            list_rangos.append([p_fecha_inicio,p_fecha_fin,p_anotacion,p_ducto,p_id_sitrac])
        else:
            # rango = pd.date_range(p_fecha_inicio,p_fecha_fin+timedelta(days=1))
            for idx, f in enumerate(rango):
                fecha_rango = f
            
                if idx == 0:
                    list_rangos.append([p_fecha_inicio,fecha_rango.replace(hour=23,minute=59,second=59),p_anotacion,p_ducto,p_id_sitrac])
                elif idx < ran_idx_max:
                    list_rangos.append([fecha_rango.replace(hour=0,minute=0,second=0),fecha_rango.replace(hour=23,minute=59,second=59),p_anotacion,p_ducto,p_id_sitrac])
                else:
                    list_rangos.append([fecha_rango.replace(hour=0,minute=0,second=0),p_fecha_fin,p_anotacion,p_ducto,p_id_sitrac])


def DiferenciaHoras(file):
    
    datos = pd.read_excel(file,header=0)
    datos = datos.rename(columns=lambda x: x.replace(' ',''))
    datos = datos.rename(columns=lambda x: x.upper())

    columnas_base = datos[['FECHA_INICIO','HORA_INICIO', 'ANOTACION', 'DETRACTOR', 'SISTEMA','ID_SITRAC']]

    datos_DETRACTOR = columnas_base[(columnas_base['DETRACTOR'].str.upper() == 'SI')]

    ductos_id = datos_DETRACTOR[['ID_SITRAC']].drop_duplicates().sort_values(by=['ID_SITRAC'],ascending=[False]).values.tolist()
    
    for d in ductos_id:
        
        datos_DUCTO = datos_DETRACTOR[(datos_DETRACTOR['ID_SITRAC'] == d[0])]
        
        datos_DUCTO = datos_DUCTO.sort_values(by=['FECHA_INICIO','HORA_INICIO'],ascending=[True,True])

        datos_DUCTO['ESTADO_SUSPENSION'] = np.where(datos_DUCTO['ANOTACION'].str.upper() == 'REANUDAR',"FIN_SUSPENDER","INICIO_SUSPENDER")
        
        list_horas = datos_DUCTO.values.tolist()

        # for line in list_horas:
        #     print(*line)

        idx_max = len(list_horas)-1

        for idx, i in enumerate(list_horas):
            v_fecha = i[0]
            v_hora = i[1]
            v_anotacion = i[2]
            v_ducto = i[4]
            v_id_sitrac = i[5]
            v_estado = i[6]

            if idx < idx_max:
                sigui_fecha = list_horas[idx+1][0]
                sigui_hora = list_horas[idx+1][1]
                sigui_estado = list_horas[idx+1][6]
                sigui_anotacion = list_horas[idx+1][2]

            if idx == 0:
                if v_estado=='FIN_SUSPENDER':
                    fecha_inicio = v_fecha.replace(hour=0, minute=0, second=0, microsecond=0)
                    fecha_fin = v_fecha.replace(hour=v_hora.hour, minute=v_hora.minute, second=v_hora.second, microsecond=0)
                    
                    genera_fechas(fecha_inicio,fecha_fin,v_anotacion,v_ducto,v_id_sitrac)
                    
                    fecha_fin = fecha_inicio - timedelta(seconds=1)
                    fecha_inicio = v_fecha.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                    
                    genera_fechas(fecha_inicio,fecha_fin,"SUSPENDE (Motivo desconocido)",v_ducto,v_id_sitrac)
                
                if v_estado == 'INICIO_SUSPENDER':
                    fecha_inicio = v_fecha.replace(hour=v_hora.hour, minute=v_hora.minute, second=v_hora.second, microsecond=0)
                    if sigui_estado =='INICIO_SUSPENDER':
                        fecha_fin = fecha_inicio - timedelta(seconds=1)
                    else:
                        fecha_fin = sigui_fecha.replace(hour=sigui_hora.hour, minute=sigui_hora.minute, second=sigui_hora.second)
                
                    genera_fechas(fecha_inicio,fecha_fin,v_anotacion,v_ducto,v_id_sitrac)
                
            else:
              
                if v_estado == 'INICIO_SUSPENDER':
                    fecha_inicio = v_fecha.replace(hour=v_hora.hour, minute=v_hora.minute, second=v_hora.second)
                    
                    if sigui_estado =='INICIO_SUSPENDER':
                        if idx == idx_max:
                            ultimo_dia = ultimo_dia_del_mes(v_fecha.year,v_fecha.month)
                            fecha_fin = v_fecha.replace(day=ultimo_dia,hour=23, minute=59, second=59)
                        else:
                            fecha_fin = sigui_fecha.replace(hour=sigui_hora.hour, minute=sigui_hora.minute, second=sigui_hora.second) - timedelta(seconds=1)
                    else:
                        fecha_fin = sigui_fecha.replace(hour=sigui_hora.hour, minute=sigui_hora.minute, second=sigui_hora.second)

                    genera_fechas(fecha_inicio,fecha_fin,v_anotacion,v_ducto,v_id_sitrac)
                    

    df = pd.DataFrame(list_rangos,columns=['FECHA_INI','FECHA_FIN','ANOTACION', 'DUCTO','ID_SITRAC']).sort_values(by=['ID_SITRAC','FECHA_INI','FECHA_FIN'])
    df['HORAS_SUSPENDIDO'] = (df['FECHA_FIN'] - df['FECHA_INI']).dt.total_seconds()/3600
    
    list_rangos.clear()
    
    return df

# DiferenciaHoras(file='BE_MARMAY2023.xlsx')
