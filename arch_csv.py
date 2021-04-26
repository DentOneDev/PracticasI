#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

# leer un archivo csv con python
resultado = pd.read_csv('datos.csv')
print(resultado)

# escribir un archivo csv con python
archivo = pd.DataFrame([['Sacramento', 'California','No', '1.743 Million'],['Miami', 'Florida','Yes','1.303 Million']], columns=['City', 'State', 'Capital', 'Population'])
archivo.to_csv('datos.csv')

