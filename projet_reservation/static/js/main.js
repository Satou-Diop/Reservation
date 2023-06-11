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




// pour le bouton supprimer

// Récupération de tous les boutons de classe "supprimer"
const boutonsSupprimer = document.querySelectorAll('.supprimer');

// Fonction pour supprimer l'élément parent du bouton cliqué
function supprimerElement() {
  const element = this.parentNode;
  element.parentNode.removeChild(element);
}

// Ajout d'un gestionnaire d'événement de clic pour chaque bouton
boutonsSupprimer.forEach(bouton => {
  bouton.addEventListener('click', supprimerElement);
});



//pour bouton editer


// Récupération de tous les boutons de classe "editer"
const boutonsEditer = document.querySelectorAll('.modifier');

// Fonction pour éditer le contenu de l'élément parent du bouton cliqué
function editerElement() {
  const element = this.parentNode;
  const texte = element.firstChild.textContent;
  const nouveauTexte = prompt('Modifier le texte', texte);

  if (nouveauTexte) {
    element.firstChild.textContent = nouveauTexte;
  }
}

// Ajout d'un gestionnaire d'événement de clic pour chaque bouton
boutonsEditer.forEach(bouton => {
  bouton.addEventListener('click', editerElement);
});