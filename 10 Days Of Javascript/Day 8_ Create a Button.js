let num = 1;

function btnClick()
{
    document.getElementById("btn").innerHTML = num++;
}


// index.html
/*
<!-- Enter your HTML code here -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Button</title>
        <link rel="stylesheet" href="css/button.css" type="text/css">
    </head>
    <body>
        <script src="js/button.js" type="text/javascript"></script>
        <button onclick = "btnClick()" id = "btn">0</button>
    </body>
</html>
*/

//button.css
/*
#btn
{
    width : 96px;
    height : 48px;
    font-size : 24px;
}
*/