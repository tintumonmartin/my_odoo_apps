function generateCaptcha()
{
const myInput = document.getElementById('mainCaptcha');
console.log("Testing Captcha")

myInput.oncopy = function(e) { e.preventDefault(); }
  var text = "";

  var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  for (var i = 0; i < 5; i++)
    text += possible.charAt(Math.floor(Math.random() * possible.length));

    var code =  text;
    document.getElementById("mainCaptcha").value = code;
    document.getElementById('txtInput').value = "";
    document.getElementById('error').innerHTML = "";
    document.getElementById('success').innerHTML = "";
    document.getElementById('loginButton').disabled = true;
    document.getElementById('signupButton').disabled = true;
}
function CheckValidCaptcha(){
    var string1 = removeSpaces(document.getElementById('mainCaptcha').value);
    var string2 = removeSpaces(document.getElementById('txtInput').value);
    if (string1 == string2){
      document.getElementById('success').innerHTML = "Captcha Matching!";
      document.getElementById('loginButton').disabled = false;
      document.getElementById('signupButton').disabled = false;
      return true;
    }
    else{
      document.getElementById('error').innerHTML = "Please enter a valid captcha.";
      document.getElementById('loginButton').disabled = true;
      document.getElementById('signupButton').disabled = true;
      return false;
    }
}

function removeSpaces(string){
  return string.split(' ').join('');
}

function onChangeTest() {
  var onChange = document.getElementById('txtInput').value.length;
  if(onChange >= 5){
    CheckValidCaptcha();
  } else if(onChange >= 4){
    document.getElementById('error').innerHTML = "";
    document.getElementById('success').innerHTML = "";
  }
}


