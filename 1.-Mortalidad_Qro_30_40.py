import pandas as pd
import numpy as np




file1 = "conjunto_de_datos_defunciones_registradas_2019.CSV"

#head = ['ent_regis', 'mun_regis', 'ent_resid', 'mun_resid', 'tloc_resid', 'loc_resid', 'ent_ocurr', 'mun_ocurr', 'tloc_ocurr', 'loc_ocurr', 'causa_def', 'lista_mex', 'sexo', 'edad', 'dia_ocurr', 'mes_ocurr', 'anio_ocur', 'dia_regis', 'mes_regis', 'anio_regis', 'dia_nacim', 'mes_nacim', 'anio_nacim', 'ocupacion', 'escolarida', 'edo_civil', 'presunto', 'ocurr_trab', 'lugar_ocur', 'necropsia', 'asist_medi', 'sitio_ocur', 'cond_cert', 'nacionalid', 'derechohab', 'embarazo', 'rel_emba', 'horas', 'minutos', 'capitulo', 'grupo', 'lista1', 'gr_lismex', 'vio_fami', 'area_ur', 'edad_agru', 'complicaro', 'dia_cert', 'mes_cert', 'anio_cert', 'maternas', 'lengua', 'cond_act', 'par_agre', 'ent_ocules', 'mun_ocules', 'loc_ocules', 'razon_m', 'dis_re_oax']


#datos = pd.read_csv(file1,nrows=100000)
datos = pd.read_csv(file1)


# Crea la tabla que contiene todos los datos de las defunciones en Qro con edades entre 30 y 40 
# Clave "22" = Queretaro
dat_30_40 = datos[(datos['edad']>4029) & (datos['edad']<4041) & (datos['ent_regis'] == 22 ) ]
dat_30_40.to_csv('Mortalidad_Qro_30_40.csv',index = False)


# Crea la tabla que contiene entidad y municipio de residencia de las defunciones en Qro con edades entre 30 y 40
dat_ent = pd.DataFrame(dat_30_40, columns = ['ent_resid','mun_resid'])
#dat_ent.to_csv('Mortalidad_Qro_30_40_resid.csv',index = False)



# Imprime el diccionario con {'entidad de residencia' : 'no_defunciones'} para las defunciones en Qro con edades entre 30 y 40
dat_ent = pd.DataFrame(dat_ent, columns = ['ent_resid'])
unique, counts = np.unique(dat_ent, return_counts=True)
x = dict(zip(unique, counts))
xx = {k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse=True)}


print('Entidades donde residen los fallecidos en Qro con edades entre 30 y 40 años:')
print()
print(xx)




