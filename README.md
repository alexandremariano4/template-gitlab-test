#Como replicar o cenário - Português
1. Criar conta, grupo e projeto no gitlab, adicionar a SSH Key
2. Fazer clone do repositório : https://github.com/alexandremariano4/template-gitlab-test ou use como template para inserir no seu projeto no gitlab
3. Installe o Runner do gitlab, no meu caso, no windows: https://docs.gitlab.com/runner/install/windows.html (instale o binário para ser mais fácil a utilização)
4. Use o binário para executar os comandos: gitlab-runner install / gitlab-runner start → para executar o gitlab-runner na máquina.
5. Vá para a parte de “CI/CD→Runners” do seu projeto e vá na parte de Runners/Executadores
6. Desabilite os executores compartilhados

[Como deve ficar sua tela de "CI/CD->Runners"](https://imgur.com/a/h9KZ9He)

1. Clique em New project runner
2. Crie o runner com qualquer descrição e marque a terceira opção que é para o runner pegar mesmo que não tenha tag
3. Execute a etapa 1 que aparecerá na tela para registrar o Runner
4. Assim que registrar, irá aparecer “Você criou um novo executor”

[Criando o Runner local](https://imgur.com/a/bbLr41Y)

1. Vá para ap ágina dos executores/runners novamente para verificar se o runner está online, se estiver, vá para tela de CI/CD→Pipelines
2.  Execute um commit ou inicie manualmente a pipeline e veja sendo executado
3. Para debugar o container em execução abra o docker desktop e visualize-o sendo executado em tempo de execução.

#How to replicate the scenario - English
1. Create account, group and project in gitlab, add SSH Key
2. Clone the repository: https://github.com/alexandremariano4/template-gitlab-test or use it as a template to insert in your project on gitlab
3. Install Runner from gitlab, in my case, on windows: https://docs.gitlab.com/runner/install/windows.html (install the binary to be easier to use)
4. Use the binary to run the commands: gitlab-runner install / gitlab-runner start → to run gitlab-runner on the machine.
5. Go to the “CI/CD→Runners” part of your project and go to the Runners/Executors part
6. Disable shared executors

[What your "CI/CD->Runners" screen should look like](https://imgur.com/a/h9KZ9He)

1. Click New project runner
2. Create the runner with any description and check the third option which is for the runner to pick up even if it has no tag
3. Perform step 1 that will appear on the screen to register the Runner
4. Once registered, “You have created a new executor” will appear.

[Creating the local Runner](https://imgur.com/a/bbLr41Y)

1. Go to executors/runners page again to check if runner is online, if so go to CI/CD→Pipelines screen
2. Perform a commit or manually start the pipeline and watch it run
3. To debug the running container, open the docker desktop and view it running at runtime.
