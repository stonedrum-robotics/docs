# Démarrage Rapide

Ce guide vous permet de lancer votre premier mouvement en moins de 5 minutes.

Exécutez ce script Python :

```python
from dexterous_hand import Hand

def main():
    hand = Hand.mock()
    hand.move_joints({"thumb_flex": 0.3, "index_flex": 0.4})
    for state in hand.read_joints():
        print(f"{state.name}: {state.position_rad:.2f} rad")

if __name__ == "__main__":
    main()
```
