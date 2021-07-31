import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file1 = "conjunto_de_datos_defunciones_registradas_2019.CSV"
#head = ['ent_regis', 'mun_regis', 'ent_resid', 'mun_resid', 'tloc_resid', 'loc_resid', 'ent_ocurr', 'mun_ocurr', 'tloc_ocurr', 'loc_ocurr', 'causa_def', 'lista_mex', 'sexo', 'edad', 'dia_ocurr', 'mes_ocurr', 'anio_ocur', 'dia_regis', 'mes_regis', 'anio_regis', 'dia_nacim', 'mes_nacim', 'anio_nacim', 'ocupacion', 'escolarida', 'edo_civil', 'presunto', 'ocurr_trab', 'lugar_ocur', 'necropsia', 'asist_medi', 'sitio_ocur', 'cond_cert', 'nacionalid', 'derechohab', 'embarazo', 'rel_emba', 'horas', 'minutos', 'capitulo', 'grupo', 'lista1', 'gr_lismex', 'vio_fami', 'area_ur', 'edad_agru', 'complicaro', 'dia_cert', 'mes_cert', 'anio_cert', 'maternas', 'lengua', 'cond_act', 'par_agre', 'ent_ocules', 'mun_ocules', 'loc_ocules', 'razon_m', 'dis_re_oax']


#datos = pd.read_csv(file1,nrows=10000)
datos = pd.read_csv(file1)


# Tabla con info de edad y causa de defunción
dat_enf = pd.DataFrame(datos, columns = ['lista_mex','ent_regis','sexo','edad'])


# 06H -> VIH
dat_vih = dat_enf[(dat_enf['lista_mex']=='06H')]
dat_muj = dat_vih[(dat_vih['sexo']==2)]
dat_hom = dat_vih[(dat_vih['sexo']==1)]


# Crea tabla con info de "ent_reg" y "edad" para fallecidos por vih, hombres y mujeres
vih_muj =  pd.DataFrame(dat_muj, columns = ['ent_regis','edad'])
vih_hom =  pd.DataFrame(dat_hom, columns = ['ent_regis','edad'])

# ignora entradas que no especifican edad
vih_muj = vih_muj[(vih_muj['edad'] != 4998)]
vih_hom = vih_hom[(vih_hom['edad'] != 4998)]




###############################################################################
# Crea tablas para hom y muj con "entidad de registro de fallecimiento por vih"

# mujeres
ent_muj = pd.DataFrame(vih_muj, columns = ['ent_regis']).to_numpy().flatten()
unique, counts = np.unique(ent_muj, return_counts=True)
x = dict(zip(unique, counts))
xm = {k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse=True)[:5]}
#xxm = {k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse=True)}


# hombres
ent_hom = pd.DataFrame(vih_hom, columns = ['ent_regis']).to_numpy().flatten()
unique, counts = np.unique(ent_hom, return_counts=True)
x = dict(zip(unique, counts))
xh = {k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse=True)[:5]}
#xxh = {k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse=True)}


print('Top 5 entidades por no. fallecimientos por VIH [entidad : no. fallecimientos] ')
print()
print('Mujeres : ',xm)
print('Hombres : ',xh)
print()
print()

# OUT

# Top 5 entidades por no. fallecimientos por VIH [entidad : no. fallecimientos]

# Mujeres :  {30: 134, 2: 77, 9: 65, 7: 62, 14: 56}
# Hombres :  {30: 565, 9: 470, 14: 321, 15: 318, 2: 239}

# 30 -> Veracruz



###############################################################################
# Crea tablas para hom y muj con "edad fallecimiento por vih"

# mujeres
edad_muj = pd.DataFrame(vih_muj, columns = ['edad']).to_numpy().flatten()
aa = np.array([x-4000 if x > 4000 else 1  for x in edad_muj])
unique, counts = np.unique(aa, return_counts=True)
x = dict(zip(unique, counts))
xm = {k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse=True)}

Edad_muj = aa.sum() / aa.size


# hombres
edad_hom = pd.DataFrame(vih_hom, columns = ['edad']).to_numpy().flatten()
aa = np.array([x-4000 if x > 4000 else 1  for x in edad_hom])
unique, counts = np.unique(aa, return_counts=True)
x = dict(zip(unique, counts))
xh = {k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse=True)}

Edad_hom = aa.sum() / aa.size

print('Edad promedio de fallecidos por VIH (años):')
print('Hombres : ', round(Edad_hom,2))
print('Mujeres : ', round(Edad_muj,2))
print()



plt.bar(list(xh.keys()), xh.values(), color='b')
plt.bar(list(xm.keys()), xm.values(), color='r')

plt.legend(["Hombres", "Mujeres"], loc ="upper right")

plt.xlabel("Edad (años)")
plt.ylabel("No. de defunciones por VIH")



plt.show()






