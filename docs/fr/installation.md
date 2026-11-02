# Préparer les sources

Utilisez les sources publiques du SDK sans supposer la disponibilité d'un paquet sur un registre :

```bash
git clone https://github.com/stonedrum-robotics/dexterous-hand-sdk.git
cd dexterous-hand-sdk
git checkout 17d8768affe743e9f997f1df5b100ea782ee5526
```

Depuis ce répertoire, le [premier exemple en mémoire](demarrage-rapide.md) importe le paquet situé à la racine avec `PYTHONPATH=.`. Aucun appareil ni environnement ROS n'est nécessaire pour cet exemple.

Le projet déclare Python `>=3.10`. Les vérifications locales enregistrées couvrent Python3.11 et3.12 ; la CI de la PR corrective a réussi sur Python3.11. Cela ne démontre pas une compatibilité testée pour tous les systèmes, toutes les versions déclarées de Python ou les distributions ROS.

Pour développer le SDK dans un environnement virtuel, `python -m pip install -e ".[dev]"` installe les dépendances déclarées dans `pyproject.toml`. L'installation et ses dépendances doivent être vérifiées dans l'environnement choisi. ROS, Docker, MoveIt et MuJoCo ont leurs propres besoins et ne sont pas validés par le simple exemple Python.
