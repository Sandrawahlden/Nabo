window.onload = start;

function start(){
	console.log("Sidan har nu laddat klart")
	document.getElementById("button1").onclick = checkForm;

//CheckForm
function checkForm() {
	
    if(form.username.value == "") {
      alert("Error: Username cannot be blank!");
      form.username.focus();
      return false;
    }

    if(form.pwd_1.value != "" && form.pwd_1.value == form.pwd_2.value) {
      
      if(form.pwd_1.value == form.username.value) {
        alert("Error: Password must be different from Username!");
        form.pwd_1.focus();
        return false;
      }
	  
    } else {
      alert("Error: Please check that you've entered and confirmed your password!");
      form.pwd_1.focus();
      return false;
    }

    alert("You entered a valid password: " + form.pwd_1.value);
    return true;
}