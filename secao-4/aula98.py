import importlib
import aula98m # Importação de módulos são singleton, são únicos, não ocorrem uma segunda vez

for i in range(10):
    importlib.reload(aula98m)