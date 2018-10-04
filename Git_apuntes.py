
	# URL: https://informatica.ucm.es/data/cont/media/www/pag-66886/TallerGitGitHub.pdf
	# URL: https://git-scm.com/book/es/v1/Fundamentos-de-Git-Guardando-cambios-en-el-repositorio
	> Untracked > Unmodified > Modificado > Staged > Commited

	# Inicio:
	#########
	> cd <ruta proyecto>; git init	# Crea un repositorio a partir de código existente.
	> git init <ruta proyecto>		# Crea repositorio en blanco.


	# Información:
	##############
	> git status					# Cambios pendientes de commit.
	> git diff						# Muestra los cambios de archivos modificados pero NO 
									# añadidos al staging area.
	> git diff --cached				# Muestra los cambios de archivos modificados que SI 
									#están añadidos al staging area.

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
	> git log [-p ] [-2]			# Visualizar la historia de los commits.
									# -p: Visualiza los cambios realizados (diff) en los commit.
									# -2, ó -N: límite del número de commits a visualizar.		
	> git reset HEAD~1 				# Deshace el último commit del branch actual, como si 
									# no hubiera existido.
									# El HEAD~1 es el commit anterior al último commit de
									# la rama.
	> git revert <sha1 commit>		# Deshacer un commit (dejando constancia que se ha eliminado).
								

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
	> git fetch <nombre remote>		# Traerse los cambios de un repositorio remoto.
	> git merge <remote>/<nombre branch> # Aplico los cambios que hay en un remoto.
	> git pull [<remote>] [<nombre branch>] # Traigo los cambios y los aplico. Las dos 
											# anteriores a la vez.

	> git push [<remote>] [<nombre branch>] # Envío los cambios a un remoto.
	
	> git remote 					# Muestra el nombre del remote que hay en mi repositorio local.
	> git remote –v 				# Muestra la URL que se utilizo para crear el remote.

	> git remote add <nombre> <URL> # Añade un remote a mi repositorio local. 


	# Remotes y sus branches:
	#########################

	# Cuando se clona un repositorio remoto se crea una branch local asociado al branch del master
		# E.g.: si el remote es "master" al clonarlo queda como "origin/master".				
		# Estos branches se denominan tracking branches

	> git ls-remote <remote>		# Lista los branches que hay en un remote.
	> git checkout --track <remote>/<branch> # Para traerme un branch remoto.
	> git checkout –b <branch> <remote>/<branch> # Para traerme un branch remoto.
	> git push origin :<branch>		# Borro un branch remoto.


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



	# Referencias:
	##############
	# URL: http://git-scm.com/
	
	> Información básica:
		> Pro Git (Free book): 
			# URL: https://git-scm.com/book/en/v2
		> Manual de git:
			# URL: https://mirrors.edge.kernel.org/pub/software/scm/git/docs/gittutorial.html
		> Everyday Git with 20 commands or so:
			# URL: https://mirrors.edge.kernel.org/pub/software/scm/git/docs/giteveryday.html
		> Git User Manual:
			# URL: https://mirrors.edge.kernel.org/pub/software/scm/git/docs/user-manual.html	
		> Git core tutorial:
			# URL: https://mirrors.edge.kernel.org/pub/software/scm/git/docs/gitcore-tutorial.html
		> Git Pocket Guide (Acceso con IP UCM):
			# URL: https://proquest.safaribooksonline.com/book/databases/content-management-systems/9781449327507
		> Version Control with Git, 2nd Edition (Acceso con IP UCM):
			# URL: https://proquest.safaribooksonline.com/book/databases/content-management-systems/9781449345037
	
	> Páginas para aprender GIT:
		# URL: http://speckyboy.com/2013/06/03/resources-for-learning-git/
		# URL: http://www.gitguys.com/
		# URL: http://teach.github.com/
		# URL: http://gitimmersion.com/
		# URL: http://sixrevisions.com/resources/git-tutorials-beginners/
		# URL: http://www.webdesignerdepot.com/2009/03/intro-to-git-for-web-designers/

	> Tips para GIT:
		> git-for-beginners-the-definitive-practical-guide:
			# URL: https://stackoverflow.com/questions/315911/git-for-beginners-the-definitive-practical-guide
		> Git Ready:
			# URL: http://gitready.com/
		> Opciones del comando git add:
			# URL: http://aprendegit.com/opciones-del-comando-git-add/
		> Forzar un merge commit:
			# URL: http://aprendegit.com/forzando-merge-commits/
		> Mantener carpetas vacías en el repositorio:
			# URL: http://aprendegit.com/gitkeep-incluyendo-carpetas-en-los-repositorios/
		> Xcode y Git:
			# URL: http://aprendegit.com/category/xcode/
		> Visual Git Reference (comandos intermedios):
			# URL: http://marklodato.github.io/visual-git-guide/index-en.html
		> 6 Motivos por los que Git no es un sistema de backups:
			# URL: http://aprendegit.com/6-motivos-por-los-que-git-no-es-un-sistema-de-backup/
		> Revisar cambios que se han añadido al index (staged):
			# URL: https://stackoverflow.com/questions/1587846/how-do-i-show-the-changes-which-have-been-staged
	
	> Conceptos avanzados de GIT:
		> http://softwareswirl.blogspot.de/:
			# URL: http://softwareswirl.blogspot.de/
		> Referencias, Github y pull requests:
			# URL: http://aprendegit.com/uso-avanzado-de-referencias-github-y-pull-requests/
		> Git alias: creación de comandos parametrizados:
			# URL: http://durdn.com/blog/2012/11/22/must-have-git-aliases-advanced-examples/
		> Convertir repositorio SVN a GIT:
			# URL: http://john.albin.net/git/convert-subversion-to-git