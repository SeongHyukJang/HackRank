let elem = document.getElementById("res");

function Zero()
{
    elem.innerHTML += '0';
}

function One()
{
    elem.innerHTML += '1';
}

function Sum()
{
    elem.innerHTML += '+';
}

function Sub()
{
    elem.innerHTML += '-';
}

function Mul()
{
    elem.innerHTML += '*';
}

function Div()
{
    elem.innerHTML += '/';
}

function Clr()
{
    elem.innerHTML = '';
}

function Eql()
{
    let re = /[+|-|*|/]/;
    let operator = re.exec(elem.innerHTML);
    let numbers = elem.innerHTML.split(operator);
    
    let res;
    if(operator == "+"){res = parseInt(numbers[0],2) + parseInt(numbers[1],2);}
    else if(operator == "-"){res = parseInt(numbers[0],2) - parseInt(numbers[1],2);}
    else if(operator == "*"){res = parseInt(numbers[0],2) * parseInt(numbers[1],2);}
    else if(operator == "/"){res = parseInt(numbers[0],2) / parseInt(numbers[1],2);}
    elem.innerHTML = res.toString(2);
}

// index.html
/*
<!-- Enter your HTML code here -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Binary Calculator</title>
        <link rel="stylesheet" href="css/binaryCalculator.css" type="text/css">
    </head>
    <body>
        <div id = "container">
            <div id = "res"></div>
            <div id = "btns">
                <button id = "btn0" onclick = "Zero()">0</button>
                <button id = "btn1" onclick = "One()">1</button>
                <button id = "btnClr" onclick = "Clr()">C</button>
                <button id = "btnEql" onclick = "Eql()">=</button>
                <button id = "btnSum" onclick = "Sum()">+</button>
                <button id = "btnSub" onclick = "Sub()">-</button>
                <button id = "btnMul" onclick = "Mul()">*</button>
                <button id = "btnDiv" onclick = "Div()">/</button>
            </div>
        </div>
        <script src="js/binaryCalculator.js" type="text/javascript"></script>    
    </body>
</html>
*/

// binaryCalculator.css
/*
  body
{
    width:33%
}

#res
{
    background-color : lightgray;
    border : solid;
    height : 48px;
    font-size : 20px;
}

#btn0, #btn1
{
    background-color : lightgreen;
    color : brown;
}

#btnClr, #btnEql
{
    background-color : darkgreen;
    color : white;
}

#btnSum, #btnSub, #btnMul, #btnDiv
{
    background-color : black;
    color : red;
}

#btns button
{
    width : 25%;
    height : 36px;
    font-size : 18px;
    margin : 0px;
    float : left;
}
*/