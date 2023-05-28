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
function verificationRegistration(name, firstName, phoneNumber, email, password) {
    // Validate the phone number.
    var phoneNumber = "771234567";
    var regex = /^(77|78|70|76|75)\d{7}$/;
    var isValid = regex.test(phoneNumber);
    console.log(isValid); // Résultat : true
    
  
    // Validate the name and first name.
    regex = /^[a-zA-Z]+$/;
    if (!regex.test(Prénom),Nom || !regex.test(Prénom,Nom)) {
      return false;
    }
  
    // Validate the email.
    regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!regex.test(email)) {
      return false;
    }
  
    // Validate the password.
    regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{8,}$/;
    if (!regex.test(password)) {
      return false;
    }
  
    // The registration is valid.
    return true;
  }

if (verificationRegistration(Prénom, Nom, téléphone, email, password)) {
  // The registration is valid.
  showAlert("Enregistrement avec succès.", "green");
} else {
  // The registration is not valid.
  showAlert("Votre enregistrement n'est pas valide. Veuillez corriger les erreurs et réessayer !", "red");
}

function showAlert(message, color) {
  var alertStyle = "color: " + color + "; position: fixed; bottom: 0; width: 100%; text-align: center; font-size: 18px;";
  var alertHTML = '<div style="' + alertStyle + '">' + message + '</div>';
  document.body.insertAdjacentHTML('beforeend', alertHTML);
}


  

  

// #####################################FIN_LATYR###############################################