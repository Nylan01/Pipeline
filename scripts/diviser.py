import os
import sys

nombre = float(sys.argv[1])
diviseur = int(sys.argv[2])

# Un nombre non entier ou impair arrête la pipeline
if not nombre.is_integer() or int(nombre) % 2 != 0:
    print(f"{sys.argv[1]} est impair : arrêt de la pipeline")
    sys.exit(1)

resultat = int(nombre) / diviseur
resultat = int(resultat) if resultat.is_integer() else resultat
print(f"{int(nombre)} / {diviseur} = {resultat}")

# Transmet le résultat au job suivant
if "GITHUB_OUTPUT" in os.environ:
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"resultat={resultat}\n")
