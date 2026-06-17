# Foire Aux Questions (FAQ)

**1. Qu'est-ce que le SDK Dexterous Hand ?**
Le SDK Dexterous Hand est une bibliothèque Python fournie par Stonedrum Robotics pour contrôler et interagir avec la main dextre L20.

**2. Quelles versions de Python sont prises en charge ?**
Le SDK nécessite Python 3.10 ou une version plus récente (3.10, 3.11 et 3.12 sont testées en CI).

**3. Quels systèmes d'exploitation sont pris en charge ?**
Nous prenons officiellement en charge Ubuntu Linux et macOS. Windows est pris en charge via WSL2.

**4. Quelles distributions ROS 2 sont compatibles ?**
Nous prenons actuellement en charge ROS 2 Humble (Ubuntu 22.04) et ROS 2 Jazzy (Ubuntu 24.04).

**5. Puis-je utiliser le SDK sans ROS 2 ?**
Oui, le paquet Python de base `dexterous_hand` est totalement indépendant de ROS 2 et peut être utilisé de manière autonome.

**6. Puis-je simuler la main sans le matériel physique ?**
Oui. Vous pouvez utiliser le mode Mock intégré pour tester le logiciel, ou utiliser nos modèles URDF fournis dans des simulateurs comme Gazebo ou MuJoCo.

**7. Comment activer le mode Mock ?**
Il suffit d'initialiser la main en utilisant la méthode d'usine mock : `hand = Hand.mock()`. Cela ne nécessite aucune connexion physique.

**8. Comment définir une posture de préhension personnalisée ?**
Vous pouvez instancier un objet `GraspPose` avec les angles d'articulation souhaités et passer le dictionnaire `joint_positions_rad` directement à `hand.move_joints()`.

**9. Quels sont les noms d'articulation standardisés ?**
Les 5 articulations principales utilisées dans le SDK sont `thumb_flex`, `index_flex`, `middle_flex`, `ring_flex` et `little_flex`.

**10. MoveIt 2 est-il pris en charge ?**
Les paquets de configuration MoveIt 2 sont en cours de développement et seront fournis dans une prochaine version pour permettre une planification de mouvement avancée.

**11. La main nécessite-t-elle un étalonnage manuel ?**
En fonctionnement normal, la main s'étalonne automatiquement au démarrage. L'étalonnage manuel n'est requis que si un actionneur est remplacé.

**12. Pourquoi une erreur `NotImplementedError` apparaît-elle dans `read_glove_frame` ?**
La téléopération via des gants de données est prévue pour une future mise à jour. La signature de la méthode existe mais n'est pas encore implémentée.

**13. Le matériel est-il certifié CE ?**
La certification CE est actuellement **en cours de vérification**. Pour plus de détails, veuillez contacter info@stonedrum.co.

**14. Comment signaler un bug ou demander une fonctionnalité ?**
Veuillez utiliser l'outil de suivi des problèmes GitHub (Issues) sur notre dépôt pour signaler des bugs ou soumettre des demandes de fonctionnalités.

**15. Qui contacter pour des questions commerciales ?**
Pour le support aux entreprises, les prix de gros ou les questions commerciales générales, veuillez contacter Stonedrum Robotics à l'adresse info@stonedrum.co.
