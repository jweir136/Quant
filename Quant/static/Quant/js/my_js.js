function signup()
{
	var email = document.getElementById("email1").value;
	//now take the email, and save it...
	//use a rpi websocket written in python to achieve this.
	var ws = new WebSocket("ws://127.0.0.1:1111/");
	ws.send(email);
}

function contact()
{
	var email = document.getElementById("email2").value;
	var message = document.getElementById("message").value;
	var name = document.getElementById("name").value;
	//send with websocket.
}