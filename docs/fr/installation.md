# Installation

Ce guide détaille toutes les étapes nécessaires pour installer le SDK Dexterous Hand et l'intégrer à votre environnement de développement.

## Prérequis

Avant d'installer le SDK, assurez-vous que votre système répond aux exigences suivantes :

*   **Système d'exploitation :** Ubuntu 22.04 LTS ou Ubuntu 24.04 LTS.
*   **Python :** Python 3.10 ou supérieur.
*   **ROS2 (Optionnel mais recommandé) :** ROS2 Humble Hawksbill (pour Ubuntu 22.04) ou ROS2 Jazzy Jalisco (pour Ubuntu 24.04).

## Installation Standard via Python

Si vous souhaitez simplement utiliser le SDK sans modifier son code source, vous pouvez l'installer directement via `pip`.

```bash
pip install dexterous-hand
```

*Résultat attendu :*
```text
Successfully installed dexterous-hand-x.y.z
```

## Installation pour le Développement

Si vous prévoyez de contribuer au SDK ou de modifier son comportement, nous recommandons une installation éditable. Cela vous permet de modifier le code et d'en voir les effets immédiatement sans avoir à le réinstaller.

1.  Clonez le dépôt :
    ```bash
    git clone https://github.com/stonedrum-robotics/dexterous-hand-sdk.git
    cd dexterous-hand-sdk
    ```
2.  Installez en mode éditable avec les dépendances de développement :
    ```bash
    pip install -e ".[dev]"
    ```

## Configuration de l'Espace de Travail ROS2

Pour utiliser le SDK dans un environnement ROS2, vous devez le compiler dans votre espace de travail colcon.

1.  Accédez au répertoire `src` de votre espace de travail ROS2 :
    ```bash
    cd ~/ros2_ws/src
    ```
2.  Clonez le dépôt :
    ```bash
    git clone https://github.com/stonedrum-robotics/dexterous-hand-sdk.git
    ```
3.  Compilez l'espace de travail :
    ```bash
    cd ~/ros2_ws
    colcon build --packages-select dexterous_hand
    ```
4.  Sourcez l'overlay :
    ```bash
    source install/setup.bash
    ```

## Installation avec Docker

Pour un environnement isolé, nous fournissons une image Docker basée sur `ros:humble-ros-base`. Elle inclut Python, colcon, et une version éditable du SDK préinstallée.

1.  Accédez au répertoire du SDK :
    ```bash
    cd dexterous-hand-sdk
    ```
2.  Construisez l'image Docker en utilisant le `docker/Dockerfile` fourni :
    ```bash
    docker build -t dexterous-hand-sdk -f docker/Dockerfile .
    ```
3.  Lancez le conteneur :
    ```bash
    docker run -it dexterous-hand-sdk
    ```

## Vérification de l'Installation

Pour confirmer que le SDK est correctement installé, exécutez un test rapide en utilisant l'interface simulée (mock) :

```bash
python -c "from dexterous_hand import Hand; print(Hand.mock())"
```

*Résultat attendu :*
```text
<dexterous_hand.hand.Hand object at 0x...>
```

## Résolution des Problèmes Courants

**Erreur :** `ModuleNotFoundError: No module named 'dexterous_hand'`
*   **Solution :** Assurez-vous d'avoir activé le bon environnement virtuel Python ou d'avoir sourcé votre espace de travail ROS2 (`source install/setup.bash`) où le SDK a été installé.

**Erreur :** `colcon: command not found`
*   **Solution :** Si vous compilez le paquet ROS2, vous devez installer le paquet `python3-colcon-common-extensions` via `apt`. Exécutez `sudo apt install python3-colcon-common-extensions`.

Besoin d'aide supplémentaire ? Contactez le support de Stonedrum Robotics à l'adresse info@stonedrum.co.
