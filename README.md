Sistema de Irrigação Automática com ESP32 🪴
============================================

Este projeto consiste em um sistema inteligente de monitoramento e irrigação automatizada desenvolvido para a disciplina de **IoT (Internet das Coisas)**. O protótipo foi construído utilizando **MicroPython** e simulado no **Wokwi**.

O sistema utiliza um sensor de umidade (simulado por um potenciômetro) para medir a necessidade de água do solo, controlando uma bomba d'água via módulo relé e fornecendo feedback visual através de LEDs coloridos.

📋 Requisitos da Atividade
--------------------------

Conforme o enunciado proposto, o sistema atende aos seguintes critérios:

*   **Medição:** Utilizar um sensor de umidade para medir o nível de água no solo.
    
*   **Automação:** Acionar um relé conectado a uma bomba d’água quando a umidade estiver baixa.
    
*   **Sinalização Visual:** \* 🔴 **LED Vermelho:** Solo seco (irrigação necessária).
    
    *   🟢 **LED Verde:** Umidade ideal.
        
    *   🔵 **LED Azul:** Solo muito úmido/saturado.
        
*   **Exibição:** Mostrar os valores de umidade em tempo real no monitor serial.
    

🛠️ Hardware Utilizado (Pinagem)
--------------------------------

A montagem seguiu a configuração de pinos abaixo no ESP32:

**ComponentePino ESP32FunçãoPotenciômetro**GPIO 34Simulador de Sensor de Umidade (Analógico)**Relé**GPIO 26Controle da Bomba d'água**LED Vermelho**GPIO 12Alerta de Solo Seco**LED Verde**GPIO 14Indicador de Umidade Ideal**LED Azul**GPIO 27Indicador de Solo Saturado**Resistores**\-220Ω para proteção de cada LED
