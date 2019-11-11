# nasa-log-analysis
## Introdução
Este projeto tem como objetivo analisar os logs de requisições HTTP feitas para o servidor da NASA Kennedy Space Center. Além disso, possui as respostas de algumas questões teóricas sobre [Apache Spark](https://spark.apache.org/).

## Dados

**Download do dataset:**

* Julho: ftp://ita.ee.lbl.gov/traces/NASA_access_log_Jul95.gz

* Agosto: ftp://ita.ee.lbl.gov/traces/NASA_access_log_Aug95.gz

**Descrição do dataset:** Os logs estão em arquivos ASCII com uma linha por requisição com as seguintes colunas:

* Host fazendo a requisição. Um hostname quando possível, caso contrário o endereço de internet se o nome não puder ser identificado;

* Timestamp no formato "DIA/MÊS/ANO:HH:MM:SS TIMEZONE";

* Requisição (entre aspas);

* Código do retorno HTTP;

* Total de bytes retornados.

## Executando o projeto

### Em uma instância [BinderHub](https://binderhub.readthedocs.io/en/latest/)
O BinderHub permite criar um ambiente computacional personalizado que pode ser acessado por diferentes usuários utilizando uma URL. 

**Instruções de execução:** Clique em um dos banners abaixo (sugestão: clicar com o botão direito e abrir em nova aba) para executar o projeto em uma instância Binder com Spark, Hadoop e Python instalados. O projeto é executado no navegador, sem a necessidade de instalar as ferramentas na sua máquina =).

[![Binder](https://notebooks.gesis.org/binder/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/lucas91batista/nasa-log-analysis/master?urlpath=lab)


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lucas91batista/nasa-log-analysis/master?urlpath=lab)

Com o ambiente em execução, abrir o notebook index.ipynb e ir clicando no "Play" para executar o comando em cada célula. A cada click no "Play" uma célula é executada e seu resultado é exibido logo abaixo.

![Executando o projeto](https://github.com/lucas91batista/nasa-log-analysis/blob/master/resources/images/nasa.gif)

### Local

**Pré-requisitos:** Apache Spark 2.4.4. Download e instruções de instalação são encontradas em https://spark.apache.org/downloads.html.

**Instruções de execução:** Baixar o script _nasa_requests.py_ para sua máquina; baixar os dois arquivos do dataset e colocar em uma pasta _input_ no mesmo diretório do script _nasa_requests.py_. Executar o script:

```sh
spark-submit nasa_requests.py
``` 
## Informações extraídas do dataset

#### 1. Número de hosts únicos.
```sh
O número de hosts únicos: 137978
```
#### 2. O total de erros 404.
```sh
O total de erros 404: 20901
```
#### 3. As 5 URLs que mais causaram erro 404.
```sh
As 5 URL's que mais causaram erro 404:
URL: /pub/winvn/readme.txt                          Quantidade: 2004
URL: /pub/winvn/release.txt                         Quantidade: 1732
URL: /shuttle/missions/STS-69/mission-STS-69.html   Quantidade: 682
URL: /shuttle/missions/sts-68/ksc-upclose.gif       Quantidade: 426
URL: /history/apollo/a-001/a-001-patch-small.gif    Quantidade: 384
```
#### 4. Quantidade de erros 404 por dia.
```sh
A quantidade de erros 404 por dia: 
Dia: 01/Aug/1995 Quantidade: 243
Dia: 03/Aug/1995 Quantidade: 304
Dia: 04/Aug/1995 Quantidade: 346
Dia: 05/Aug/1995 Quantidade: 236
Dia: 06/Aug/1995 Quantidade: 373
Dia: 07/Aug/1995 Quantidade: 537
Dia: 08/Aug/1995 Quantidade: 391
Dia: 09/Aug/1995 Quantidade: 279
Dia: 10/Aug/1995 Quantidade: 315
Dia: 11/Aug/1995 Quantidade: 263
Dia: 12/Aug/1995 Quantidade: 196
Dia: 13/Aug/1995 Quantidade: 216
Dia: 14/Aug/1995 Quantidade: 287
Dia: 15/Aug/1995 Quantidade: 327
Dia: 16/Aug/1995 Quantidade: 259
Dia: 17/Aug/1995 Quantidade: 271
Dia: 18/Aug/1995 Quantidade: 256
Dia: 19/Aug/1995 Quantidade: 209
Dia: 20/Aug/1995 Quantidade: 312
Dia: 21/Aug/1995 Quantidade: 305
Dia: 22/Aug/1995 Quantidade: 288
Dia: 23/Aug/1995 Quantidade: 345
Dia: 24/Aug/1995 Quantidade: 420
Dia: 25/Aug/1995 Quantidade: 415
Dia: 26/Aug/1995 Quantidade: 366
Dia: 27/Aug/1995 Quantidade: 370
Dia: 28/Aug/1995 Quantidade: 410
Dia: 29/Aug/1995 Quantidade: 420
Dia: 30/Aug/1995 Quantidade: 571
Dia: 31/Aug/1995 Quantidade: 526
Dia: 01/Jul/1995 Quantidade: 316
Dia: 02/Jul/1995 Quantidade: 291
Dia: 03/Jul/1995 Quantidade: 474
Dia: 04/Jul/1995 Quantidade: 359
Dia: 05/Jul/1995 Quantidade: 497
Dia: 06/Jul/1995 Quantidade: 640
Dia: 07/Jul/1995 Quantidade: 570
Dia: 08/Jul/1995 Quantidade: 302
Dia: 09/Jul/1995 Quantidade: 348
Dia: 10/Jul/1995 Quantidade: 398
Dia: 11/Jul/1995 Quantidade: 471
Dia: 12/Jul/1995 Quantidade: 471
Dia: 13/Jul/1995 Quantidade: 532
Dia: 14/Jul/1995 Quantidade: 413
Dia: 15/Jul/1995 Quantidade: 254
Dia: 16/Jul/1995 Quantidade: 257
Dia: 17/Jul/1995 Quantidade: 406
Dia: 18/Jul/1995 Quantidade: 465
Dia: 19/Jul/1995 Quantidade: 639
Dia: 20/Jul/1995 Quantidade: 428
Dia: 21/Jul/1995 Quantidade: 334
Dia: 22/Jul/1995 Quantidade: 192
Dia: 23/Jul/1995 Quantidade: 233
Dia: 24/Jul/1995 Quantidade: 328
Dia: 25/Jul/1995 Quantidade: 461
Dia: 26/Jul/1995 Quantidade: 336
Dia: 27/Jul/1995 Quantidade: 336
Dia: 28/Jul/1995 Quantidade: 94
```
#### 5. O total de bytes retornados.
```sh
A quantidade de bytes utilizados: 65524314915
```

### Problemas encontrados no dataset:

1. Entrada fora do padrão esperado;
2. URLs das requisições com " e/ou espaços;
3. String - no lugar de inteiro para representar os bytes utilizados

## Questões Teóricas:
### 1. Qual o objetivo do comando cache em Spark?
O comando cache armazena o RDD (Resilient Distributed Dataset) em memória. Utilizamos a função cache quando queremos reutilizar o RDD. O RDD é reprocessado cada vez que executamos uma ação, utilizando a função cache este RDD ficará disponível na memória aumentando o desempenho de acesso em seu reuso.

### 2. O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?
O Spark utiliza o conceito de DAG (Directed Acyclic Graph - Grafos Acíclicos Direcionados) que permite mapear os passos que serão necessários para atingir o resultado esperado e, então, otimiza esses passos da melhor maneira possível; O Spark faz suas operações em memória; O Spark trabalha com RDD que armazena os elementos, é tolerante a falhas e pode ser executado em paralelo. Além disso, o Spark não computa os seus resultados de imediato, uma transformação é executada apenas quando uma ação é solicitada, isto também contribui para o seu desempenho. Por estes motivos, o Spark consegue executar um trabalho de maneira mais eficiente que o MapReduce.

### 3. Qual é a função do SparkContext?
O SparkContext permite a conexão com um cluster Spark e então podemos utilizar os recursos do Spark naquele cluster, por exemplo criar RDDs.

### 4. Explique com suas palavras o que é Resilient Distributed Datasets (RDD).
O RDD é a principal estrutura de dados do Spark, é um conjunto de registros imutáveis que podem ser executados em paralelo. É possível realizar transformações e ações no RDD. Apenas as transformações geram um novo RDD e essas transformações só são aplicadas quando uma ação é necessária. Cada vez que é necessário utilizar um RDD ele é reprocessado, mas existem funções para persistir um RDD em memória ou disco melhorando o desempenho.

### 5. GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?
O GroupByKey é menos eficiente que o reduceByKey porque ele transfere mais dados pela rede para computar o resultado final. O GroupByKey percorre todas as partições em busca de todos os valores para todas as chaves e então transfere todos esses dados via rede para obter o resultado final (processo conhecido como shuffle). Por outro lado, o reduceByKey primeiro agrega todas os valores das chaves, transferindo via rede uma menor quantidade de dados, ou seja, apenas um valor para cada chave.

### 6. Explique o que o código Scala abaixo faz.
```scala
val​​ ​ textFile​​ ​ = ​ ​ sc​ . ​ textFile​ ( ​ "hdfs://..."​ )
val​​ ​ counts​​ ​ = ​ ​ textFile​ . ​ flatMap​ ( ​ line​​ ​ =>​​ ​ line​ . ​ split​ ( ​ " ​ ​ " ​ ))
​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ . ​ map​ ( ​ word​​ ​ =>​​ ​ ( ​ word​ , ​ ​ 1 ​ ))
​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ . ​ reduceByKey​ ( ​ _ ​ ​ + ​ ​ _ ​ )
counts​ . ​ saveAsTextFile​ ( ​ "hdfs://..."​ )
``` 
O código realiza a contagem de palavras de um arquivo lido do HDFS e salva seu resultado em um arquivo texto também no HDFS. É criado um RDD a partir do arquivo lido do HDFS, em seguida ocorrem várias transformações: o RDD inicial é transformado utilizando a função flatMap, assim obtemos as palavras separando cada entrada por espaço. Em seguida, transformamos o RDD utilizando a função map para exportar pares chave-valor com a palavras sendo a chave e o valor o numeral 1. Por fim, a transformação reduceBykey irá somar os valores para cada chave. A ação saveAsTextFile faz com que as transformações sejam de fato processadas e salva o resultado em um arquivo no HDFS.
