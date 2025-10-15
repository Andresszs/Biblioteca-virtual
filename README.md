# 📚 Biblioteca Virtual - Sistema de Venta de Libros

## Descripción del Proyecto
Sistema de e-commerce especializado en venta de libros digitales desarrollado como proyecto académico.

## Características Principales
- Catálogo de libros con búsqueda avanzada
- Sistema de carrito y compras
- Biblioteca personal de usuarios
- Sistema de reseñas y calificaciones

## Historias de Usuario
- 15 HU implementadas en tablero Kanban
- Seguimiento de desarrollo en GitHub Projects

## Tecnologías
- Frontend: Por definir
- Backend: Por definir
- Base de datos: Por definir

#Comandos GIT

### Conceptos Clave

- **Repositorio**: Directorio que contiene el proyecto y su historial de versiones
- **Commit**: Instantánea de los cambios realizados en el proyecto
- **Branch**: Línea independiente de desarrollo
- **Merge**: Proceso de combinar cambios de diferentes ramas
- **Remote**: Versión del repositorio alojada en un servidor remoto


## Comandos Básicos de Git

### Inicialización y Clonado

```bash
# Inicializar un nuevo repositorio
git init

# Clonar un repositorio existente
git clone https://github.com/usuario/repositorio.git

# Clonar con un nombre específico
git clone https://github.com/usuario/repositorio.git mi-proyecto
```

### Seguimiento de Cambios

```bash
# Ver estado del repositorio
git status

# Agregar archivos al staging area
git add archivo.txt
git add .                    # Agregar todos los archivos
git add *.js                 # Agregar archivos por patrón

# Confirmar cambios
git commit -m "Mensaje descriptivo del commit"
git commit -am "Agregar y confirmar archivos modificados"

# Ver historial de commits
git log
git log --oneline           # Formato compacto
git log --graph             # Mostrar gráfico de ramas
```

### Información y Diferencias

```bash
# Ver diferencias no confirmadas
git diff

# Ver diferencias en staging area
git diff --cached

# Ver diferencias entre commits
git diff commit1 commit2

# Mostrar información de un commit específico
git show commit-hash
```

### Deshacer Cambios

```bash
# Deshacer cambios en working directory
git checkout -- archivo.txt

# Quitar archivo del staging area
git reset HEAD archivo.txt

# Deshacer último commit (mantener cambios)
git reset --soft HEAD~1

# Deshacer último commit (eliminar cambios)
git reset --hard HEAD~1
```

> **⚠️ Advertencia**: `git reset --hard` elimina permanentemente los cambios no confirmados.

---

## Trabajo con Ramas

### Gestión de Ramas

```bash
# Listar ramas locales
git branch

# Listar todas las ramas (locales y remotas)
git branch -a

# Crear nueva rama
git branch nueva-funcionalidad

# Cambiar a una rama
git checkout nueva-funcionalidad

# Crear y cambiar a nueva rama
git checkout -b nueva-funcionalidad

# Cambiar a rama (comando moderno)
git switch nueva-funcionalidad

# Crear y cambiar a nueva rama (comando moderno)
git switch -c nueva-funcionalidad
```

### Fusión de Ramas

```bash
# Fusionar rama en la rama actual
git merge nombre-rama

# Fusión con mensaje personalizado
git merge nombre-rama -m "Mensaje de merge"

# Fusión sin fast-forward
git merge --no-ff nombre-rama

# Eliminar rama local
git branch -d nombre-rama

# Eliminar rama forzadamente
git branch -D nombre-rama
```

### Rebase

```bash
# Rebase interactivo
git rebase -i HEAD~3

# Rebase sobre otra rama
git rebase development

# Continuar rebase después de resolver conflictos
git rebase --continue

# Abortar rebase
git rebase --abort
```

> **Nota**: Usa rebase para mantener un historial lineal y limpio, pero evítalo en ramas compartidas.

---
*-*-*-*-*-*-**/*/*/*/*/*/*/
## GitHub: Comandos Remotos
### Sincronización con Repositorio Remoto

```bash
# Subir cambios al repositorio remoto
git push origin development
# Subir nueva rama al remoto
git push -u origin nueva-funcionalidad

# Subir todas las ramas
git push --all origin

# Subir tags
git push --tags origin

# Forzar push (usar con precaución)
git push --force origin development
```

### Obtener Cambios del Remoto

```bash
# Obtener cambios sin fusionar
git fetch origin

# Obtener y fusionar cambios
git pull origin development

# Pull con rebase
git pull --rebase origin development

# Establecer rama upstream
git branch --set-upstream-to=origin/development development
```


---

## Solución de Conflictos

### Identificar y Resolver Conflictos

```bash
# Ver archivos con conflictos
git status

# Ver diferencias de conflictos
git diff

# Resolver conflictos manualmente y confirmar
git add archivo-resuelto.txt
git commit -m "Resolver conflicto en archivo-resuelto.txt"

# Usar herramienta de merge
git mergetool
