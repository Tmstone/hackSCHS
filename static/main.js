$(document).ready(function(){
    $('#rBtn').click(function(){
        $.get(" ");
    })
    $('#lBtn').click(function(){
        //$.get("templates/register.html")
        //$('.lForm').toggle();
        //add registration button link here
    })
    //validate login form here
    $('loginForm').submit(
        function(event) {
           var isValid = True;
           //add email validation here

           
           var password = $("#password").val().trim()
            var passwordPattern = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$';
            if (password == "") {
                $('#password').next().text("This field is required.")
            }
            else if (!passwordPattern.test(password)) {
                $("#password").next().text('* Please enter a valid password: 6-20 characters, A-Z and (# $ % @ &)');
                isValid = False;
            } 
            else {
                ('#password').next().text("");
            }
            ('#password').val(password);
            if (isValid == false) {
             event.preventDefault();   
            }
        }
    );
});