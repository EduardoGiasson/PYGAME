# 🎮 Simulação de Colisão de Textos com Pygame

## 📌 Sobre o Projeto

Este projeto foi desenvolvido utilizando **Python** e **Pygame**.

Ele simula dois textos se movimentando dentro de uma janela que:

- 🧱 Rebatem nas bordas da tela  
- 💥 Colidem entre si  
- 🎨 Mudam de cor quando ocorre colisão  

O comportamento visual é semelhante ao clássico efeito de tela de DVD.

## 🚀 Tecnologias Utilizadas

- Python 3
- Pygame
- random (biblioteca padrão)
- sys (biblioteca padrão)

## 🖥️ Como Funciona

### 🔹 Movimento

Cada texto possui:

- Um objeto `Rect` para controle de posição  
- Velocidade nos eixos X e Y  

```python
rect.x += vel_x
rect.y += vel_y
