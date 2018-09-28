
	> Untracked > Unmodified > Modificado > Staged > Commited


	> cd <ruta proyecto>; git init	# Crea un repositorio a partir de código existente.
	> git init <ruta proyecto>		# Crea repositorio en blanco.



	> git help <comando>			# Ayuda sobre un comando.
	> git help config				# Ayuda para ver qué opciones hay de configuración


	# Información:
	##############
	> git status					# Cambios pendientes de commit.
	> git diff						# Muestra los cambios de archivos modificados pero NO 
									# añadidos al staging area.
	> git diff --cached				# Muestra los cambios de archivos modificados que SI 
									#están añadidos al staging area.

	# Deshaer cambios en Copia de trabajo:
	######################################
	> git checkout -- <archivo>		# Deshacer los cambios en la copia de trabajo y volver 
									# al archivo original desde la última instantánea.

	# Staging area:
	###############
	> git add <ruta archivo>		# Añade el archivo al Staging area
	> git add .  					# Añade todos los archivos nuevos o modificados
	# Ojo! si modificas el archivo añadido tendrás que volver a añadirlo
	> git add -A  					# Añade todos los archivos modificados, nuevos o borrados

	# Eliminar un archivo del staging area sin perder las modificaciones:
	> git rm --cached <archivo> 	# ...Si el archivo es nuevo.
	> git reset HEAD <archivo>		# ...Si el archivo está modificado.


	# Commits:
	##########				
	> git reset HEAD~1 				# Deshace el último commit del branch actual.
									# El HEAD~1 es el commit anterior al último commit de
									# la rama.
	> git revert <sha1 commit>		# Deshacer un commit (dejando constancia que se ha eliminado)


	# Branches:
	###########

	> git branch [-v] –a			# Listar branches / Averiguar branch actual
	> git branch <nombre branch>	# Crea un branch a partir del branch actual
	> git checkout <nombre branch>	# Pasar a trabajar a otro branch
	> git checkout –b <nombre branch> # Los dos a la vez