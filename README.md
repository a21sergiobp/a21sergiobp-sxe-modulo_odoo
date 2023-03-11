# Módulo de xestión de préstamos de material
## Modelos
O módulo conta con tres modelos (material, cliente, e préstamo). O modelo material ten campos simples e relacionais. Cliente extende do modelo res.partner por delegación, e ten, como o anterior, campos simples e relacionais, e por último o modelo Préstamo, co cal relacionamos materiais e clientes.

## Interface
Poderemos ver un menú con tres campos, que teñen asociadas unhas vistas básicas, estes son Material, Cliente e Prestamo. Cliente e prestamo están compostos por unha vista de árbore e unha vista de formulario, mentres que o material está composto por unha vista kanban e unha vista formulario.
En estas vistas mostranse diversos campos que nos dan información sobre os rexistros. 

## Funcionamento
Este módulo permite crear clientes e materiais, e asocialos para saber que cliente usa o material, que material está dispoñible e cal no.

### Funcionamento xeral
Cando creamos un préstamo debemos asocialo con un cliente e un material. O material deixa de estar dispoñible facendo que non se poida crear outro prestamo con el ate que este se devolva. Tamén se controlan outras restriccións como que non se poida borrar un prestamo que aínda non se devolveu, ou que un prestamo xa devolto non se poida devolver outra vez.

### Borrado por código
Na vista de formulario (tanto do préstamo como do material) existe un botón que borra o rexistro seleccionado.

### Modificación por código
Cando creamos un préstamo modificase o estado do material, facendo que este pase a estar prestado e deixe de estar dispoñible.
Tamén existe unha serie de botóns na vista formulario do material que permiten cambiar o estado do mesmo, comprobando se a transición está permitida. 

### Creación por código
No modelo dos clientes se seleccionamos un cliente na vista de árbore aparece un botón co cal poderemos crear un material e un préstamo de exemplo para este cliente. Se se selecciona máis dun cliente ao mesmo tempo crease un erro indicando que tan só se pode seleccionar un.

### Campos calculados
No modelo cliente podemos ver na súa vista formulario un campo chamado "Préstamos activos" que conta cantas veces se repite o cliente no modelo préstamo e ten o campo devolto a false e outro campo chamado "Préstamos devoltos", que como o anterior conta cantas veces está o cliente no modelo préstamo, pero ca condición de que o campo devolto sexa verdadeiro.