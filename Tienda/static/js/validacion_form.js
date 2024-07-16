// Validacion ingreso de Usuarios

$(function () {
  $("#registro").validate({
    rules: {
      first_name: {
        required: true,
        lettersonly: true,
        minlength: 3,
      },
      email: {
        required: true,
        email: true,
      },
      username: {
        required: true,
        minlength: 3,
      },
      password1: {
        required: true,
        minlength: 3,
      },
      password2: {
        required: true,
        equalTo: "#pass1",
      },
    },
    messages: {
      first_name: {
        required: "Debe ingresar su nombre*",
        minlength: "Caracteres insuficientes*",
        lettersonly: "El nombre solo debe contener letras*",
      },
      email: {
        required: "Debe ingresar un correo*",
        email: "Debe tener un formato válido de correo*",
      },
      username: {
        required: "Debe ingresar su usuario*",
        minlength: "caracteres insuficientes*",
      },
      password1: {
        required: "Ingrese una contraseña*",
        minlength: "caracteres insuficientes*",
      },
      password2: {
        required: "Ingrese una contraseña*",
        equalTo: "Las contraseñas no son iguales*",
      },
    },
  });

  // Método adicional para validar solo letras
  $.validator.addMethod(
    "lettersonly",
    function (value, element) {
      return this.optional(element) || /^[a-zA-Z]+$/.test(value);
    },
    "Solo se permiten letras"
  );
});
