var container = document.getElementById('container')
var slider = document.getElementById('slider');
var slides = document.getElementsByClassName('slide').length;
var buttons = document.getElementsByClassName('btn');


var currentPosition = 0;
var currentMargin = 0;
var slidesPerPage = 0;
var slidesCount = slides - slidesPerPage;
var containerWidth = container.offsetWidth;
var prevKeyActive = false;
var nextKeyActive = true;

window.addEventListener("resize", checkWidth);

function checkWidth() {
    containerWidth = container.offsetWidth;
    setParams(containerWidth);
}

function setParams(w) {
    if (w < 551) {
        slidesPerPage = 1;
    } else {
        if (w < 901) {
            slidesPerPage = 2;
        } else {
            if (w < 1101) {
                slidesPerPage = 3;
            } else {
                slidesPerPage = 4;
            }
        }
    }
    slidesCount = slides - slidesPerPage;
    if (currentPosition > slidesCount) {
        currentPosition -= slidesPerPage;
    };
    currentMargin = - currentPosition * (100 / slidesPerPage);
    slider.style.marginLeft = currentMargin + '%';
    if (currentPosition > 0) {
        buttons[0].classList.remove('inactive');
    }
    if (currentPosition < slidesCount) {
        buttons[1].classList.remove('inactive');
    }
    if (currentPosition >= slidesCount) {
        buttons[1].classList.add('inactive');
    }
}

setParams();

function slideRight() {
    if (currentPosition != 0) {
        slider.style.marginLeft = currentMargin + (100 / slidesPerPage) + '%';
        currentMargin += (100 / slidesPerPage);
        currentPosition--;
    };
    if (currentPosition === 0) {
        buttons[0].classList.add('inactive');
    }
    if (currentPosition < slidesCount) {
        buttons[1].classList.remove('inactive');
    }
};

function slideLeft() {
    if (currentPosition != slidesCount) {
        slider.style.marginLeft = currentMargin - (100 / slidesPerPage) + '%';
        currentMargin -= (100 / slidesPerPage);
        currentPosition++;
    };
    if (currentPosition == slidesCount) {
        buttons[1].classList.add('inactive');
    }
    if (currentPosition > 0) {
        buttons[0].classList.remove('inactive');
    }
};

// #####################################LATYR###############################################*
function register(event) {
    event.preventDefault();
  
    var nom = document.getElementById('nom').value;
    var prenom = document.getElementById('prenom').value;
    var email = document.getElementById('email').value;
    var telephone = document.getElementById('telephone').value;
    var adresse = document.getElementById('adresse').value;
    var motDePasse = document.getElementById('passeword').value;
    var motDePasse2 = document.getElementById('passeword').value;
  
    var errors = [];
  
    var regex = /^[a-zA-Z]+$/;
    if (!regex.test(nom) || !regex.test(prenom)) {
      errors.push('Nom et prénom doivent contenir uniquement des lettres.');
    }
  
    regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!regex.test(email)) {
      errors.push('Adresse email invalide.');
    }
  
    regex = /^(77|78|70|76|75)\d{7}$/;
    if (!regex.test(telephone)) {
      errors.push('Numéro de téléphone invalide.');
    }
  
    regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{8,}$/;
    if (motDePasse !== motDePasse2) {
      errors.push("Les mots de passe ne correspondent pas.");
    }
  
    if (errors.length > 0) {
      var errorElement = document.getElementById('error-message');
      errorElement.innerHTML = '';
      errorElement.classList.add('text-danger');
      errors.forEach(function (error) {
        var errorItem = document.createElement('p');
        errorItem.textContent = error;
        errorElement.appendChild(errorItem);
      });
    } else {
      // Soumettre le formulaire
      document.getElementById('inscription_form').submit();
    }
  }
  
  document.getElementById('inscription_form').addEventListener('submit', register);
  
  
  
  
  




  

  

// #####################################FIN_LATYR###############################################