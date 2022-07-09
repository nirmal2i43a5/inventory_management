
function login(){
    username = document.getElementById("exampleInputUsername").value;
    email = document.getElementById("exampleInputUsername").value;
    password = document.getElementById("exampleInputPassword").value;
    csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    $("#errorlogin").html("");

    $.ajax({
        type:"POST",
        url:'/user/login/',
        data:{
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
            'username':username,
            'email':email,
            'password':password,
        },
        success : function(data){
            console.log(data);
            if(data['message'] == "Success"){
                location.reload();
            }
            else if(data['message'] == "inactive"){
                $("#errorlogin").html("Please verify this E-mail address.");
            }
            else{
                $("#errorlogin").html("The E-mail and Password do not match.");
            }
        }
    });
}


//     function signup(){
//         email = document.getElementById("exampleInputEmail").value;
//         fname = document.getElementById("exampleInputFname").value;
//         lname = document.getElementById("exampleInputLname").value;
//         password1 = document.getElementById("exampleInputPassword1").value;
//         password2 = document.getElementById("exampleInputPassword2").value;
//         csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
//         $("#erroremail").html("");
//         $("#errorpass").html("");
//         if(fname == "" || lname == ""){
//             $("#errorname").html("First Name and Last Name Required");
//         }
//         else{
//         $.ajax({
//         type:"POST",
//         url:'/signup/',
//         data:{
//             'csrfmiddlewaretoken': csrfmiddlewaretoken,
//         //   'first_name':fname,
//         //   'last_name':lname,
//           'email':email,
//           'password1':password1,
//           'password2':password2,
//         },
//         success : function(data){
//             console.log(data['message']);
//             if(data['message'] == "Success"){
//                 window.location = "/"
//             }
//             else{
//                 if("email" in data['message'])
//                     $("#erroremail").html(data['message']['email'][0]);
//                 if("password2" in data['message'])
//                     $("#errorpass").html(data['message']['password2'][0]);
//             }
//         }
//     })
//     }
//   }
