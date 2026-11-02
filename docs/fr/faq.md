# Foire aux questions

## Que peut-on utiliser sans matériel ?

`Hand.mock()` conserve cinq positions articulaires logicielles. Le [premier exemple](demarrage-rapide.md) montre les commandes et les valeurs retournées ; il ne simule pas le contact et ne prouve pas le comportement d'un appareil.

## Peut-on remplacer le mock par une main physique ?

Les adaptateurs Linkerbot/OmniHand actuels refusent les opérations non prises en charge avant toute communication. Un changement de constructeur ne crée pas de pilote fonctionnel. `Hand.stop()` n'est pas une fonction d'arrêt d'urgence physique implémentée.

## Quels environnements ont été vérifiés ?

Les résultats locaux enregistrés couvrent Python3.11/3.12 ; la CI de la PR corrective a réussi sur Python3.11. Cela ne valide pas tous les systèmes, versions déclarées, distributions ROS, images Docker, configurations MoveIt ou modèles MuJoCo.

## Combien de poses sont décrites ?

Neuf ensembles de cibles principaux et trois entrées de compatibilité. `open` contient un dictionnaire vide et ne correspond pas à `relaxed_open`. `Hand.open()` est une méthode distincte qui demande des cibles nulles.

## Existe-t-il une lecture de gant ou un service de données ?

La lecture de gant n'est pas implémentée dans le contrôleur et l'exemple applique une trame prédéfinie. La page [données d'entraînement](donnees-entrainement.md) n'annonce aucun service, jeu de données, calendrier ou garantie de conformité.

## Comment poser une question ?

Utilisez [les Issues du SDK](https://github.com/stonedrum-robotics/dexterous-hand-sdk/issues) pour un problème reproductible et expurgé. Discussions n'est pas activé. Envoyez les rapports sensibles en privé à [info@stonedrum.co](mailto:info@stonedrum.co). Aucun délai de réponse, SLA, service de support ou statut de conformité matérielle n'est promis ici.
