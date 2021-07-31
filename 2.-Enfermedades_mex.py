import pandas as pd
import numpy as np




file1 = "conjunto_de_datos_defunciones_registradas_2019.CSV"

#head = ['ent_regis', 'mun_regis', 'ent_resid', 'mun_resid', 'tloc_resid', 'loc_resid', 'ent_ocurr', 'mun_ocurr', 'tloc_ocurr', 'loc_ocurr', 'causa_def', 'lista_mex', 'sexo', 'edad', 'dia_ocurr', 'mes_ocurr', 'anio_ocur', 'dia_regis', 'mes_regis', 'anio_regis', 'dia_nacim', 'mes_nacim', 'anio_nacim', 'ocupacion', 'escolarida', 'edo_civil', 'presunto', 'ocurr_trab', 'lugar_ocur', 'necropsia', 'asist_medi', 'sitio_ocur', 'cond_cert', 'nacionalid', 'derechohab', 'embarazo', 'rel_emba', 'horas', 'minutos', 'capitulo', 'grupo', 'lista1', 'gr_lismex', 'vio_fami', 'area_ur', 'edad_agru', 'complicaro', 'dia_cert', 'mes_cert', 'anio_cert', 'maternas', 'lengua', 'cond_act', 'par_agre', 'ent_ocules', 'mun_ocules', 'loc_ocules', 'razon_m', 'dis_re_oax']


#datos = pd.read_csv(file1,nrows=10000)
datos = pd.read_csv(file1)

#dat_enf = pd.DataFrame(datos, columns = ['lista_mex','edad_agru'])
dat_enf0 = pd.DataFrame(datos, columns = ['lista_mex'])


# Cuenta de mayor a menor las causas de defuncion en México
unique, counts = np.unique(dat_enf0, return_counts=True)
x = dict(zip(unique, counts))

# Ordena y muestra las 5 causas con mayor número de fallecidos
xx = {k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse=True)[:5]}
print('Top 5 causas de muerte en MX : ',xx)

# {'28A': 105210, '20D': 104354, '55': 36661, '33B': 30327, '35M': 26169}

# 28A Infarto agudo del miocardio
# 20D Diabetes mellitus
# 55 Agresiones (homicidios)
# 33B Neumonía
# 35M Otras enfermedades del hígado


# Tabla con info de edad y causa de defunción
dat_enf1 = pd.DataFrame(datos, columns = ['lista_mex','edad'])


# 28A
dat_28a = dat_enf1[(dat_enf1['lista_mex']=='28A')]
dat_28a = pd.DataFrame(dat_28a, columns = ['edad']).to_numpy().flatten()

# No consideramos los casos que no especifican edad
aa = np.array([x for x in dat_28a if (x != 4998) ])

# A los menores de 1 año, les asignamos edad de 1 año, por simplicidad.
aa = np.array([x-4000 if (x > 4000) else 1 for x in aa])
Edad_prom_28a = aa.sum() / aa.size



# 20D
dat_20d = dat_enf1[(dat_enf1['lista_mex']=='20D')]
dat_20d = pd.DataFrame(dat_20d, columns = ['edad']).to_numpy().flatten()
aa = np.array([x for x in dat_20d if (x != 4998) ])
aa = np.array([x-4000 if x > 4000 else 1  for x in aa])
Edad_prom_20d = aa.sum() / aa.size


# 55
dat_55 = dat_enf1[(dat_enf1['lista_mex']=='55')]
dat_55 = pd.DataFrame(dat_55, columns = ['edad']).to_numpy().flatten()
aa = np.array([x for x in dat_55 if (x != 4998) ])
aa = np.array([x-4000 if x > 4000 else 1  for x in aa])
Edad_prom_55 = aa.sum() / aa.size


# 33B
dat_33b = dat_enf1[(dat_enf1['lista_mex']=='33B')]
dat_33b = pd.DataFrame(dat_33b, columns = ['edad']).to_numpy().flatten()
aa = np.array([x for x in dat_33b if (x != 4998) ])
aa = np.array([x-4000 if x > 4000 else 1  for x in aa])
Edad_prom_33B = aa.sum() / aa.size


# 35M
dat_35m = dat_enf1[(dat_enf1['lista_mex']=='35M')]
dat_35m = pd.DataFrame(dat_35m, columns = ['edad']).to_numpy().flatten()
aa = np.array([x for x in dat_35m if (x != 4998) ])
aa = np.array([x-4000 if x > 4000 else 1  for x in aa])
Edad_prom_35M = aa.sum() / aa.size





print('Edad prom 28A (años) : ', round(Edad_prom_28a,2))
print('Edad prom 20D (años) : ', round(Edad_prom_20d,2))
print('Edad prom 55 (años) : ',  round(Edad_prom_55,2))
print('Edad prom 33B (años) : ', round(Edad_prom_33B,2))
print('Edad prom 35M (años) : ', round(Edad_prom_35M,2))



# Output: 
# Edad prom 28A (años) :  74.93
# Edad prom 20D (años) :  68.16
# Edad prom 55 (años) :  34.71
# Edad prom 33B (años) :  68.2
# Edad prom 35M (años) :  62.06







