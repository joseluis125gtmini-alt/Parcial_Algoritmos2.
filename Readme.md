# Parcial Final – Grafos (Estructura de Datos)

**Institución:** Corporación Universitaria Remington (Uniremington)  
**Asignatura:** Estructura de Datos  
**Lenguaje:** Python 3  
**Librerías utilizadas:** `networkx`, `matplotlib`

---

## 📋 Descripción del Proyecto

Implementación algorítmica, representación gráfica y análisis estructural de un grafo dirigido a partir de una imagen asignada, aplicando el modelo a una situación del mundo real y evaluando su eficiencia de almacenamiento en memoria.

---

## 🧩 Parte 1: Interpretación del Grafo

A partir del análisis visual de la estructura asignada, se determinaron los siguientes componentes:

* **Vértices (V):** El grafo consta de **6 vértices**:
  V = {1, 2, 3, 4, 5, 6}

* **Aristas ($E$):** El grafo consta de **8 aristas dirigidas**:
  E = \{(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 4), (6, 1)\}

* **Clasificación:** Es un **grafo dirigido (dígrafo)** y **no ponderado**, ya que cada arista posee una flecha que define un único sentido de recorrido entre el vértice de origen y el de destino.

### Lista de Adyacencia resultante
```text
1 -> [2, 3]
2 -> [4]
3 -> [4, 5]
4 -> [6]
5 -> [4]
6 -> [1]