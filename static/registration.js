
    $( "#password" ).focus(function() {
            $(this).css("border-color", "#0080ff");

    });
    $( "#firstname" ).focus(function() {
            $(this).css("border-color", "#0080ff");

    });
    $( "#lastname" ).focus(function() {
            $(this).css("border-color", "#0080ff");

    });
    $( "#phoneno" ).focus(function() {
            $(this).css("border-color", "#0080ff");

    });
    $( "#email" ).focus(function() {
            $(this).css("border-color", "#0080ff");

    });
    $( "#password" ).focusout(function() {
        var value = $(this).val()
        if( checkpassword(value)==1 )
        {
            $(this).css("border-color", "#FF0000");
        }else{
            $(this).css("border-color", "#00CD00");
        }
    })
    $("#firstname" ).focusout(function() {
        var value = $(this).val()
        if (checkfirstname(value) == 1) {
            $(this).css("border-color", "#FF0000");
        } else {
            $(this).css("border-color", "#00CD00");
        }
    })
    $("#lastname" ).focusout(function() {
        var value = $(this).val()
        if (checklastname(value) == 1) {
            $(this).css("border-color", "#FF0000");
        } else {
            $(this).css("border-color", "#00CD00");
        }
    })
    $("#email" ).focusout(function() {
        var value = $(this).val()
        if (checkemail(value) == 1) {
            $(this).css("border-color", "#FF0000");
        } else {
            $(this).css("border-color", "#00CD00");
        }
    })
    $("#phoneno" ).focusout(function() {
        var value = $(this).val()
        if (checkphone(value) == 1) {
            $(this).css("border-color", "#FF0000");
        } else if (checkphone(value) == 2) {
            $(this).css("border-color", "#cccccc");
        } else{
            $(this).css("border-color", "#00CD00");
        }
    })


  function checkpassword(value){
        document.getElementById('passwordstatus').style.color="red";
      if(value.length < 8 || value.length>16) {
        document.getElementById('passwordstatus').innerHTML ='X Password must be between 8 and 16 characters'+"<br />"+"<br />";
          return 1;
      }else if(value.indexOf(' ')>=0){
          document.getElementById('passwordstatus').innerHTML ='X Password must not contain whitespaces'+"<br />"+"<br />";
          return 1
      }
      else {
          document.getElementById('passwordstatus').innerHTML ='';
          return 0;
      }
  }
  function checkphone(value){
      document.getElementById('phonenostatus').style.color="red";
      if(value.length == 0) {
          document.getElementById('phonenostatus').innerHTML ='';
          return 2
      }
      if(value.length !=10) {
          if(value.indexOf(' ')>=0 && hasAlphabet(value)) {

              document.getElementById('phonenostatus').innerHTML ='X Phone number must not contain whitespaces, contain alphabet, and contain exactly 10 digits'+"<br />"+"<br />";
              return 1
          } else if(value.indexOf(' ')>=0) {
              document.getElementById('phonenostatus').innerHTML ='X Phone number must not contain whitespaces'+"<br />"+"<br />";
               return 1
          }else if(hasAlphabet(value)){
              document.getElementById('phonenostatus').innerHTML ='X Phone number must not contain alphabet'+"<br />"+"<br />";
              return 1
          } else {
              document.getElementById('phonenostatus').innerHTML ='X Phone number must contain 10 digits'+"<br />"+"<br />";
              return 1
          }
      } else {
          if(value.indexOf(' ')>=0 && hasAlphabet(value)) {
              document.getElementById('phonenostatus').innerHTML ='X Phone number must not contain whitespaces, contain alphabet, and contain exactly 10 digits'+"<br />"+"<br />";
              return 1
          } else if(value.indexOf(' ')>=0) {
               alert("Phonenumber must not contain whitespaces")
              document.getElementById('phonenostatus').innerHTML ='X Phone number must not contain whitespaces'+"<br />"+"<br />";
               return 1
          }else if(hasAlphabet(value)){
              document.getElementById('phonenostatus').innerHTML ='X Phone number must not contain alphabet'+"<br />"+"<br />";
              return 1
          } else {
              document.getElementById('phonenostatus').innerHTML ='';
              return 0
          }
      }
       /* alert("Phonenumber must contain 10 digits")
        return 1;
      }
      #else if(value.indexOf(' ')>=0){
          alert("Phonenumber must not contain whitespaces")
          return 1
      }
      else if(hasAlphabet(value)){
          alert("Phonenumber must not contain alphabet")
          return 1
      }
      else {
          return 0;
      }*/
  }
  function checkfirstname(value){
      document.getElementById('firstnamestatus').style.color="red";
   if(value.length <=1) {
       document.getElementById('firstnamestatus').innerHTML ='X Please enter your name'+"<br />"+"<br />";
        return 1;
    }
    else if(hasNumber(value)){
       document.getElementById('firstnamestatus').innerHTML ='X Name must not contain number'+"<br />"+"<br />";
        return 1
    } else {
        document.getElementById('firstnamestatus').innerHTML ='';
          return 0;
      }
  }
  function checklastname(value){
      document.getElementById('lastnamestatus').style.color="red";
   if(value.length <=1) {
       document.getElementById('lastnamestatus').innerHTML ='X Please enter your name'+"<br />"+"<br />";
        return 1;
    }
    else if(hasNumber(value)){
       document.getElementById('lastnamestatus').innerHTML ='X Name must not contain number'+"<br />"+"<br />";
        return 1
    } else {
        document.getElementById('lastnamestatus').innerHTML ='';
          return 0;
      }
  }
  function checkemail(value){
      document.getElementById('emailstatus').style.color="red";
          if(hasAt(value) && hasDot(value)){
              document.getElementById('emailstatus').innerHTML ='';
              return 0
          }else{
              document.getElementById('emailstatus').innerHTML ='X Invalid email address'+"<br />"+"<br />";
              return 1;
          }
  }
function hasNumber(myString) {
    return /\d+/.test(myString);
}
function hasAt(myString) {
    if((myString.split("@").length-1)>1){
        return false
    } //Check how many "@"
    var att = new RegExp("@");
    return att.test(myString);
}
function hasDot(myString) {
    return /\./.test(myString)

}
function hasAlphabet(myString) {
    return /[a-zA-Z]/.test(myString)
}
function checkall() {
  var firstnamevalue = $('#firstname').val();
  var lastnamevalue = $('#lastname').val();
  var passwordvalue = $('#password').val();
  var emailvalue = $('#email').val();
  var phonenovalue = $('#phoneno').val();

    if(checkfirstname(firstnamevalue) == 1 ||
      checklastname(lastnamevalue) == 1 ||
      checkpassword(passwordvalue) == 1 ||
      checkemail(emailvalue) == 1 ||
      checkphone(phonenovalue) ==1) {
        alert("กรุณากรอกข้อมูลให้ครบและถูกต้อง");
      return false;
    }
}

