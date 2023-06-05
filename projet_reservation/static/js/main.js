// var container = document.getElementById('container')
// var slider = document.getElementById('slider');
// var slides = document.getElementsByClassName('slide').length;
// var buttons = document.getElementsByClassName('btn');


// var currentPosition = 0;
// var currentMargin = 0;
// var slidesPerPage = 0;
// var slidesCount = slides - slidesPerPage;
// var containerWidth = container.offsetWidth;
// var prevKeyActive = false;
// var nextKeyActive = true;

// window.addEventListener("resize", checkWidth);

// function checkWidth() {
//     containerWidth = container.offsetWidth;
//     setParams(containerWidth);
// }

// function setParams(w) {
//     if (w < 551) {
//         slidesPerPage = 1;
//     } else {
//         if (w < 901) {
//             slidesPerPage = 2;
//         } else {
//             if (w < 1101) {
//                 slidesPerPage = 3;
//             } else {
//                 slidesPerPage = 4;
//             }
//         }
//     }
//     slidesCount = slides - slidesPerPage;
//     if (currentPosition > slidesCount) {
//         currentPosition -= slidesPerPage;
//     };
//     currentMargin = - currentPosition * (100 / slidesPerPage);
//     slider.style.marginLeft = currentMargin + '%';
//     if (currentPosition > 0) {
//         buttons[0].classList.remove('inactive');
//     }
//     if (currentPosition < slidesCount) {
//         buttons[1].classList.remove('inactive');
//     }
//     if (currentPosition >= slidesCount) {
//         buttons[1].classList.add('inactive');
//     }
// }

// setParams();

// function slideRight() {
//     if (currentPosition != 0) {
//         slider.style.marginLeft = currentMargin + (100 / slidesPerPage) + '%';
//         currentMargin += (100 / slidesPerPage);
//         currentPosition--;
//     };
//     if (currentPosition === 0) {
//         buttons[0].classList.add('inactive');
//     }
//     if (currentPosition < slidesCount) {
//         buttons[1].classList.remove('inactive');
//     }
// };

// function slideLeft() {
//     if (currentPosition != slidesCount) {
//         slider.style.marginLeft = currentMargin - (100 / slidesPerPage) + '%';
//         currentMargin -= (100 / slidesPerPage);
//         currentPosition++;
//     };
//     if (currentPosition == slidesCount) {
//         buttons[1].classList.add('inactive');
//     }
//     if (currentPosition > 0) {
//         buttons[0].classList.remove('inactive');
//     }
// // };

var chambre_selectionner;
var mes_boutons = document.querySelectorAll('.btn_res')
mes_boutons.forEach(function(button) {
    button.addEventListener('click', function() {
      // Récupérer les informations spécifiques à ce bouton à partir de l'attribut 'data-info'
      chambre_selectionner = this.getAttribute('data-info');
      // Utiliser les informations spécifiques selon vos besoins
     
    });
  });

var confirmation = document.querySelector('.confirmer')

confirmation.addEventListener('click',()=>{
    var chambre = document.getElementById('id_chambre')
    chambre.value =chambre_selectionner
    console.log("Valeur =")
    console.log( chambre.value)
})

// Récupérer l'élément <form> par son id
var form = document.getElementById('myForm');

// Écouter l'événement "submit" du formulaire
form.addEventListener('submit', function(event) {
  event.preventDefault(); // Empêcher le comportement par défaut du formulaire (rechargement de la page)

  // Envoyer la requête de soumission du formulaire
  var formData = new FormData(form); // Créer un objet FormData pour collecter les données du formulaire
  var url = form.action; // Récupérer l'URL de traitement du formulaire
  var method = form.method; // Récupérer la méthode d'envoi du formulaire (POST dans cet exemple)

  // Effectuer la requête AJAX pour envoyer les données du formulaire
  form.submit();
});

var boutons = document.querySelectorAll('.accordion-button')
boutons.forEach(function(button) {
  button.addEventListener('click', function() {
    button.firstElementChild.checked=true
    
    // Utiliser les informations spécifiques selon vos besoins
   
  });
});
