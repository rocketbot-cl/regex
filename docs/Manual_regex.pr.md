



# Regex
  
Módulo para trabalhar com padrões fixos ou complexos através de Regex  

*Read this in other languages: [English](Manual_regex.md), [Português](Manual_regex.pr.md), [Español](Manual_regex.es.md)*

![banner](imgs\Banner_Regex.jpg)

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Comece com
  
Detecta sequências de texto que começam com uma letra ou número
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dados|Informações para pesquisar palavras que começam com uma letra ou número.|O|
|Texto|Texto para pesquisar palavras que começam com uma letra ou número|Olá mundo|
|Atribuir resultado à variável|Variável que armazena o resultado.|{var}|

### Contém 
  
Procure por strings de texto que contenham os dados indicados
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dados|Dados a serem procurados no texto|Undo|
|Texto|Texto para pesquisar palavras que contenham os dados indicados|Olá mundo|
|Atribuir resultado à variável|Variável que armazena o resultado.|{var}|

### Obter datas
  
Obtém todas as datas do texto inserido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Texto|Texto onde a data é obtida|Data: aaaa/mm/dd - dd/mm/aaaa|
|Atribuir resultado à variável|Variável onde a data obtida é armazenada|{var}|

### Obter telefone
  
Obter números de telefone de um texto
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Texto|Texto onde você consegue o número de telefone|Telefone: +18005551212|
|Atribuir resultado à variável|Variável onde os números de telefone obtidos são armazenados.|{var}|

### Obter e-mail
  
Obtém todos os e-mails em um texto
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Texto|Texto de onde você recebe o e-mail|E-mail: usuário@exemplo.com|
|Atribuir resultado à variável|Variável onde os emails obtidos são armazenados|{var}|
