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
