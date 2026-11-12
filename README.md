# dependency-extra-activation

## Français

Expliquer les dépendances conditionnelles par extra.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m dependency_extra_activation examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Expliquer les dépendances conditionnelles par extra : calcul déterministe sur entrées structurées, témoins et cas limites explicites.

### Limites

Modèle borné, données fictives, aucun service ou matériel de production validé. Méthodes classiques ; aucune supériorité SOTA générale ni adoption humaine démontrée.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Explain conditional dependencies activated by extras.

Synthetic data; no network access or secret required.

```sh
python -m dependency_extra_activation examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Explain conditional dependencies activated by extras: deterministic computation over structured inputs, explicit witnesses and boundary cases.

### Limits

Bounded model and synthetic data; no production service or hardware validated. Classical methods; no general SOTA superiority or human adoption demonstrated.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Explicar dependencias condicionales por extras.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m dependency_extra_activation examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Explicar dependencias condicionales por extras: cálculo determinista con entradas estructuradas, testigos y casos límite explícitos.

### Límites

Modelo acotado y datos ficticios; ningún servicio ni hardware de producción validado. Métodos clásicos; sin superioridad SOTA general ni adopción humana demostrada.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://packaging.python.org/en/latest/specifications/recording-installed-packages/
- https://git-scm.com/docs/git-worktree

## Projets voisins / Neighboring projects / Proyectos vecinos

FR : [wheel-platform-tag-audit](https://github.com/gbesse/wheel-platform-tag-audit) est un autre diagnostic du portefeuille. Ici : Expliquer les dépendances conditionnelles par extra. Comparaison de périmètres seulement, sans affiliation ni benchmark de supériorité.

EN: [wheel-platform-tag-audit](https://github.com/gbesse/wheel-platform-tag-audit) is a different portfolio diagnostic. Here: Explain conditional dependencies activated by extras. Scope comparison only, no affiliation or superiority benchmark.

ES: [wheel-platform-tag-audit](https://github.com/gbesse/wheel-platform-tag-audit) es otro diagnóstico del portafolio. Aquí: Explicar dependencias condicionales por extras. Comparación de alcance, sin afiliación ni benchmark de superioridad.
