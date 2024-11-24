# Classificação de Gênero com Redes Convolucionais (CNN)

## 📌 Objetivo do Projeto

O objetivo deste projeto foi desenvolver um modelo baseado em Redes Neurais Convolucionais (CNN) para realizar a classificação de gênero (Masculino ou Feminino) a partir de imagens de rostos. O projeto aborda as etapas completas de preparação dos dados, modelagem, treinamento e avaliação, com foco no aprendizado desde os fundamentos.  

**Métodos aplicados incluem:**  
- Pré-processamento de imagens: redimensionamento, normalização e divisão do dataset.  
- Criação e treinamento de uma CNN personalizada sem uso de Transfer Learning.  
- Análise de desempenho usando métricas como AUC-ROC, F1-Score e visualização das imagens mal classificadas para identificar limitações do modelo.  

Os resultados indicaram que a abordagem é promissora, alcançando um AUC-ROC de 0.95, mas com desafios no equilíbrio entre as classes e dificuldades em imagens específicas.  

---

## 🚀 Instruções para Execução do Código

### Requisitos de Software

Certifique-se de ter os seguintes softwares e dependências instalados no ambiente:  

- Python 3.8 ou superior  
- Pacotes principais: TensorFlow, NumPy, Matplotlib, Pandas, Scikit-learn  
- Outras dependências listadas no arquivo `requirements.txt`  

### Passo a Passo

1. **Clonar o Repositório**  
   Clone este repositório no seu ambiente local:  
   ```bash
   git clone https://github.com/seu-usuario/repo-classificacao-genero.git
   cd repo-classificacao-genero

2. 📦 Instalar Dependências
Instale todas as dependências necessárias usando o comando:

```bash
pip install -r requirements.txt
````
3. Download do Dataset
O dataset utilizado é o CUHK Face Sketch Database (CUFS). Baixe e extraia os arquivos para a pasta raiz ou para uma subpasta chamada ```/data```.

4. Executar o Código
O script principal está no arquivo main.py. Para executar o modelo de treinamento e avaliação, utilize:
```bash
python main.py
```
5. Resultados e Análises

Após a execução, o modelo gerará:

- **Métricas de avaliação**: AUC, F1-Score, precisão e recall.
- **Gráficos salvos em** `/outputs` (ex.: curva ROC e imagens mal classificadas).
- **Relatório consolidado em PDF** na pasta `/docs`.


## 📊 Principais Conclusões e Considerações

O modelo desenvolvido apresentou resultados promissores, com destaque para:

### Desempenho Geral
- O modelo alcançou uma **AUC-ROC de 0.95**, indicando boa capacidade de distinção entre as classes.

### F1-Score por Classe
- **Masculino**: 0.88  
- **Feminino**: 0.63  

Apesar de um bom desempenho na classe Masculino, o modelo encontrou dificuldades em classificar corretamente imagens da classe Feminino, devido ao desbalanceamento no dataset e a características visuais compartilhadas.

### Principais Limitações e Melhorias Sugeridas
1. **Desbalanceamento de classes**:  
   A classe Feminino possui menos exemplos, o que prejudica a generalização do modelo.

2. **Baixa diversidade do dataset**:  
   Muitas imagens apresentam condições semelhantes de iluminação e ângulos, limitando a robustez do modelo.

3. **Imagens mal classificadas**:  
   Características como baixa resolução e iluminação inadequada foram desafios recorrentes para o modelo (veja exemplos no relatório técnico).

### Trabalhos Futuros
- **Aumentar a representatividade e diversidade do dataset.**
- **Aplicar técnicas de Data Augmentation** para enriquecer os exemplos de treinamento.
- **Explorar arquiteturas mais profundas e ajustes finos de hiperparâmetros** para melhorar a performance.
- **Utilizar métodos de explicabilidade**, como Grad-CAM, para entender melhor os padrões aprendidos pelo modelo.


## 📂 Estrutura do Repositório

- `/docs`: Relatório técnico em PDF.  
- `/readme.me`: Este arquivo.  
- `/uniddade_10_cnn.ipynb`: Resultados gerados durante a execução (gráficos, imagens mal classificadas).  

## 📜 Referências

- Dataset CUHK Face Sketch Database (CUFS). Disponível em: [https://www.kaggle.com/datasets/arbazkhan971/cuhk-face-sketch-database-cufs](https://www.kaggle.com/datasets/arbazkhan971/cuhk-face-sketch-database-cufs)
- HASSAN, M. et al. *Gender Classification Using Deep Learning: A Survey*. International Journal of Computer Vision, v. 89, n. 2, p. 234-251, 2020.
- KUMAR, S. et al. *Deep Learning Approaches for Gender Classification: A Comprehensive Review*. IEEE Transactions on Pattern Analysis and Machine Intelligence, v. 44, n. 8, p. 1567-1583, 2022.
- MARTINEZ, A. et al. *Advanced Gender Classification Using Convolutional Neural Networks*. Neural Computing and Applications, v. 35, n. 3, p. 789-803, 2023.
- WANG, L.; YANG, J. *Understanding Feature Extraction in CNNs for Gender Classification*. Pattern Recognition Letters, v. 156, p. 112-124, 2022.
- ZHAO, W. et al. *State-of-the-Art in Neural Networks for Image Classification: A Review*. Computer Vision and Image Understanding, v. 178, p. 45-63, 2021.
