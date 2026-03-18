# 🏓 Refatoração do Pong em Pygame

## 📌 Objetivo

Melhorar a organização, manutenção e legibilidade do código, reduzindo o acoplamento e centralizando configurações.

---

## Antes da Refatoração

### Problemas encontrados:

- Valores espalhados pelo código
- Dificuldade para alterar configurações (precisava modificar em vários lugares)
- Código mais difícil de manter e escalar

### Exemplo:

```python
largura = 800
altura = 600
velocidade_bola_x = 5
raquete_altura = 60
```

Se fosse necessário mudar algo, era preciso procurar no código inteiro.

---

## Depois da Refatoração

### Solução aplicada:

Criação de classes para centralizar configurações:

- `Cores` → cores do sistema
- `Config` → configurações globais (tela, FPS)
- `JogoConfig` → regras e parâmetros do jogo

### Exemplo:

```python
class Config:
    LARGURA = 800
    ALTURA = 600

class JogoConfig:
    VELOCIDADE_RAQUETE = 5
```

Agora, qualquer alteração é feita em um único lugar.

## 🔄 Evolução da Refatoração (POO)

Além das configurações, o código também foi melhorado com **Programação Orientada a Objetos (POO)**:

- Foi criada a classe `Player` para representar as raquetes
- Foi criada a classe `Bola` para representar a bola

➡️ Agora cada entidade do jogo é responsável por seu próprio comportamento.

---

## 🧍 Classe Player (Raquete)

A classe `Player` representa cada jogador no jogo.

### Responsabilidades:

- Armazenar posição (x, y)
- Movimentar a raquete para cima e para baixo
- Impedir que saia da tela
- Desenhar a raquete na tela
- Fornecer área de colisão (retângulo)

### Extra:

- Possui o método `ia()`, que faz o jogador automático (bot) seguir a bola

➡️ Toda a lógica da raquete fica organizada em um único lugar.

---

## ⚽ Classe Bola

A classe `Bola` controla todo o comportamento da bola.

### Responsabilidades:

- Iniciar no centro da tela (`reset()`)
- Se movimentar (`mover()`)
- Quicar nas bordas superior e inferior
- Detectar colisão com os jogadores
- Inverter direção ao bater nas raquetes
- Desenhar a bola na tela

➡️ Toda a física e movimentação da bola ficam centralizadas.

---

## Principais Melhorias

### 1. Centralização de Configurações

- Todos os valores importantes ficam organizados
- Evita repetição de código

### 2. Redução de Acoplamento

- Código principal não depende mais de valores fixos
- Depende apenas das configurações

### 3. Facilidade de Manutenção

- Mudanças rápidas e seguras
- Menor chance de erro

### 4. Melhor Organização

Separação clara de responsabilidades:

- Sistema
- Aparência
- Lógica do jogo

---

## 🚀 Benefícios Finais

- Código mais limpo
- Mais fácil de entender
- Mais fácil de evoluir
- Mais organizado
