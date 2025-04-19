# BLE Fence – Cerca Eletrónica com Bluetooth Low Energy

A **BLE Fence** é uma aplicação Python que atua como uma "cerca eletrónica", emitindo um alerta sonoro quando um dispositivo Bluetooth Low Energy (BLE) ultrapassa uma distância segura definida. É ideal para contextos como o acompanhamento de **idosos**, **crianças** ou até **animais de estimação**, onde é importante garantir que não se afastem demasiado de uma zona segura.

## 🛠️ Funcionalidades

- Deteção de dispositivos BLE próximos.
- Estimativa de distância baseada no sinal RSSI.
- Alerta sonoro (`alert.mp3`) sempre que o dispositivo ultrapassa a distância configurada.
- Totalmente personalizável com base no endereço MAC e raio de segurança.

## 📁 Estrutura do Projeto

- `scanner.py`: Script para encontrar o MAC address do dispositivo BLE pretendido.
- `BLE_fence.py`: Script principal que monitoriza a distância do dispositivo e emite o alerta.
- `alert.mp3`: Som do alerta, tocado quando a distância máxima é ultrapassada.

## 🧪 Requisitos

- Python 3.10 ou superior.
- [Bleak](https://pypi.org/project/bleak/) – biblioteca para interagir com dispositivos BLE.
- [playsound](https://pypi.org/project/playsound/) – usada para tocar o alerta sonoro.

### Instalação

```bash
pip install bleak playsound==1.2.2
```

> ⚠️ Recomenda-se a versão `1.2.2` do `playsound` no Windows.

## 🚀 Como Usar

1. **Encontrar o MAC address** do dispositivo BLE:

   ```bash
   python scanner.py
   ```

   Copia o endereço `MAC` do dispositivo pretendido.

2. **Editar o ficheiro `BLE_fence.py`**:
   Substitui a linha:

   ```python
   mac_do_telemovel = "43:52:C4:21:0E:65"
   ```

   pelo MAC address obtido no passo anterior.

3. **Correr o sistema de cerca eletrónica**:
   ```bash
   python BLE_fence.py
   ```

## ⚙️ Personalização

- **Alterar a distância máxima**:
  No topo do ficheiro `BLE_fence.py`, modifica:

  ```python
  DISTANCE = 5  # em metros
  ```

- **Alterar o som do alerta**:
  Substitui o ficheiro `alert.mp3` por outro com o nome igual na mesma pasta.

## 🧠 Exemplo de Aplicação

- **Cuidados com idosos**: o cuidador é alertado quando o idoso sai de uma zona segura (ex: casa ou jardim).
- **Segurança infantil**: em parques, eventos ou centros comerciais, garante que a criança permanece próxima.
- **Animais de estimação**: monitoriza se o animal sai do raio definido.

---

## 📌 Observações

- A estimativa de distância com base no RSSI não é exata — interferências e obstáculos físicos podem afetar o resultado.
- Testado em Windows com Python 3.11.3. Requer permissões de Bluetooth ativas.

---

## 🧑‍💻 Autor

Diogo Guerra
Projeto desenvolvido no âmbito de estudos em Computação Móvel.
