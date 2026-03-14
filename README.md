# Python Lesson 03 — Conditional Logic and Calculations

This README contains **two languages**:

English  
Español

The same explanation is provided in both sections.

---

# Lesson 03 — Conditional Logic with a Simple Program

```text
👋 Hello.

This is Programming I level, and in this README I will explain how this program works.
I hope it is useful to you.

The code for this lesson is included in this repository.
You can open the script and explore the program directly.

The goal of the program is simple:

The user chooses between two options:
1 → Cookies
2 → Cakes

After that, the user enters how many they want to make.

The program then calculates how many ingredients are required.
```

---

# Program idea

```text
📘 This program demonstrates a very common concept in programming.

User input → decision → calculations → output

Step 1
The program asks the user to choose an option.

Step 2
The program asks how many items will be produced.

Step 3
Using conditional logic (if / elif / else),
the program determines which ingredients should be calculated.

Step 4
The program multiplies the ingredient amounts by the quantity entered.
```

---

# User input

```text
⌨️ The program first asks the user to select a product.

Example:

1 → Cookies
2 → Cakes

The program then asks for the quantity.

Both inputs are converted to integers using int()
because the program needs numbers for calculations.
```

---

# Conditional logic

```text
 The decision in this program is handled using:

if
elif
else

This structure allows the program to execute
different blocks of code depending on the user's choice.

If the user selects 1 → cookie ingredients are calculated.

If the user selects 2 → cake ingredients are calculated.

If the user enters something else →
the program displays an error message.
```

---

# Calculations

```text
 The ingredient quantities are calculated using multiplication.

Example idea:

ingredient_needed = quantity * ingredient_per_unit

This means the program scales the recipe
based on how many items the user wants to produce.

Example:

If one cookie requires:
100g flour

Then:

5 cookies → 5 * 100 = 500g flour
```

---

# Why this example is useful

```text
 Even though this is a simple program,
it demonstrates several important beginner concepts:

• user input
• conditional logic
• arithmetic calculations
• structured program flow

These ideas appear in many real programs,
especially when building small systems
that calculate or process information.
```

---

# Personal learning note

```text
 This example comes from Programming I level practice.

Small programs like this are very useful
for understanding how programs make decisions
and perform calculations based on user input.

Learning programming is not about writing huge systems at first.

It is about understanding the small building blocks.
```

---

# == ESPAÑOL ==

# Lección 03 — Lógica condicional y cálculos

```text
 Hola.

Esto es nivel Programación I, y en este README les explicaré cómo funciona este programa.
Espero les sea de utilidad.

El código de esta lección se encuentra dentro de este repositorio.
Puedes abrir el script y explorar el programa directamente.

El objetivo del programa es simple:

El usuario elige entre dos opciones:
1 → Galletas
2 → Pasteles

Después el usuario indica cuántos desea hacer.

El programa calcula automáticamente
la cantidad de ingredientes necesarios.
```

---

# Idea del programa

```text
 Este programa muestra un concepto muy común en programación.

Entrada del usuario → decisión → cálculos → resultado

Paso 1
El programa pide al usuario elegir una opción.

Paso 2
El programa pide la cantidad que se desea producir.

Paso 3
Usando lógica condicional (if / elif / else),
el programa determina qué ingredientes calcular.

Paso 4
El programa multiplica los ingredientes
por la cantidad indicada por el usuario.
```

---

# Entrada del usuario

```text
Primero el programa pide al usuario elegir un producto.

Ejemplo:

1 → Galletas
2 → Pasteles

Después el programa pide la cantidad.

Ambos valores se convierten a enteros usando int()
porque el programa necesita números para hacer cálculos.
```

---

# Lógica condicional

```text
 La decisión del programa se maneja usando:

if
elif
else

Esta estructura permite ejecutar
diferentes partes del código
dependiendo de la elección del usuario.

Si el usuario elige 1 → se calculan galletas.

Si el usuario elige 2 → se calculan pasteles.

Si el usuario escribe otro número →
el programa muestra un mensaje de error.
```

---

# Cálculos

```text
 Las cantidades de ingredientes se calculan usando multiplicación.

Idea básica:

ingrediente_total = cantidad * ingrediente_por_unidad

Esto permite escalar la receta
dependiendo de cuántos productos se quieren hacer.

Ejemplo:

Si una galleta necesita:
100g de harina

Entonces:

5 galletas → 5 * 100 = 500g de harina
```

---

# Por qué este ejemplo es útil

```text
 Aunque es un programa sencillo,
muestra varios conceptos importantes para principiantes:

• entrada de usuario
• lógica condicional
• cálculos matemáticos
• flujo de ejecución del programa

Estas ideas aparecen en muchos programas reales,
especialmente en sistemas que procesan datos
o realizan cálculos.
```

---

# Nota personal

```text
 Este ejemplo proviene de ejercicios de nivel Programación I.

Programas pequeños como este ayudan
a entender cómo los programas toman decisiones
y realizan cálculos basados en datos del usuario.

Aprender programación no empieza con sistemas enormes.

Empieza entendiendo bien los bloques básicos.
```
