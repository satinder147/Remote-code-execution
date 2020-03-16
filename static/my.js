function defaultText(x)
{

    var cpp='#include<iostream>\nusing namespace std;\nint main(){\n \n \n\/\/write your code here\n \n \nreturn 0;\n \n \n}';
    var java='java';
    if(x=='cpp')
    {
        document.getElementById("but").innerHTML="C++";
        document.getElementById('exampleFormControlTextarea1').innerHTML=cpp;
    }
    
    else
    {
        document.getElementById("but").innerHTML="JAVA";
        document.getElementById('exampleFormControlTextarea1').innerHTML=java;
    }

}
function disableButton()
{
  if(document.getElementById("compile").disabled==false)
  {
    //alert("dis");
    document.getElementById("compile").disabled=true;
  }

}
function enableButton()
{
  document.getElementById("compile").disabled=false;
}

function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        if(this.responseText=="success")
        {
          enableButton();
        }
      }
    };
    

    var text=document.getElementById('exampleFormControlTextarea1').value;
    //text=unescapeHTML(text);
    //console.log(text);
    var jso={code:text};
    sen=JSON.stringify(jso);
    // console.log(jso);
    // console.log(sen);
    xhttp.open("POST", "ajax", true);
    xhttp.setRequestHeader("Content-Type", "application/json;");
    xhttp.send(JSON.stringify(sen));
    
  }

  function checkTestCases()
  {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        
        alert(this.responseText);
      }
    };

    xhttp.open("GET", "test?msg=1", true);
    xhttp.send();
/*
    var url="ws://localhost:12345"
    
    var webSocket = new WebSocket(url,"protocolOne");
    webSocket.send("1"); 

    webSocket.onmessage = function (event) {
      console.log(event.data);
    }
    webSocket.close();
    */
  }
 