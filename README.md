# Reconhecimento de Celebridades com AWS Rekognition

Este projeto utiliza o serviço **AWS Rekognition** para identificar celebridades em imagens e marcar seus rostos com caixas vermelhas e nomes. O código está escrito em **Python** e utiliza a biblioteca **Boto3** para acessar a API da AWS.

## 📸 Demonstração

### Exemplo de entrada:

- Imagem de teste com múltiplas celebridades.



### Exemplo de saída:

- Imagem processada com os rostos reconhecidos marcados.



## 🔧 Configuração e Uso

### 1️⃣ Pré-requisitos

- Python 3 instalado
- Conta na AWS e credenciais configuradas
- Dependências instaladas

### 2️⃣ Instalação

- Clone o repositório e instale as dependências necessárias:

```bash
git clone https://github.com/dorigonato/reconhecimento-celebridades.git
```

### 3️⃣ Como Usar

1. Adicione imagens na pasta `images/`.
2. Execute o script:

```bash
python reconhecimento.py
```

3. As imagens processadas serão salvas na mesma pasta com o sufixo `-resultado.jpg`.

## 📌 Insights

- O AWS Rekognition é uma solução poderosa para reconhecimento facial.
- A precisão da identificação depende da qualidade da imagem.
- Apenas celebridades reconhecidas são marcadas.

## 📜 Licença

Este projeto é de código aberto e está sob a licença MIT.

