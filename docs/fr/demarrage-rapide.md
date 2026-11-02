# Premier exemple en mémoire

Après la [préparation des sources](installation.md), lancez cet exemple depuis le répertoire du SDK fixé au commit `17d8768affe743e9f997f1df5b100ea782ee5526` :

```bash
PYTHONPATH=. python3 - <<'PYTHON'
from dexterous_hand import Hand

hand = Hand.mock()
hand.move_joints({"thumb_flex": 0.25, "index_flex": 0.4})
for state in hand.read_joints():
    print(f"{state.name}: {state.position_rad:.2f} rad")
hand.open()
hand.stop()
PYTHON
```

Sortie attendue :

```text
thumb_flex: 0.25 rad
index_flex: 0.40 rad
middle_flex: 0.00 rad
ring_flex: 0.00 rad
little_flex: 0.00 rad
```

`Hand.mock()` conserve cinq positions en mémoire. `move_joints()` modifie les valeurs indiquées et `read_joints()` renvoie cet état logiciel. `open()` demande des cibles nulles pour les articulations déclarées. `stop()` ne réalise aucune action physique dans ce backend.

Cet exemple ne commande aucun appareil et ne simule ni contact, ni collision, ni dynamique. Les adaptateurs matériels actuels refusent les opérations non prises en charge avec `NotImplementedError` avant toute communication. Un changement de constructeur ne fournit donc pas une intégration matérielle. Le SDK ne fournit pas de fonction d'arrêt d'urgence physique validée.
