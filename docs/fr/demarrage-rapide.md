# Premier Mouvement

Dans ce tutoriel, vous allez écrire votre premier script pour interagir avec le SDK Dexterous Hand.

## Comprendre le Mode Simulé (Mock Mode)

Avant de connecter le matériel physique, nous allons utiliser le **Mode Simulé (Mock Mode)**. L'interface mock du SDK crée une simulation logicielle de la main qui répond aux commandes de l'API de manière identique au matériel réel.

L'utilisation du mode simulé est cruciale pour plusieurs raisons :
1.  **Sécurité :** Il vous permet de tester la logique et les séquences de mouvement sans risquer d'endommager la main physique ou l'environnement immédiat.
2.  **Praticité :** Vous pouvez développer et déboguer du code n'importe où, même lorsque le matériel n'est pas disponible.
3.  **Vérification :** Il garantit que votre environnement logiciel est correctement configuré avant d'introduire les complexités liées au matériel.

## Le Code

Écrivons un script simple pour initialiser la main simulée et lire ses positions articulaires de départ. Créez un fichier nommé `premier_mouvement.py` et ajoutez le code suivant :

```python
# Importer la classe Hand depuis le SDK
from dexterous_hand import Hand

# Initialiser une instance de main simulée. Cela se connecte à un pilote
# simulé en utilisant la configuration articulaire par défaut.
hand = Hand.mock()

# Lire l'état actuel de toutes les articulations depuis le pilote simulé
joints = hand.read_joints()

# Itérer à travers les états articulaires retournés et afficher leurs noms et positions
for joint in joints:
    print(f"Articulation : {joint.name}, Position : {joint.position_rad} rad")
```

Exécutez le script :

```bash
python premier_mouvement.py
```

## Comprendre le Résultat

Lorsque vous exécutez le script, vous devriez voir un résultat similaire à celui-ci :

```text
Articulation : thumb_flex, Position : 0.0 rad
Articulation : index_flex, Position : 0.0 rad
Articulation : middle_flex, Position : 0.0 rad
Articulation : ring_flex, Position : 0.0 rad
Articulation : little_flex, Position : 0.0 rad
```

*   **Articulation :** Cela identifie le point d'articulation spécifique sur la main. Par défaut, le pilote simulé initialise cinq articulations représentant les axes de flexion principaux du pouce, de l'index, du majeur, de l'annulaire et de l'auriculaire.
*   **Position :** Il s'agit de l'angle actuel de l'articulation, mesuré en radians (`rad`). Parce que nous venons d'initialiser la main simulée et que nous n'avons commandé aucun mouvement, toutes les positions sont à `0.0`, ce qui représente une pose neutre et ouverte.

## Prochaines Étapes

Maintenant que vous avez initialisé la main et lu son état avec succès, vous êtes prêt à commander des mouvements. Consultez le guide de configuration matérielle pour connecter votre Linkerbot, ou continuez à explorer le SDK avec le tutoriel sur les séquences de saisie.
