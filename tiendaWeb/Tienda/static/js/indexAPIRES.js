const { response } = require("express");

function pag() {
  miAPIRES();
}

function miAPIRES() {
  const url = "http://localhost:3000/productos";

  fetch(url)
    .then((response) => response.json())
    .then((data) => cardProducto(data))
    .catch((error) => console.log(error));

  const cardProducto = (data) => {
    console.log(data);
    let card = "";

    for (let i = 0; i < data.length; i++) {
      card += `
            <div class="card">
            <a href="producto_card.html" class="link_card">
            <img src="${data[i].img}" class="card-img-top" alt="..." />
            <div class="card-body">
            <h5 class="card-title">${data[i].nombre}</h5>
            <div class="precio">
                <p>
                  Precio:
                  <span> $${data[i].precio} </span>
                </p>
            </div>
            </div>
            <span class="mensaje">
              ${data[i].descripcion}
            </span>
            </a>
            </div>
            `;
    }

    document.getElementById("contenedor_cartas").innerHTML = card;
  };
}

/* 
<div class="card">
          <a href="producto_card.html" class="link_card">
            <img src="img/soap (1).jpg" class="card-img-top" alt="..." />
            <div class="card-body">
              <h5 class="card-title">Jabón de lavanda</h5>
              <div class="precio">
                <p>
                  Precio:
                  <span> $3.000 </span>
                </p>
              </div>
            </div>
            <span class="mensaje">
              Calmante y relajante, ideal para una experiencia de baño rejuvenecedora y aromática.
            </span>
          </a>
          <!-- link -->
        </div><!-- .card -->
*/


function fetchHoroscope() {
  const url =
    "https://horoscopes-ai.p.rapidapi.com/get_horoscope/aries/today/wellness/es";
  const options = {
    method: "GET",
    headers: {
      "X-RapidAPI-Key": "eca2cebc3fmshb61459aed2b724dp129bc2jsn9041ddb98e9d",
      "X-RapidAPI-Host": "horoscopes-ai.p.rapidapi.com",
    },
  };

  fetch(url, options)
    .then((response) => {
      // Capturar el estado de la respuesta
      const status = response.status;
      // Convertir la respuesta a JSON
      return response.json().then((data) => ({ status, data }));
    })
    .then((result) => {
      const { status, data } = result;
      // Llamar a la función para manejar el resultado
      horoscopo(status, data);
    })
    .catch((error) => console.log(error));
}

function horoscopo(status, data) {
  console.log(data)
  let texto = "";
  let t = "";
  if (status === 429) {
    texto = "<h1>Funciona, pero no se muestra debido al estado 429</h1>";
  } else {
    texto += `
      <p><strong>Signo:</strong> ${data.sign}</p>
      <p><strong>Período:</strong> ${data.period}</p>
      <p><strong>Bienestar:</strong> ${data.wellness[0]}</p>
    `;
    t += `
    Signo: ${data.sign}
    Período: ${data.period}
    Bienestar: ${data.wellness[0]}
    `
  }
  
  // Mostrar el resultado en un elemento con el id "horoscopo"
  alert(t)
  document.getElementById("horoscopo").innerHTML = texto;
}



