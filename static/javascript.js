
function get_node(string){
	const division = document.createElement("div");
	const node = document.createTextNode(string);
	division.appendChild(node)
	return division
}

function add_response(response){

	document.getElementById("div1").appendChild(get_node(response[0])).className="send";
	document.getElementById("div1").appendChild(get_node(response[1])).className="receive";	
}

$(function() {
$('button').click(function() {
	
	document.getElementById("intro").innerHTML = "";
	document.getElementById("intro1").innerHTML = "";
	
	$.ajax({
		url: '/',
		data: $('form').serialize(),
		type: 'POST',
		success: function(response) {
			add_response(response);			
			},
			error: function(error){
			console.log(error);
			}
		});
	});
});
