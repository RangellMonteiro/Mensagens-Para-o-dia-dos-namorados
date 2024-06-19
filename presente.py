import tkinter as tk
import pygame
import numpy as np

# Lista de mensagens a serem exibidas
messages = [
    "Olá! Meu amor, venho através destes códigos expressar o quanto você é especial para mim.",
    "Você é a luz que ilumina meu caminho, e a razão dos meus mais sinceros sorrisos.",
    "Desde o momento em que nos conhecemos, você transformou a minha vida de uma forma que eu nunca poderia imaginar.",
    "Cada dia ao seu lado é uma nova aventura, repleta de risos, carinho e momentos inesquecíveis.",
    "Neste dia especial, quero reafirmar o meu amor por você e agradecer por cada momento que compartilhamos.",
    "Obrigado por ser minha companheira, minha amiga e meu grande amor.",
    "Prometo estar ao seu lado, te apoiando e te amando cada vez mais, hoje e sempre.",
    "Feliz Dia dos Namorados, meu amor. Que possamos celebrar muitos e muitos outros juntos, construindo uma história de amor que é só nossa.",
    "Com todo o meu amor, Rangell"

]

# Função que muda a mensagem na tela
def change_message():
    global current_message_index
    if current_message_index < len(messages):
        label.config(text=messages[current_message_index])
        current_message_index += 1
    else:
        # Exibir coração
        # Inicializando o Pygame
        pygame.init()

        # Configurando a tela
        width, height = 800, 600
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Coração")

        # Definindo cores
        red = (255, 0, 0)
        white = (255, 255, 255)

        # Função para desenhar o coração
        def draw_heart(screen, center, size):
            t = np.linspace(0, 2 * np.pi, 1000)
            x = center[0] + size * 16 * np.sin(t)**3
            y = center[1] - size * (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t))
            points = [(int(x[i]), int(y[i])) for i in range(len(t))]
            pygame.draw.polygon(screen, red, points)

        # Loop principal
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Preenchendo o fundo
            screen.fill(white)

            # Desenhando o coração
            draw_heart(screen, (width // 2, height // 2), 10)

            # Atualizando a tela
            pygame.display.flip()

        # Encerrando o Pygame
        pygame.quit()

# Configuração inicial
current_message_index = 0

# Criação da janela principal
root = tk.Tk()
root.title("Para o meu amor Yasmin")

# Criação de um label para exibir as mensagens
label = tk.Label(root, text="", font=("Helvetica", 16))
label.pack(pady=20)

# Criação de um botão que chama a função change_message quando clicado
button = tk.Button(root, text="S2", command=change_message, font=("Helvetica", 14))
button.pack(pady=20)

# Exibir a primeira mensagem
change_message()

# Iniciar o loop principal da interface gráfica
root.mainloop()
