
	# URL: https://informatica.ucm.es/data/cont/media/www/pag-66886/TallerGitGitHub.pdf
	# URL: https://git-scm.com/book/es/v1/Fundamentos-de-Git-Guardando-cambios-en-el-repositorio
	
	# Conceptos básicos:
	####################
	> Untracked > Unmodified > Modificado > Staged > Commited # Flujo de trabajo de un archivo.

	> áreas de trabajo:
		# Son áreas de trabajo que están en tu disco local.
		- Working directory 				# Files in your working directory.
		- Staging Area (aka cache, index) 	# A temp area that git add is placed into.
		- HEAD 								# A reference to a specific commit (think of 
											# it as a variable). Normally, it points to 
											# the last commit in local repository. (that is, 
											# after you did git commit).


	# Inicio:
	#########
	> cd <ruta proyecto>; git init	# Crea un repositorio a partir de código existente.
	> git init <ruta proyecto>		# Crea repositorio en blanco.


	# Información:
	##############
	> git status				# Informe de estado.ç
	> git diff --color			# diff working dir, staging area.
	> git diff --color filename # diff working dir, staging area, para 1 filename.
	> git diff					# diff staging area, commit.
	> git diff filename			# diff staging area, commit, para 1 filename.
	> git diff --cached			# Muestra los cambios de archivos modificados que SI 
								# están añadidos al staging area, y los del commit.
	> git diff --staged 		# Muestra los cambios entre los archivos del HEAD y el 
								# staging area. El "HEAD" es current branch, is a pointer 
								# to the local branch you’re currently on, y normalmente
								# estás en el branch "master". Por lo que en ocasiones
								# este comando es equivalente a "git diff --cached"



	> ¿Cómo mostrar diferencias entre repositorio local y un remote?:
		# Por repositorio local se entiende que son los archivos en el commit, no los 
		# modificados del staging área ni los modificados.
		# Es decir, muestra los cambios entre los archivos del commit local y los del 
		# remote.
		# Me traigo el repositorio remoto pero sin "merge" con el local:
		git fetch origin master
		# Comparo ambos repositorios:
		git diff <local-branch> <remote repo>/<remote branch>
		Ej: git diff master origin/master
		Ej: git diff master mi_remote_repo/master

		# Otra forma de hacerlo:
		git fetch origin ; git diff --name-only master origin/master

	> git show <commitHash>:<path to file> # Mostrar cómo estaba el archivo en ese commit.


	# Ayuda:
	########
	> git help <comando>			# Ayuda sobre un comando.
	> git help config				# Ayuda para ver qué opciones hay de configuración.


	# Copia de trabajo:
	###################
	> git rm <archivo>				# Elimina el archivo (opción recomendada).
	> rm <archivo>; git rm [-f] <archivo> # otra forma de eliminar el archivo.

	> git mv <origen> <destino>		# Renombar el archivo.
	> mv <origen> <destino>;git rm <origen>; git add <destino> # Otra forma más larga 
									# de hacerlo.
									# Git se da cuenta de que estamos renombrando el 
									# archivo debido a la firma del archivo.

	> git checkout -- <archivo>		# Deshacer los cambios en la copia de trabajo y volver 
									# al archivo original desde la última instantánea.

	# Staging area:
	###############
	> git add <ruta archivo>		# Añade el archivo al Staging area.
	> git add *   					# Incluye en Git todos los archivos o los añade al Staging area. 
	> git add *.py  				# Incluye en Git los archivos *.py o los añade al Staging area.
	> git add .  					# Añade todos los archivos nuevos o modificados.
									# Ojo! si modificas el archivo añadido tendrás que 
									# volver a añadirlo.
	> git add -A  					# Añade todos los archivos modificados, nuevos o borrados.

									# Eliminar un archivo del staging area sin perder 
									# las modificaciones:
	> git rm --cached <archivo> 	# ...Si el archivo es nuevo.
	> git reset HEAD <archivo>		# ...Si el archivo está modificado.
									# Útil por si no queremos hacer commit de este archivo.

	# Commits:
	##########
	> git commit -m "Mensaje"		# Crea una instantánea en el repositorio teniendo 
									# en cuenta:
										# El estado de la última instantánea realizada.
										# El contenido de la staging area.
		Ej: git commit -m "initial commit of full repository"

	> git log [-p ] [-2]			# Visualizar la historia de los commits.
									# -p: Visualiza los cambios realizados (diff) en los commit.
									# -2, ó -N: límite del número de commits a visualizar.		
	> git reset HEAD~1 				# Deshace el último commit del branch actual, como si 
									# no hubiera existido.
									# El HEAD~1 es el commit anterior al último commit de
									# la rama.
	> git revert <sha1 commit>		# Deshacer un commit (dejando constancia que se ha eliminado).
	
	> Recuperar una versión anterior de un archivo específico:
		# Buscas el archivo en el listado de commits realizados, y recuperas ese archivo
		# del commit previo que elijas.
		> git log 					# Buscas en el listado de commits realizados
		> git show <commitHash>:<path to file> # Mostrar cómo estaba el archivo en ese commit.
		> git checkout <commitHash> -- <file1/to/restore> # Recuperar el archivo del commit que elijas
					

	# Branches:
	###########
	> Flujo de trabajo con branches:
		> Crear un branch cuando tengo que hacer una tarea o quiero experimentar algo.
		> Trabajar sobre el branch (desarrollar, hacer pruebas).
		> Nos aseguramos que la copia de trabajo está limpia (que no haya ningún cambio pendiente).
		> Actualizamos nuestro branch de trabajo con los cambios que haya habido en master.
		> Cuando estamos contentos con el trabajo hacemos un merge del trabajo en el branch master.

	> git branch [-v] –a			# Listar branches / Averiguar branch actual.
									# La referencia HEAD apunta al branch actual.
	> git branch <nombre branch>	# Crea un branch a partir del branch actual.
	> git checkout <nombre branch>	# Para pasar a trabajar a otro branch.
	> git checkout –b <nombre branch> # Los dos a la vez. Crea el branch y pasa a trabajar
									# a él.

	> git branch -d <branch>		# Elimina un branch (si ya está integrado en el branch activo)

	#¿Cómo hacemos un merge cuando queremos integrar el trabajo de un branch en el master?
	> git checkout master			# Hacemos un checkout del branch donde vamos a integrar 
									# los cambios.
	> git merge <nombre branch>		# E integrammos los cambios.


	# ¿Cómo averiguo que branches NO están integrados con el branch activo?
	> git branch --no-merged		# Lista los que no están integrados.
	> git branch --no-merged 		# Lista los que sí están integrados.

	
	# ¿Cómo deshago el último commit del branch actual?
	> git reset HEAD~1 				# Como si no hubiera existido.
									# El HEAD~1 es el commit anterior al último commit de
									# la rama.
	> git revert <sha1 commit>		# Deshacer un commit (dejando constancia que se 
									# ha eliminado).


	# Remotes:
	###########
	> git remote add origin <bitbucket_URL> # Connect your new local Git repository 
											# to the remote repository.
		Ej: git remote add origin https://alvareztrabajo@bitbucket.org/alvareztrabajo/proyectos.git
			
	> git fetch <nombre remote>		# Traerse los cambios de un repositorio remoto.
	> git merge <remote>/<nombre branch> # Aplico los cambios que hay en un remoto.
	> git pull [<remote>] [<nombre branch>] # Traigo los cambios y los aplico. Las dos 
											# anteriores a la vez.

	> git push [<remote>] [<nombre branch>] # Envío los cambios a un remoto.
		Ej: git push -u origin --all
	
	> git remote 					# Muestra el nombre de los remotes que hay en mi repositorio local.
	> git remote –v 				# Muestra la URL que se utilizo para crear el remote.

	> git remote add <nombre> <URL> # Añade un remote a mi repositorio local. 

	# Remotes y sus branches:
	#########################
	> Cuando se clona un repositorio remoto se crea una branch local asociado al branch del master
		# E.g.: si el remote es "master" al clonarlo queda como "origin/master".				
		# Estos branches se denominan tracking branches

	> git ls-remote <remote>		# Lista los branches que hay en un remote.
	> git checkout --track <remote>/<branch> # Para traerme un branch remoto.
	> git checkout –b <branch> <remote>/<branch> # Para traerme un branch remoto.
	> git push origin :<branch>		# Borro un branch remoto.


	# Guardar credenciales de un remote en local:
	#############################################
	> Cada vez que hacemos un Push tenemos que identificarnos en el remote, pero podemos
 	  guardar las credenciales en local:
 	  
 	  # Averiguamos la ruta completa del remote, incluyendo credenciales:
 	  	https://Username:Password@github.com/myRepoDir/myRepo.git
 	  	Ej:https://miusuario:mipass@github.com/miusuario/mirepo.git

 	  # Añadimos el remote indicando la ruta completa del mismo:
 	  	git remote add mirepo https://Username:Password@github.com/myRepoDir/myRepo.git

 	  # Y ya podemos utilizar este remote sin necesidad de identificarnos:
 	  	git push mirepo			 	
 	  	git push mirepo <branch> 	# Si quiero indicar en qué rama publico los cambios.


	# Deshacer los cambios:
	#######################
	> git checkout -- <archivo>		# Deshacer los cambios en la copia de trabajo y volver 
									# al archivo original desde la última instantánea.

									# Eliminar un archivo del staging area sin perder 
									# las modificaciones:
	> git rm --cached <archivo> 	# ...Si el archivo es nuevo.
	> git reset HEAD <archivo>		# ...Si el archivo está modificado.
									# Útil por si no queremos hacer commit de este archivo.

	> git reset HEAD~1 				# Deshace el último commit del branch actual, como si 
									# no hubiera existido.
									# El HEAD~1 es el commit anterior al último commit de
									# la rama.
	> git revert <sha1 commit>		# Deshacer un commit (dejando constancia que se 
									# ha eliminado).
