import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




file1 = "conjunto_de_datos_defunciones_registradas_2019.CSV"

#head = ['ent_regis', 'mun_regis', 'ent_resid', 'mun_resid', 'tloc_resid', 'loc_resid', 'ent_ocurr', 'mun_ocurr', 'tloc_ocurr', 'loc_ocurr', 'causa_def', 'lista_mex', 'sexo', 'edad', 'dia_ocurr', 'mes_ocurr', 'anio_ocur', 'dia_regis', 'mes_regis', 'anio_regis', 'dia_nacim', 'mes_nacim', 'anio_nacim', 'ocupacion', 'escolarida', 'edo_civil', 'presunto', 'ocurr_trab', 'lugar_ocur', 'necropsia', 'asist_medi', 'sitio_ocur', 'cond_cert', 'nacionalid', 'derechohab', 'embarazo', 'rel_emba', 'horas', 'minutos', 'capitulo', 'grupo', 'lista1', 'gr_lismex', 'vio_fami', 'area_ur', 'edad_agru', 'complicaro', 'dia_cert', 'mes_cert', 'anio_cert', 'maternas', 'lengua', 'cond_act', 'par_agre', 'ent_ocules', 'mun_ocules', 'loc_ocules', 'razon_m', 'dis_re_oax']


#datos = pd.read_csv(file1,nrows=10000)
datos = pd.read_csv(file1)



# Tabla con info de edad y causa de defunción
dat_enf1 = pd.DataFrame(datos, columns = ['lista_mex','edad'])


# 28A
dat_20d = dat_enf1[(dat_enf1['lista_mex']=='20D')]
dat_20d = pd.DataFrame(dat_20d, columns = ['edad']).to_numpy().flatten()

# No consideramos los casos que no especifican edad
aa = np.array([x for x in dat_20d if (x != 4998) ])

# A los menores de 1 año, les asignamos edad de 1 año, por simplicidad.
aa = np.array([x-4000 if x > 4000 else 1  for x in aa])
unique, counts = np.unique(aa, return_counts=True)


# Crea el diccionario con {'edad' : 'no_defunciones'} para las defunciones causadas por 20D "diabetes"
x = dict(zip(unique, counts))
x1 = {k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse=True)[:5]}
xx = {k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse=True)}


print('Top 5 de edades con mayor no. de muertes por diabetes : ',x1)
print()

# out:  {71: 2843, 68: 2834, 69: 2803, 64: 2783, 65: 2776}
# Edad prom 20D (años) :  68.16


plt.bar(list(xx.keys()), xx.values(), color='b')

plt.xlabel("Edad (años)")
plt.ylabel("No. de defunciones por diabetes")



plt.show()


