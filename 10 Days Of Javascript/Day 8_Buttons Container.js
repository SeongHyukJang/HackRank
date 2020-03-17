let nums=[1,2,3,6,9,8,7,4];
const ids=[1,2,3,6,9,8,7,4];

let btn5=document.getElementById("btn5");

btn5.onclick=function() 
{
    nums.unshift(nums.pop());
    for (let i=0; i<nums.length; i++)
    {
        document.getElementById("btn"+ids[i]).innerHTML=nums[i];
    }
}

// index.html

/*
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="css/buttonsGrid.css" type="text/css">
    </head>
    
    <body>
        <div id="btns" class="buttonContainer">
        <button id="btn1" class="buttonClass">1</button>
        <button id="btn2" class="buttonClass">2</button>
        <button id="btn3" class="buttonClass">3</button>
        <button id="btn4" class="buttonClass">4</button>
        <button id="btn5" class="buttonClass">5</button>
        <button id="btn6" class="buttonClass">6</button>
        <button id="btn7" class="buttonClass">7</button>
        <button id="btn8" class="buttonClass">8</button>
        <button id="btn9" class="buttonClass">9</button>
        </div>
        <script src="js/buttonsGrid.js" type="text/javascript"></script>
    </body>
</html>
*/

// buttonGrid.css
/*
.buttonContainer{
    width: 75%;
}

.buttonContainer > .buttonClass{
    width: 30%;
    height: 48px;
    font-size: 24px;
}
*/