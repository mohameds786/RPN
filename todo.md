# RPN
Ce projet consiste en une calculatrice RPN

## Différentes parties
Un Front End développé en Angular
Un Back En développé en Python avec Flask

## Fonctionnalités réalisées
*GET /rpn/op:* Récupérer les opérandes (+, -, /, *) <br/>
*POST /rpn/op/{op_id}/stack/{stack_id}:* Appliquer une opération sur une stack <br/>
*POST /rpn/stack:* Créer une nouvelle stack <br/>
*GET /rpn/stack:* Récupérer la liste des stack_ids <br/>
*DELETE /rpn/stack/{stack_id}:* Supprimer une stack <br/>
*POST /rpn/stack/{stack_id}:* Ajouter la valeur à la stack <br/>
*GET /rpn/stack/{stack_id}:* Récupérer la stack <br/>

## To Do
- Utilisation de float pour les nombres relatifs
- Améliorer la gestion des erreurs (id inexistant, liste vide, ...): utiliser des exceptions plutôt que de simples print
- Améliorer le style de la page
- Gérer une actualisation automatique des données affichées quand une action est effectuée 
- Structuration des API en blueprint pour les regrouper selon le début du path
- Amélioration du code (choix des variables, utilisations de fonctions, ...)
- Ajouter les codes HTTP dans les retours des opérations


