
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

    > Tutoriales sencillos para empezar:

        # URL: http://rogerdudler.github.io/git-guide/index.es.html
        # URL: https://git-scm.com/book/es/v1/Empezando
        # URL: https://es.atlassian.com/git
        # URL: https://guides.github.com/activities/hello-world/


    > Libros de Git:

        > Pro Git (Free book): 
            # URL: https://git-scm.com/book/en/v2
        # URL: https://progit2.s3.amazonaws.com/en/2016-03-22-f3531/progit-en.1084.pdf

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
        > Si todo el local y el remoto están al día, pero git muestra el mensaje: 
            # "Your branch is ahead of 'origin/master' by 6 commits. (use "git push" to publish 
            #  your local commits)":"
            # Una solución es:
            > git fetch # Y desaparecerán los mensajes de error.
            # URL: https://stackoverflow.com/questions/16288176/your-branch-is-ahead-of-origin-master-by-3-commits



    > Conceptos avanzados de GIT:

        > Guardar credenciales de GitHub en local:
            # URL: https://stackoverflow.com/questions/35942754/how-to-save-username-and-password-in-git
            # URL: https://git-scm.com/docs/git-credential-store
        > Mostrar el contenido de una versión anterior de un archivo específico:        
            # URL: https://stackoverflow.com/questions/338436/is-there-a-quick-git-command-to-see-an-old-version-of-a-file
        > Mostrar las diferencias entre un repositorio local y uno remoto:
            # URL: https://stackoverflow.com/questions/46786070/how-to-show-differences-between-local-and-remote-files-in-git
        > Recuperar una versión anterior de un archivo específico:
            # URL: https://stackoverflow.com/questions/215718/reset-or-revert-a-specific-file-to-a-specific-revision-using-git
        > http://softwareswirl.blogspot.de/:
            # URL: http://softwareswirl.blogspot.de/
        > Referencias, Github y pull requests:
            # URL: http://aprendegit.com/uso-avanzado-de-referencias-github-y-pull-requests/
        > Git alias: creación de comandos parametrizados:
            # URL: http://durdn.com/blog/2012/11/22/must-have-git-aliases-advanced-examples/
        > Convertir repositorio SVN a GIT:
            # URL: http://john.albin.net/git/convert-subversion-to-git


    > Trabajar con BitBucket:

        > Add unversioned code to a repository:
            Añadir a Git un proyecto local y subirlo a un repositorio remoto nuevo en BitBucket:
            
            https://confluence.atlassian.com/bitbucket/add-unversioned-code-to-a-repository-877177133.html

        > Connect your new local Git repository to the remote repository on Bitbucket.:

            git remote add origin <bitbucket_URL>

            Ej: git remote add origin https://alvareztrabajo@bitbucket.org/alvareztrabajo/proyectos.git

        > Push all the code in your local repo to Bitbucket with the following command:

            git push -u origin --all

        > Problemas comunes al intentar trabajar con BitBucket desde la línea de comandos:

            > Si al hacer "git push -u origin --all" sale el error:
                '''
                Permission denied (publickey).
                fatal: Could not read from remote repository.

                Please make sure you have the correct access rights
                and the repository exists.
                '''

                git error error: src refspec master does not match any."

                Solución: seguir la guía "Set up an SSH key":

                # URL: https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html


    > Git para SublimeText:

        # URL: https://intelequia.com/blog/post/585/git-y-sublime-text-la-pareja-perfecta


    > Truco: abrir archivo en TextEdit desde la Terminal de Mac OS X:

        # URL: https://www.appleayuda.com/pregunta/18/puedo-abrir-archivos-en-textedit-de-la-terminal-en-mac-os-x

    - Error: "bitbucket line 9: Bad configuration option: usekeychain"

        # URL: https://stackoverflow.com/questions/47455300/ssh-config-bad-configuration-option-usekeychain-on-mac-os-sierra-10-12-6



